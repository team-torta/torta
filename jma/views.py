from django.shortcuts import render
from django.http import HttpResponse

from .utils.analysis import analysis_xml
import feedparser
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
