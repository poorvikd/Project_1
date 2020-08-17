from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from random import choice
import urllib
md= Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request,title,k=1):
    page = util.get_entry(title)
    if page!=None:
        page=md.convert(page)
    if k != 1:
        return title
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
            if len(substr)!=0:
                return render(request, "encyclopedia/index.html", {
                    "entries": substr
                })
            else:
                return render(request, "encyclopedia/search.html", context={
                    "pages": None,
                    "title": "Error!"
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
        return redirect("/wiki/{}".format(title))
    return render(request, "encyclopedia/create_page.html")
def edit(request,parameter):
    t=parameter
    page = util.get_entry(t)
    if request.method == "POST":
        dic = request.POST
        title = dic['ttl']
        content = dic['content']
        util.save_entry(title=title, content=content)
        return redirect("/wiki/{}".format(title))
    return render(request,"encyclopedia/edit_page.html",context={
        "title":t,
        "content":page
    })  
def random(request):
    entries=util.list_entries()
    entry=choice(entries)
    page= util.get_entry(entry)
    if page != None:
        page = md.convert(page)
    return render(request, "encyclopedia/search.html", context={
        "pages": page,
        "title": entry
    })

    
    
