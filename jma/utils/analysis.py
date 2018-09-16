from jma.models import Eearthquake

import xml.etree.ElementTree as ET
import urllib.request
import logging

logger = logging.getLogger(__name__)
# uuid = '10fc89ca-6a4d-3b99-9b94-a5ca7eb896ef'

def analysis_xml(uuid):
    logger.info('*** exec utils.analysis.analysis_xml ***')
    uuid = uuid[9:]
    url = 'http://www.data.jma.go.jp/developer/xml/data/' + uuid + '.xml'
    logger.debug(url)
    req = urllib.request.Request(url)


    # XMLを読み込み
    with urllib.request.urlopen(req) as response:
        XmlData = response.read()
    root = ET.fromstring(XmlData)

    # 気象庁XMLのBodyのネームスペース
    ns = '{http://xml.kishou.go.jp/jmaxml1/body/seismology1/}'

    # City(市区町村)階層から市区町村コード、最大震度を取得
    for city in root.iter(ns + 'City'):
        code = city.find(ns + 'Code').text
        maxint = city.find(ns + 'MaxInt').text
        # 登録
        eq = Eearthquake(uuid=uuid, code=code, intensity=maxint)
        eq.save() # 一括登録（bulk_create）使ってみたい
