from rest_framework import serializers

from namelist.models import DevilName

# Serializers define the API representation.
class DevilNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DevilName
        fields = ['id', 'name', 'creation_date']