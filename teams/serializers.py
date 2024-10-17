from rest_framework import serializers 
from .models import TeamModel


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'

    # def validate(self, attrs):  # attribute is in a dictionary format
    #     name = attrs.get("name")

    #     if TeamModel.objects.filter(name=name).exists():
    #         raise serializers.ValidationError("This team already exists.")
    #     return attrs    

    def create(self, validated_data):
        return TeamModel.objects.create(**validated_data)   

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.base = validated_data.get('base', instance.base)
        instance.team_principal = validated_data.get('team_principal', instance.team_principal)
        instance.championship_won = validated_data.get('championship_won', instance.championship_won)
        instance.save()
        return instance