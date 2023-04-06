from django.shortcuts import render, redirect


def project_list(request):
    return render(request, "project_list.html")