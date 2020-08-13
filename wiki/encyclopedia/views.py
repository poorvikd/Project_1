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
