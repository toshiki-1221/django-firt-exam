from django.http import HttpResponse


def add(request, num1, num2):
    add = num1 + num2
    return HttpResponse(f"<h1>{add}</h1>")


def minus(request, num1, num2):
    minus = float(num1) - float(num2)
    return HttpResponse(f"<h1>{minus}</h1>")


def dev(request, num1, num2):
    dev = round(float(num1) / float(num2))
    return HttpResponse(f"<h1>{dev}</h1>")
