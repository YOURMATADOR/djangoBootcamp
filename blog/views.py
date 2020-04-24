from django.shortcuts import render
from django.views import View

from .models import Article
# Create your views here.

def article(req,*args, **kwargs):
    
    products = Article.objects.all()
    print(products)
    return render(req,"article_details.html",{"products":products})

class ArticleView(View):
    
    template_name="article_details.html"
    def get(self,req,*args, **kwargs):
        products = Article.objects.all()

        return render(req,self.template_name,{"products":products})