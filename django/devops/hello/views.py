# from django.shortcuts import render
# from django.http import HttpResponse, QueryDict
# #from hello.models import User
#
# # def index(request):
# #     year = request.GET.get("year","2020")
# #     month = request.GET.get("month","03")
# #     return HttpResponse("year is %s.month is %s" (year,month))
# #     #return HttpResponse("<p>Hello World,Hello, Django</p>")
#
# # def index(request,year,month):
# #     return HttpResponse("year is %s.month is %s" (year,month))
# #
# # def index(request, **kwargs):
# #     print(kwargs)
# #     year =kwargs.get('year')
# #     month = kwargs.get('month')
# #     return HttpResponse("year is %s.month is %s" % (year,month))
#
# def index(request):
#     print(request.scheme)
#     print(request.method)
#     print(request.headers)
#     print(request.path)
#     print(request.META)
#     print(request.GET)
#     data = request.GET
#     year = data.get("year", "2019")
#     month = data.get("month", "10")
#     if request.method == "POST":
#         print(request.method)
#         print(request.body)
#         print(QuaryDict(request.body).dict())
#         print(request.POST)
#         data = request.POST
#         year = data.get("year","2018")
#         month = data.get("month","07")
#     return HttpResponse("year is %s,month is %s" % (year,month))
from django.http import HttpResponse
def index(request):
    return HttpResponse("<p>Hello World,Hello, Django</p>")