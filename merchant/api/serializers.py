from rest_framework import serializers

from merchant.models import Application, Channel


class ApplicationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    token = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Application.objects.create(**validated_data)
    
    
    class Meta:
        model = Application
        
 
        
class ChannelSerializer(serializers.Serializer):
    token = serializers.CharField()
    website_url = serializers.URLField()
    trendyol_url = serializers.URLField()
    amazon_url = serializers.URLField()
       
    class Meta:
        model = Channel
        
    def validate(self, attrs):
        token = attrs.pop('token')
        try:
            application = Application.objects.get(token=token)
            attrs['application'] = application
        except Application.DoesNotExist:
            raise serializers.ValidationError("Invalid Application Token")
        
        return attrs
    
    def create(self, validated_data):
        return Channel.objects.create(**validated_data)
    