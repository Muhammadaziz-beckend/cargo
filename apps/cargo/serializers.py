from rest_framework import serializers

from .models import Trek


class ListTrekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trek
        fields = (
            "id",
            "number_trek",
            # "description",
            "status",
        )


class RetrieveTrekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trek
        fields = (
            "id",
            "number_trek",
            "description",
            "status",
        )


class CreateTrekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trek
        fields = (
            "number_trek",
            "description",
        )