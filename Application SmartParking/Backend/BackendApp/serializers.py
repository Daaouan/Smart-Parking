from rest_framework import serializers
from BackendApp.models import Abonnement, Car, EntryTable, OutTable, TableComplet

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'

class TableCompletSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableComplet
        fields = '__all__'

class EntryTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryTable
        fields = '__all__'

class OutTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutTable
        fields = '__all__'