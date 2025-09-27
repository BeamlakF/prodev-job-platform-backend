from rest_framework import viewsets, permissions
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.core.cache import cache

from .models import User, Category, Job, Application
from .serializers import UserSerializer, CategorySerializer, JobSerializer, ApplicationSerializer
from .filters import JobFilter
from rest_framework.permissions import AllowAny
from rest_framework import generics

# ----------------------------
# Custom Permissions
# ----------------------------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class IsOwnerOrAdmin(permissions.BasePermission):
    """Allow object owners or admins to edit; others read-only."""
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.role == "admin":
            return True
        # Support User, Job (posted_by), Application (applicant)
        return obj == request.user or getattr(obj, "posted_by", None) == request.user or getattr(obj, "applicant", None) == request.user

class ReadOnlyOrAdmin(permissions.BasePermission):
    """Allow read-only for users, full access for admins."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.role == "admin"

# ----------------------------
# User ViewSet (Admins only)
# ----------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

# ----------------------------
# Category ViewSet
# ----------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & ReadOnlyOrAdmin]

# ----------------------------
# Job ViewSet
# ----------------------------
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related('category', 'posted_by').all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = JobFilter
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

    def list(self, request, *args, **kwargs):
        # Cache list endpoint per query params for 2 minutes
        cache_key = f"jobs:{request.get_full_path()}"
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)
        resp = super().list(request, *args, **kwargs)
        cache.set(cache_key, resp.data, 120)
        return resp

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

# ----------------------------
# Application ViewSet
# ----------------------------
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.select_related('applicant', 'job').all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
