from django.shortcuts import render

def sender(request):
    return render(request, 'app_sender/pages/sender.html')