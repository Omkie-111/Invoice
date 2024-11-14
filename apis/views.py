from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceAPIView(APIView):

    def post(self, request, *args, **kwargs):
        invoice_number = request.data.get('invoice_number')

        if invoice_number:
            try:
                invoice = Invoice.objects.get(invoice_number=invoice_number)
                
                # Updating the existing invoice
                serializer = InvoiceSerializer(invoice, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Invoice.DoesNotExist as e:
                print(e)

        # Creating a new invoice if invoice_number was not provided or not found
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
