from rest_framework import serializers

class JobSerializer(serializers.Serializer):
  job_title = serializers.CharField()
  is_popular = serializers.BooleanField()
  