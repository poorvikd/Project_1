from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django.http import HttpResponse
from django import forms
from django.contrib import messages
md= Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request,title):
    page = util.get_entry(title)
    if page!=None:
        page=md.convert(page)
    return render(request,"encyclopedia/search.html",context={
        "pages":page,
        "title":title
    })
def search_bar(request):
    if request.method == "GET":
        query = request.GET.get('q')
        text=util.get_entry(query)
        if text == None:
            substr=[]
            entries=util.list_entries()
            for entry in entries:
                if query.lower() in entry.lower():
                    substr.append(entry)
            return render(request, "encyclopedia/index.html", {
                "entries": substr
            })

        if text!=None:
            text=md.convert(text)
        return render(request,"encyclopedia/search.html",context={
            "pages":text,
            "title": query
    })
    return index(request)
def create(request):
    if request.method == "POST":
        dic=request.POST
        title=dic['ttl']
        entries=[i.lower() for i in util.list_entries()]
        if title.lower() in entries:
            messages.add_message(request, messages.ERROR, "File with same title exists")
            return render(request, "encyclopedia/create_page.html")
        content=dic['content']
        util.save_entry(title=title,content=content)
        return render(request, "encyclopedia/search.html",context={
            "title":title,
            "pages":content
        })
    return render(request, "encyclopedia/create_page.html")
    
    
