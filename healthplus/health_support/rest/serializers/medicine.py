from rest_framework import serializers
from health_support.models import Medicine, MedicineCategory


class MedicineCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MedicineCategory
        fields = (
            "uid",
            "name",
            "slug",
            "created_at",
            "updated_at",
            "slug",
            "description",
        )


class MedicineSerializer(serializers.ModelSerializer):
    medicine_category = MedicineCategorySerializer()

    class Meta:
        model = Medicine
        fields = (
            "uid",
            "name",
            "slug",
            "created_at",
            "updated_at",
            "price",
            "description",
            "medicine_category",
        )
