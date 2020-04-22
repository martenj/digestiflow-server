"""API Views for the flowcells app."""

from digestiflow.utils import SodarObjectInProjectPermissions, ProjectMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import FileBoxSerializer, FileBoxAuditEntrySerializer
from ..models import FileBox, FileBoxAuditEntry


# TODO: authorization still missing, need mixin for this!


class FileBoxListCreateApiView(ListCreateAPIView, ProjectMixin):
    permission_classes = (SodarObjectInProjectPermissions,)
    serializer_class = FileBoxSerializer

    def get_queryset(self):
        return FileBox.objects.filter(project=self.get_project()).prefetch_related("account_grants")


class FileBoxRetrieveUpdateApiView(RetrieveUpdateAPIView, ProjectMixin):
    permission_classes = (SodarObjectInProjectPermissions,)
    serializer_class = FileBoxSerializer

    lookup_url_kwarg = "filebox"
    lookup_field = "sodar_uuid"

    def get_queryset(self):
        return FileBox.objects.filter(project=self.get_project()).prefetch_related("account_grants")


class FileBoxAuditEntryListCreateApiView(ListCreateAPIView, ProjectMixin):
    permission_classes = (SodarObjectInProjectPermissions,)
    serializer_class = FileBoxAuditEntrySerializer

    def get_serializer_context(self):
        result = super().get_serializer_context()
        result["file_box"] = self.get_filebox()
        return result

    def get_filebox(self):
        return FileBox.objects.get(
            project=self.get_project(), sodar_uuid=self.kwargs.get("filebox")
        )

    def get_queryset(self):
        return FileBoxAuditEntry.objects.filter(file_box=self.get_filebox())
