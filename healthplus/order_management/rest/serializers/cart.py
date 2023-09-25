from rest_framework import serializers
from organization.rest.serializers.user import UserSerializer
from order_management.models import Cart, CartItem
from health_support.models import Medicine, LabTest


class CartManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("uid", "medicine", "labtest", "quantity", "total_price")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["total_price"] = instance.product.price * instance.quantity
        return representation

    def create(self, validated_data):
        medicine_uid = validated_data.get("medicine")
        labtest_uid = validated_data.get("labtest")
        quantity = int(validated_data.get("quantity", 1))

        if quantity < 1:
            quantity = 1

        try:
            medicine = Medicine.objects.get(uid=medicine_uid)
        except Medicine.DoesNotExist:
            raise serializers.ValidationError({"detail": "Medicine not found."})

        try:
            labtest = LabTest.get(uid=labtest_uid)
        except LabTest.DoesNotExist:
            raise serializers.ValidationError({"detail": "LabTest not found."})

        user = self.context["request"].user
        cart, _ = Cart.objects.get_or_create(user=user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, medicine=medicine, labtest=labtest
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return cart_item


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CartItem
        fields = ("uid", "user", "created_at", "updated_at", "total_price")
