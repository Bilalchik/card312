from rest_framework import serializers as s

from .models import Service_category


class RecursiveSerializer(s.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class Service_categorySerializer(s.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Service_category
        fields = ['id', 'name', 'icon', 'image', 'children']
        
        
        
        