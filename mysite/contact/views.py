from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contact.forms import ContactForm

def contact(request):
    global data_request
    data_request = request.POST.get('subject', 'пустая тема сообщения')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #send_mail(cd['subject'],
            # cd['message'],
            # cd.get('email',
            # 'noreply@example.com'),
            # ['siteowner@example.com'])

            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form':form})

def thanks(request):
    return render_to_response('thanks.html', {'request_subj':data_request})