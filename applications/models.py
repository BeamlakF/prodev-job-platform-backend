from django.db import models
from users.models import User
from jobs.models import Job

class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('applicant', 'job')  # Prevent duplicate applications

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"
