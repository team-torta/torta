from django.shortcuts import render
from django.http import HttpResponse

from .utils.analysis import analysis_xml
from .models import AreaInformationCity
from .models import EarthquakeDetail
from collections import OrderedDict
import feedparser
import json
import logging
logger = logging.getLogger(__name__)

# 気象庁Atomフィード（地震火山）
URL_EQVOL = 'https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml'


def index(request):
    logger.info('*** exec viwes.index ***')
    context = {'hoge': 'hoge'}
    return render(request, 'jma/index.html', context)


def feedList(request):
    logger.info('*** exec viwes.feedList ***')
    entries = feedparser.parse(URL_EQVOL)['entries']
    # logger.debug(entries)
    context = {'entries': entries}
    return render(request, 'jma/feedList.html', context)


def analysis(request):
    logger.info('*** exec viwes.analysis ***')
    logger.debug(request)
    # id = request.GET.get(key="id", default="none")

    if "id" in request.GET:
        # idが指定されている場合の処理
        # ここで解析関数を呼ぶ
        logger.debug(analysis_xml(request.GET.get(key="id", default="none")))

        return HttpResponse("call = " + request.GET.get(key="id", default="none"))
    else:
        # idが指定されていない場合の処理
        return HttpResponse("error!!")


def aci_data(request):
    acis = []
    for aci in AreaInformationCity.objects.all().order_by('id'):

        aci_dict = OrderedDict([
            ('id', aci.id),
            ('code', aci.code),
            ('name', aci.name),
            ('lon', aci.lon),
            ('lat', aci.lat),
        ])
        acis.append(aci_dict)

    data = OrderedDict([('acis', acis)])
    return render_json_response(request, data)


def eq_data(request):
    eqs = []
    for eq in EarthquakeDetail.objects.all().order_by('id'):

        eqs_dict = OrderedDict([
            ('id', eq.id),
            ('intensity', eq.intensity),
            ('citycode', eq.citycode),
        ])
        eqs.append(eqs_dict)

    data = OrderedDict([('eqs', eqs)])
    return render_json_response(request, data)


def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response
