from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
<<<<<<< HEAD
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('sugainquiry/',views.SugaInquiryView.as_view(),name="sugainquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary-list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),

=======
    path('inquiry',views.InquiryView.as_view(),name="inquiry"),
    path('diary-list', views.DiaryListView.as_view(), name="diary-list"),
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
    path('suga',views.SugaView.as_view(), name="yuki")

]