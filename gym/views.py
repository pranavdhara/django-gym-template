from django.shortcuts import render
from . models import Member
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']

        userInfo = Member(first_name=first_name,last_name=last_name,email=email,phone=phone)
        userInfo.save()
        
    return render(request,'gym/index.html')


def about(request):
    return render(request,'gym/about.html')


def classes(request):
    return render(request,'gym/classes.html')


def schedule(request):
    return render(request,'gym/schedule.html')


def contact(request):
    if request.method == 'POST':
        subject = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject='From '+subject,
            from_email= email,
            message=message,
            recipient_list=['pranavdhara6@gmail.com'],
            fail_silently=False
        )
        
    return render(request,'gym/contact.html')