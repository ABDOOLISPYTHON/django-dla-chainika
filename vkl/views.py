from django.shortcuts import render
  
def index(request):
    return render(request, "index.html")
 
def contacts(request):
    return render(request, "contact.html")

def friend(request):
    return render(request, "base.html")

  