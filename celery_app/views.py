from django.shortcuts import render, HttpResponse
from .task import test_func


def test(request):
    test_func.delay()
    return HttpResponse("Done")