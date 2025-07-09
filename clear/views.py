import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CallbackForm
from .forms import SyllabusRequestForm
from .models import Callback
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from django.core.mail import send_mail

load_dotenv()

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def course(request):
    return render(request, 'course.html')

def careers(request):
    return render(request, 'careers.html')

def aws(request):
    return render(request, 'aws.html')

def python(request):
    return render(request, 'python.html')

def java(request):
    return render(request, 'java.html')

def datascience(request):
    return render(request, 'datascience.html')

def advanceexcel(request):
    return render(request, 'advanceexcel.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CallbackForm
from .models import Callback
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def callbackForm(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            callback = form.save()

            subject_admin = f'New Callback Request from {callback.name}'
            message_body_admin = f'''
You have received a new callback request:

Name: {callback.name}
Email: {callback.email}
Phone Number: {callback.number}
Message: {callback.message}

Submitted at: {callback.submitted_at.strftime('%Y-%m-%d %H:%M:%S')}
            '''

            subject_user = "Thank you for your callback request!"
            message_body_user = f'''
Dear {callback.name},

Thank you for reaching out to us. We have received your callback request and will get back to you shortly.

Here’s a copy of your message:
-------------------------------------------------
Email: {callback.email}
Phone Number: {callback.number}
Message: {callback.message}
-------------------------------------------------

Best regards,
ClearIT Team
            '''

            admin_email = 'varmasagar108@gmail.com'
            user_email = callback.email

            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))  # Store API key in .env securely

                # Send email to Admin
                message_admin = Mail(
                    from_email='varmasagar108@gmail.com',
                    to_emails=admin_email,
                    subject=subject_admin,
                    plain_text_content=message_body_admin
                )
                response_admin = sg.send(message_admin)

                # Send confirmation email to User
                message_user = Mail(
                    from_email='varmasagar108@gmail.com',
                    to_emails=user_email,
                    subject=subject_user,
                    plain_text_content=message_body_user
                )
                response_user = sg.send(message_user)

                if response_admin.status_code == 202 and response_user.status_code == 202:
                    messages.success(request, 'Thank you! Your callback request has been received.')
                else:
                    messages.warning(request, 'Request saved, but some emails failed to send.')

            except Exception as e:
                messages.error(request, f'Request saved, but email failed: {str(e)}')

            return redirect('course')
        else:
            messages.error(request, 'Please correct the form errors.')
    else:
        form = CallbackForm()

    return render(request, 'callback_form.html', {'form': form})


# These views are for the syllabus request form
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SyllabusRequestForm

def syllabusrequest(request):
    if request.method == 'POST':
        form = SyllabusRequestForm(request.POST)
        if form.is_valid():
            data = form.save()

            subject = f"Syllabus Request from {data.name}"
            message = f"""
You have a new syllabus request:

Name: {data.name}
Email: {data.email}
Mobile: {data.mobile}
City: {data.city}
Course: {data.course}
            """

            try:
                print("Sending email...")
                send_mail(
                    subject,
                    message,
                    'clearit712@gmail.com',  # Sender (must be verified in SendGrid)
                    [data.email, 'clearit712@gmail.com'],  # Send to user and admin
                    fail_silently=False,
                )
                print("Email sent successfully")
            except Exception as e:
                print("Email sending failed:", e)

            return render(request, 'course.html', {'form': form, 'success': True})
    else:
        form = SyllabusRequestForm()

    return render(request, 'course.html', {'form': form})




# message = Mail(
#     from_email='from_email@example.com',
#     to_emails='to@example.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     # sg.set_sendgrid_data_residency("eu")
#     # uncomment the above line if you are sending mail using a regional EU subuser
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)