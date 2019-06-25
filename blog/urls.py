from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from .views import ArticleList, ArticleManageView, ArticleSearch

urlpatterns = [
        url('articles/search/',ArticleSearch.as_view()),
        url('articles/', ArticleList.as_view()),
        url('article/', ArticleManageView.as_view()),
        url(r'^login/', obtain_jwt_token),  
]

urlpatterns = format_suffix_patterns(urlpatterns)