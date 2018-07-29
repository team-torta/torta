from django.views.generic import CreateView
from django.shortcuts import render

from .models import Day
from .forms import DayForm


def index(request):
    day_list = Day.objects.order_by('-day')[:10]
    context = {'day_list': day_list}
    return render(request, 'dailymeeting/index.html', context)


class DayCreateView(CreateView):
    model = Day
    form_class = DayForm
    template_name = "dailymeeting/day_create_form.html"
    success_url = "/dailymeeting/"  # 成功時にリダイレクトするURL
