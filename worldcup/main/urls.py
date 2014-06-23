from django.conf.urls import patterns, include, url


urlpatterns = patterns('main.views',
    url(r'^$', 'home', name='main_home'),
    url(r'^team/(?P<name>[-\w]+)/$', 'team_detail', name='main_team_detail'),
    url(r'^match/(?P<match_id>\d)/$', 'match_detail', name='main_match_detail'),
    url(r'^match/like/(?P<match_id>\d)/$', 'like_match', name='main_like_match'),
    url(r'^news/(?P<news_id>\d)/$', 'news_detail', name='main_news_detail'),
    url(r'^news/like/(?P<news_id>\d)/$', 'like_news', name='main_like_news'),
    url(r'^news/tag/(?P<tag>[-\w]+)/$', 'news_tag' , name='main_news_tag'),
    url(r'^register/$', 'register', name='main_user_register'),
)