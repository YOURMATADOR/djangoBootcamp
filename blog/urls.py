from django.urls import path

from .views import article,ArticleView

app_name="blog"

urlpatterns=[
    path("",article,name="blog"),
    path("class/",ArticleView.as_view(template_name="article_details.html"),name="blog")
]