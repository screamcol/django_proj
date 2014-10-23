from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def contact(request):
    errors = []
    global data_request
    data_request = request.POST.get('subject', 'пустая тема сообщения')
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Введите тему.')
        if not request.POST.get('message', ''):
            errors.append('Введите сообщение.')
        if request.POST.get('e-mail') and '@' not in request.POST['e-mail']:
            errors.append('Введите правильный адрес e-mail.')
        if not errors:
            #send_mail(request.POST['subject'], request.POST['message'], request.POST.get('e-mail', 'noreply@example.com'), ['siteowner@example.com'])
            print('We send this email, believe us')
        return HttpResponseRedirect('/contact/thanks')

    return render_to_response('contact_form.html', {'errors':errors})

def thanks(request):
    return render_to_response('thanks.html', {'request_subj':data_request})