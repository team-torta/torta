from jma.models import Earthquake
from jma.models import EarthquakeDetail
from django.db import transaction

import xml.etree.ElementTree as ET
import urllib.request
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

# 登録する震度の閾値
regist_min_int = 3

@transaction.atomic
def analysis_xml(uuid):
    logger.info('*** exec utils.analysis.analysis_xml ***')
    uuid = '6c461de6-27fb-3ef6-b239-48f77c5607bc' #長野震度４
    # uuid = uuid[9:]
    url = 'http://www.data.jma.go.jp/developer/xml/data/' + uuid + '.xml'
    logger.debug(url)
    req = urllib.request.Request(url)

    # XMLを読み込み
    with urllib.request.urlopen(req) as response:
        XmlData = response.read()
    root = ET.fromstring(XmlData)

    # 気象庁XMLのBodyのネームスペース
    ns = '{http://xml.kishou.go.jp/jmaxml1/body/seismology1/}'

    # 地震の情報を取得
    bd = root.find(ns + 'Body')
    # 発生日時 ->　'.//' をつけると子孫配下を探す
    datetime_str = bd.find('.//' +ns + 'OriginTime').text
    # 最大震度 ->　Bodyタグ配下の子孫要素内で一番最初の'MaxInt'
    max_int = bd.find('.//' + ns + 'MaxInt').text
    # 震源地 ->　Bodyタグ配下の子孫要素内で一番最初の'Name'
    area_name = bd.find('.//' + ns + 'Name').text
        # 緯度経度はまだ

    # 登録
    eq = Earthquake(
        uuid=uuid,
        date=datetime_str[:19],
        maxint=max_int,
        epicenter=area_name,
        upddt=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    eq.save()

    # City(市区町村)階層から市区町村コード、市区町村の最大震度を取得
    for city in root.iter(ns + 'City'):
        code = city.find(ns + 'Code').text
        city_maxint = city.find(ns + 'MaxInt').text
        # 震度が閾値以上の場合、登録
        if int(city_maxint) >= regist_min_int:
            eqd = EarthquakeDetail(
                uuid=Earthquake.objects.get(id=eq.id), # 外部キーはEarthquakeオブジェクトから取らないと怒られる
                intensity=city_maxint,
                citycode=code)
            eqd.save() # 一括登録（bulk_create）使ってみたい
