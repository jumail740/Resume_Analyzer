from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ResumeAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume=models.FileField(upload_to='resumes/')
    job_description=models.TextField()
    extracted_text=models.TextField(blank=True)
    result=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Analysis{self.id}"