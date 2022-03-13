from rest_framework import serializers
from .models import CoachType, Train, Coach


class CoachTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachType
        fields = ('id', 'name', 'price', 'seats', 'is_active')
    
    def create(self, validated_data):
        if 'name' not in validated_data:
            raise serializers.ValidationError('name is required')
        if 'price' not in validated_data:
            raise serializers.ValidationError('price is required')
        if 'seats' not in validated_data:
            raise serializers.ValidationError('seats is required')
        return CoachType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.seats = validated_data.get('seats', instance.seats)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ('id', 'name', 'number', 'source', 'destination', 'arrival_time', 'departure_time', 'runs_on_sunday', 'runs_on_monday', 'runs_on_tuesday', 'runs_on_wednesday', 'runs_on_thursday', 'runs_on_friday', 'runs_on_saturday', 'is_active')
    
    def create(self, validated_data):
        if 'name' not in validated_data:
            raise serializers.ValidationError('name is required')
        if 'number' not in validated_data:
            raise serializers.ValidationError('number is required')
        if 'source' not in validated_data:
            raise serializers.ValidationError('source is required')
        if 'destination' not in validated_data:
            raise serializers.ValidationError('destination is required')
        if 'arrival_time' not in validated_data:
            raise serializers.ValidationError('arrival_time is required')
        if 'departure_time' not in validated_data:
            raise serializers.ValidationError('departure_time is required')
        train = Train.objects.create(**validated_data)
        return train

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.source = validated_data.get('source', instance.source)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.arrival_time = validated_data.get('arrival_time', instance.arrival_time)
        instance.departure_time = validated_data.get('departure_time', instance.departure_time)
        instance.runs_on_sunday = validated_data.get('runs_on_sunday', instance.runs_on_sunday)
        instance.runs_on_monday = validated_data.get('runs_on_monday', instance.runs_on_monday)
        instance.runs_on_tuesday = validated_data.get('runs_on_tuesday', instance.runs_on_tuesday)
        instance.runs_on_wednesday = validated_data.get('runs_on_wednesday', instance.runs_on_wednesday)
        instance.runs_on_thursday = validated_data.get('runs_on_thursday', instance.runs_on_thursday)
        instance.runs_on_friday = validated_data.get('runs_on_friday', instance.runs_on_friday)
        instance.runs_on_saturday = validated_data.get('runs_on_saturday', instance.runs_on_saturday)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'train', 'coach_type', 'coach_number', 'seats_available', 'is_active')
    
    def create(self, validated_data):
        if 'train' not in validated_data:
            raise serializers.ValidationError('train is required')
        if 'coach_type' not in validated_data:
            raise serializers.ValidationError('coach_type is required')
        if 'number' not in validated_data:
            raise serializers.ValidationError('number is required')
        if 'is_active' not in validated_data:
            raise serializers.ValidationError('is_active is required')
        coach = Coach.objects.create(**validated_data)
        return coach

    def update(self, instance, validated_data):
        instance.train = validated_data.get('train', instance.train)
        instance.coach_type = validated_data.get('coach_type', instance.coach_type)
        instance.number = validated_data.get('number', instance.number)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance