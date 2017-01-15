"""
Simple serializer setup for ICML papers.

This is a simple demo based on the tutorial at:
http://www.django-rest-framework.org/api-guide/serializers/#modelserializer
"""
from rest_framework import serializers
from papers.models import Paper, SERVER

db = SERVER['papers']

class PaperSerializer(serializers.Serializer):
    """Basic serializer for papers"""

    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    abstract = serializers.CharField()
    type = serializers.CharField()

    # you can specify validate function for field xyz using validate_xyz
    def validate_type(self, value):
        """Document type must be one of a set list of allowed values."""
        if value not in ['proceedings', 'shortpaper', 'journal']:
            raise serializers.ValidationError("Paper type must be valid")
        else:
            return value

    def create(self, validated_data):
        """Create a paper from scratch"""

        paper = Paper()
        return self.update(paper, validated_data)

    def update(self, paper, validated_data):
        """Merge an existing document with validated data"""

        paper.title = validated_data.get('title')
        paper.abstract = validated_data.get('abstract')
        paper.type = validated_data.get('type')
        paper.store(db)

        return paper
