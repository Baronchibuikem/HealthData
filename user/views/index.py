from django.shortcuts import render


def dashboard(request):
    template = "index.html"
    return render(request, template)
