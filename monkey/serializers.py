from rest_framework import serializers
from .models import fur

class furSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = fur
        fields = ('imdbID', 'quotes')