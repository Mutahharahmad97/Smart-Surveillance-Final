from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail


def SendEmail(request):
    try:
        emailToSend = request.GET.get('message',None)
        send_mail('Alert', emailToSend,
                  'mutahharahmad9@gmail.com', ['django@mailinator.com', ], fail_silently=False)
        return JsonResponse({'status': 'OK'})

    except Exception as e:
        return JsonResponse({'status' : 'Error'})