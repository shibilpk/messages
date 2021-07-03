from django.urls import re_path
from rest_framework_simplejwt.views import (TokenRefreshView,)
from . import views

app_name = 'api_v1_texts'

urlpatterns = [

    re_path(r'^tags/$', views.TagList.as_view()),
    re_path(r'^tag/(?P<pk>.*)/$', views.TagDetail.as_view()),

    re_path(r'^text-snippets/$', views.TextSnippetList.as_view()),
    re_path(r'^create-text-snippet/$', views.TextSnippetCreate.as_view()),
    re_path(r'^text-snippet/(?P<pk>.*)/$', views.TextSnippeSnippetDetail.as_view(),name="text_snippet"),
    re_path(r'^update-text-snippet/(?P<pk>.*)/$', views.TextSnippetUpdate.as_view()),

]
