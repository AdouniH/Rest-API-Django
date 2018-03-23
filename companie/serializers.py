from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSerializer
        fields = ('ticker','volume')
        fields = '__all__'
