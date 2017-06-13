from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<user_id>\d+)$', views.view, name="view"),
    url(r'^(?P<friend_id>\d+)/add$', views.add, name="add"),
    url(r'^(?P<friendship_id>\d+)/delete$', views.delete, name="delete"),
]
