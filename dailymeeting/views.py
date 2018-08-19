from django.views.generic import CreateView
from django.shortcuts import render

from .models import Day
from .models import Member
from .forms import DayForm

from .utils.team import create_teams
import logging

logger = logging.getLogger(__name__)

# チーム数
team_num = 4


def index(request):
    logger.info('*** exec viwes.index ***')
    day_list = Day.objects.order_by('-day')[:10]
    context = {'day_list': day_list}
    logger.debug(create_teams(members, team_num))
    return render(request, 'dailymeeting/index.html', context)


def grouping(request):
    logger.info('*** exec viwes.grouping ***')
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'dailymeeting/grouping.html', context)


def get_group(request):
    logger.info('*** exec viwes.get_group ***')
    context = {'result': view_group(create_teams(Member.objects.all(),
                                                 team_num))}
    return render(request,
                  'dailymeeting/get_group.html',
                  context)


def view_group(groups):
    result = ""
    for index, group in enumerate(groups):
        result += str(index+1)
        result += ":"
        for index, member in enumerate(groups[group]):
            result += str(member)
            result += "、"
        result += "\n"
    return result


class DayCreateView(CreateView):
    logger.info('*** exec viwes.DayCreateView ***')
    model = Day
    form_class = DayForm
    template_name = "dailymeeting/day_create_form.html"
    success_url = "/dailymeeting/"  # 成功時にリダイレクトするURL
