from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<user_id>\d+)$', views.view, name="view"),
    url(r'^(?P<friend_id>\d+)/add$', views.add, name="add"),
    url(r'^(?P<friendship_id>\d+)/delete$', views.delete, name="delete"),
    url(r'^(?P<friendship_id>\d+)/accept$', views.accept, name="accept"),
    url(r'^(?P<friendship_id>\d+)/decline$', views.decline, name="decline"),
]
