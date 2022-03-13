from rest_framework import serializers
from .models import MyUser, PaymentMethod, PaymentMethodType


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'is_verified')

    def create(self, validated_data):
        if 'username' not in validated_data:
            raise serializers.ValidationError('username is required')
        if 'password' not in validated_data:
            raise serializers.ValidationError('password is required')
        if 'first_name' not in validated_data:
            raise serializers.ValidationError('first_name is required')
        if 'last_name' not in validated_data:
            raise serializers.ValidationError('last_name is required')
        
        validated_data['email'] = validated_data['username']
        username = validated_data['username']
        if MyUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        password = validated_data['password']
        del validated_data['password']
        user = MyUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'phone_number' in validated_data and validated_data['phone_number'] and validated_data['phone_number'] != instance.phone_number:
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.is_phone_verified = False
        if 'password' in validated_data and validated_data['password']:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class PaymentMethodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethodType
        fields = ('id', 'name')
    
    def create(self, validated_data):
        if 'name' not in validated_data:
            raise serializers.ValidationError('name is required')
        name = validated_data['name']
        if PaymentMethodType.objects.filter(name=name).exists():
            raise serializers.ValidationError('Payment method type already exists')
        payment_method_type = PaymentMethodType.objects.create(**validated_data)
        return payment_method_type

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'user', 'payment_method_type', 'is_valid', 'is_active')

    def create(self, validated_data):
        if 'user' not in validated_data:
            raise serializers.ValidationError('user is required')
        if 'payment_method_type' not in validated_data:
            raise serializers.ValidationError('payment_method_type is required')
        user = validated_data['user']
        payment_method_type = validated_data['payment_method_type']
        if PaymentMethod.objects.filter(user=user, payment_method_type=payment_method_type).exists():
            raise serializers.ValidationError('Payment method already exists')
        payment_method = PaymentMethod.objects.create(**validated_data)
        return payment_method

    def update(self, instance, validated_data):
        instance.is_valid = validated_data.get('is_valid', instance.is_valid)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

