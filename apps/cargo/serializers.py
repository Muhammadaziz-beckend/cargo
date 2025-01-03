from rest_framework import serializers

from .models import Trek, Store


class ListTrekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trek
        fields = (
            "id",
            "number_trek",
            # "description",
            "china",
            "store",
            "client",
            "create_dt",
            "update_dt",
        )


class RetrieveTrekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trek
        fields = (
            "id",
            "number_trek",
            "description",
            "china",
            "store",
            "client",
            "create_dt",
            "update_dt",
        )


class CreateTrekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trek
        fields = (
            "number_trek",
            "description",
        )


class UpdateTrekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trek
        fields = (
            "number_trek",
            "description",
            "china",
            "store",
            "client",
        )


class ListStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = (
            "id",
            "name",
        )


class RetrieveStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = (
            "id",
            "name",
        )


class CreateStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ("name",)
