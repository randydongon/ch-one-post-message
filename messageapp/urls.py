from django.urls import path
from . import views

app_name = 'messageapp'
urlpatterns = [
    # path('', views.message_post, name='message_post'),
    path('', views.MessageListView.as_view(), name='message_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.detail_post, name='detail_post'),

]
