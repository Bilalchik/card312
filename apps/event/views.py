from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from apps.event.serializers import EventCreateSerializer, EventListSerializer, EventUpdateSerializer
from apps.event.models import Event, EventImage


class EventCreateView(CreateAPIView):
    serializer_class = EventCreateSerializer
    permission_classes = [IsAuthenticated]


class MyEventListView(ListAPIView):
    serializer_class = EventListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user.id)


class EventUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventUpdateSerializer

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user.id)

    def get_object(self):
        event = super().get_object()
        user = self.request.user

        if event.user != user:
            raise PermissionDenied(
                "Вы не можете изменить этот объект, так как он принадлежит другому пользователю.")
        return event

