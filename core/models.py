from django.db import models
from django.contrib.auth.models import AbstractUser

# -------------------------
# Custom User Model
# -------------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"
    


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name 


class Job(models.Model):
    title = models.CharField(max_length=255, db_index=False)  # text search handled separately
    description = models.TextField()
    location = models.CharField(max_length=150, db_index=True)   # index for filtering
    job_type = models.CharField(
        max_length=50,
        choices=(
            ('full-time', 'Full-Time'),
            ('part-time', 'Part-Time'),
            ('contract', 'Contract'),
            ('internship', 'Internship'),
        ),
        db_index=True  # index for filtering
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="jobs")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # index for ordering/recent queries
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['location']),
            models.Index(fields=['job_type']),
            models.Index(fields=['-created_at']),
            # if you later need text search indexing, we'll add a GIN index via a migration
        ]
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('applicant', 'job')  # Prevent duplicate applications

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"

