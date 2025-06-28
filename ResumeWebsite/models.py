from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    github_link = models.URLField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True) 

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}" # This will return a string representation of the message with the sender's name and timestamp
    
class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='briefcase') # FontAwesome icon class for the experience
    order = models.PositiveIntegerField(default=0) # To control the order of experiences in the frontend

    class Meta: # Meta class is used to define metadata for the model
        ordering = ['order'] # This will order the experiences by the 'order' field in ascending order

    def __str__(self):
        return f"{self.role} at {self.company} ({self.duration})"
    

