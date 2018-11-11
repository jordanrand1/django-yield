from django.shortcuts import render

def userdash(request):
    return render(request, "userdash.html", {})
