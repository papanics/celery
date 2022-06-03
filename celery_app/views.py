from django.shortcuts import render, HttpResponse
from .task import test_func
from send_mail_app.task import send_mail_func

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("sent")