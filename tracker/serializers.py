from rest_framework import serializers
from .models import Income, Tax

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['income_id','income_name','time_frame','income_type','income_amount','user_id']

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ['tax_id','name','country','rate','min','max']

