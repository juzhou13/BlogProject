from django.shortcuts import render, HttpResponse
from Crawler.models import People, Article
from django.template import Context, Template


# Create your views here.

def show_index(request):
    person = People(name="Jay", job="officer", password="Password123!")
    html_string = '''
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
            <meta name="description" content="" />
            <meta name="author" content="" />
            <!--[if IE]>
                <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
                <![endif]-->
            <title>Bootstrap Free Blog Template</title>
            <!-- BOOTSTRAP CORE STYLE CSS -->
            <link href="assets/css/bootstrap.css" rel="stylesheet" />
            <!-- FONTAWESOME STYLE CSS -->
            <link href="assets/css/font-awesome.css" rel="stylesheet" />
            <!-- CUSTOM STYLE CSS -->
            <link href="assets/css/style.css" rel="stylesheet" />
        </head>
        <body>
            Hello, {{ person.name }} 
        </body>
    </html>
    '''
    t = Template(html_string)
    c = Context({'person': person})

    web_page = t.render(c)
    return HttpResponse(web_page)


def index(request):
    article_list = Article.objects.all()
    users = People.objects.all()
    context = {"article_list": article_list,
               "user": users[0]
               }
    index_page = render(request, 'index.html', context=context)

    return index_page
