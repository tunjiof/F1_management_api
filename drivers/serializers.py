from rest_framework import serializers 
from .models import DriverModel


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = '__all__'

    # def validate(self, attrs):  # attribute is in a dictionary format
    #     name = attrs.get("name")

    #     if TeamModel.objects.filter(name=name).exists():
    #         raise serializers.ValidationError("This team already exists.")
    #     return attrs    

    def create(self, validated_data):
    
        driver = DriverModel(
            name=validated_data['name'],
            nationality=validated_data['nationality'],
            date_of_birth=validated_data['date_of_birth'],
            championship_won=validated_data['championship_won']
        )

        driver.save()
        driver.team.set(validated_data['team'])
        return driver


    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.base = validated_data.get('base', instance.base)
    #     instance.team_principal = validated_data.get('team_principal', instance.team_principal)
    #     instance.championship_won = validated_data.get('championship_won', instance.championship_won)
    #     instance.save()
    #     return instance