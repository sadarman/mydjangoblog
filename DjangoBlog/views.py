from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('این صفحه درباره ما ایت . که در حال بروز رسانی است .')
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('این صفحه خانه است که در حال بروز رسانی می باشد ')
    return render(request,'home.html')