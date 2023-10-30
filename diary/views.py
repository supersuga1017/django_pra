from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import  messages
from .forms import InquiryForm
from .forms import DiaryCreateForm
from .forms import SugaForm
from .models import Diary

import logging

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

# class InquiryView((generic.TemplateView):):
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('inquiry sent by {}'.format(form.cleaned_data['name']) )
        messages.success(self.request,'お問い合わせが完了しました。')
        return super().form_valid(form)

class SugaInquiryView(generic.FormView):
    template_name = "suga_inquiry.html"
    form_class = SugaForm
    success_url = reverse_lazy('diary:sugainquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('inquiry sent by {}'.format(form.cleaned_data['name']) )
        messages.success(self.request,'お問い合わせが完了しました。')
        return super().form_valid(form)


class SugaView(generic.TemplateView):
    template_name = "suga.html"

class DiaryListView(generic.ListView):
    model = Diary
    template_name = "diary_list.html"
    paginnate_by = 2

    def get_queryset(self):
        # diaries = Diary.objects.filter(user = self.request.user).order_by('created_at')
        diaries = Diary.objects.order_by('created_at')
        return diaries

class DiaryDetailView(generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'
    pk_url_kwarg = 'id'

class DiaryCreateView(generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary-list')



