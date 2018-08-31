# from django.conf.urls import url
#
# from . import views
#
# app_name='api'
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]






# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
#
#
# app_name='api'
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)







# from django.conf.urls import url
#
# from . import views
#
#
# app_name='api'
# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# ]







# from django.conf.urls import url
#
# from . import views
#
#
# app_name='api'
# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# ]







from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from . import views

schema_view = get_schema_view(title='LocalHost API')

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)

app_name='api'
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'', include(router.urls)),   # 添加 router 的 url
]