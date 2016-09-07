from django.conf.urls import include, url
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^app/$', views.base_app_view),

    url(r'^$', views.api_root),
    url(r'^users/$', views.UserListView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
    url(r'^todos/$', views.TodoListView.as_view(), name='todo-list'),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.TodoDetailView.as_view(), name='todo-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
