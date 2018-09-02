from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)


def index(request):
    logger.info('*** exec viwes.index ***')
    context = {'hoge': 'hoge'}
    return render(request, 'jma/index.html', context)
