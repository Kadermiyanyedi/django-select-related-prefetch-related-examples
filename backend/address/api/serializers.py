from rest_framework import serializers

from address.models import Country


class CountryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "code", "name")
