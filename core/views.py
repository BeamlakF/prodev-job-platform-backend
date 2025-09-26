from rest_framework import viewsets, permissions
from .models import User, Category, Job, Application
from .serializers import UserSerializer, CategorySerializer, JobSerializer, ApplicationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS


# ----------------------------
# Custom Permissions
# ----------------------------
class IsOwnerOrAdmin(permissions.BasePermission):
    """Allow object owners or admins to edit; others read-only."""
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.role == "admin":
            return True
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
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


# ----------------------------
# Application ViewSet
# ----------------------------
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
