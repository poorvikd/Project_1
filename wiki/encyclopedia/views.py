from django.shortcuts import render
from . import util
from markdown2 import Markdown
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
