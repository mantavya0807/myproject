from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt


# Create your views here.
def index(request):
  return render(request, 'index.html')

def project(request):
  return render(request, 'project.html')

def education(request):
  return render(request, 'education.html')

@csrf_exempt
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        full_message = f"Message from {name} ({email}):\n\n{message}"
        
        # Send email to the site owner
        send_mail(
            subject="Contact Form Message",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['mantavyamahajan08@gmail.com'],
        )
        
        # Send thank you email to the user
        thank_you_message = f"Dear {name},\n\nThank you for contacting me. I have received your message and will get back to you shortly.\n\nBest regards,\nMantavya Mahajan"
        send_mail(
            subject="Thank You for Contacting",
            message=thank_you_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )
        
        return JsonResponse({"message": "Message sent successfully!"})
    return render(request, 'contact.html')

def experience(request):
  return render(request, 'experience.html')