import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def education(request):
    return render(request, 'education.html')

@csrf_protect
@require_POST
def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    
    if not name or not email or not message:
        return JsonResponse({"message": "All fields are required."}, status=400)
    
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
        # Log the error (optional)
        # logger.error(f"Failed to send contact form message: {e}")
        return JsonResponse({"message": "Failed to send message. Please try again later."}, status=500)

def contact_view(request):
    if request.method == "POST":
        return contact(request)
    return render(request, 'contact.html')


def experience(request):
    return render(request, 'experience.html')

def projects(request):
    return render(request, 'project.html')