from django.shortcuts import redirect, render
from articles.forms import CreateArticleForm
from articles.models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html',context)

@login_required(login_url='/accounts/login/')
def create(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # returns a new instance of the article (model of the form) 
            # but does not commit the save to the database yet
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:get', article_slug=article.slug)
    else:
        form = CreateArticleForm()
    return render(request, 'articles/create.html', {'form': form})

def get(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    context = {
        'article': article
    }
    return render(request, 'articles/get.html',context)
