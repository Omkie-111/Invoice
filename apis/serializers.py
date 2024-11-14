from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description', 'quantity', 'price', 'line_total']
        extra_kwargs = {
            'line_total': {'read_only': True}
        }

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, required=True)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            detail_data['line_total'] = detail_data['quantity'] * detail_data['price']
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        
        # Updating Invoice instance fields
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        # Deleting old details and replace with new ones
        instance.details.all().delete()
        for detail_data in details_data:
            detail_data['line_total'] = detail_data['quantity'] * detail_data['price']
            InvoiceDetail.objects.create(invoice=instance, **detail_data)

        return instance
