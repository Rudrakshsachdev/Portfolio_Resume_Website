from django.shortcuts import render
from .models import Project, Experience
from .forms import ContactForm 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactMessageForm

# Create your views here.
def HomePage(request):
    Projects = Project.objects.all() # Fetching out all the projects from the database
    experience = Experience.objects.all() # Fetching out all the experiences from the database
    form = ContactMessageForm() # Initializing the contact form

    # Handling form submission
    if request.method == 'POST': 
        form = ContactMessageForm(request.POST) # Creating a form instance with submitted data
        if form.is_valid():
            form.save() # saving the form data to the database
            # Extracting cleaned data from the form
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Now, sending the email
            send_mail(
                subject = f"Portfolio Contact from {name}", 
                message = message,
                from_email = settings.EMAIL_HOST_USER, # The email address from which the email will be sent
                recipient_list = [email], # The email address to which the email will be sent,
                fail_silently = False,
            )
            # Displaying a success message
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactMessageForm() # Reset the form after successful completion
    
    return render(
        request,  'index.html',
        {
            'Projects': Projects,  # Passing the projects to the template
            'experience': experience,  # Passing the experience to the template
            'form': form,  # Passing the contact form to the template
        }
    )



