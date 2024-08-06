from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        try:
            # Email content
            msg = MIMEMultipart()
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = 'mantavyamahajan08@gmail.com'
            msg['Subject'] = "Contact Form Message"
            msg.attach(MIMEText(full_message, 'plain'))

            # SMTP server configuration
            server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_HOST_USER, 'mantavyamahajan08@gmail.com', msg.as_string())
            server.quit()

            # Send thank you email to the user
            thank_you_message = f"Dear {name},\n\nThank you for contacting me. I have received your message and will get back to you shortly.\n\nBest regards,\nMantavya Mahajan"
            
            # Email content for thank you message
            thank_you_msg = MIMEMultipart()
            thank_you_msg['From'] = settings.EMAIL_HOST_USER
            thank_you_msg['To'] = email
            thank_you_msg['Subject'] = "Thank You for Contacting"
            thank_you_msg.attach(MIMEText(thank_you_message, 'plain'))

            # Send thank you email
            server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_HOST_USER, email, thank_you_msg.as_string())
            server.quit()

            return JsonResponse({"message": "Message sent successfully!"})
        except Exception as e:
            return JsonResponse({"message": f"Failed to send message: {e}"})

    return render(request, 'contact.html')

def experience(request):
    return render(request, 'experience.html')
