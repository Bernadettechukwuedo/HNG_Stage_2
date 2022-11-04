from django.shortcuts import render
from .serializers import OperandSerializer
from rest_framework.response import Response
import json
from rest_framework import generics
# Create your views here.


class ArithmeticCreateAPIView(generics.CreateAPIView):

    serializer_class = OperandSerializer

    def post(self, request):
        data = request.data
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
        operation_data = serialized_data.data
        operation_type = operation_data.get("operation_type")
        x = operation_data.get("x")
        y = operation_data.get("y")
        print(operation_type, x, y)
        if operation_type == "addition":
            result = x + y
        elif operation_type == "subtraction":
            result = x - y
        elif operation_type == "multiplication":
            result = x * y

        output = {
            "slackUsername": "Berny",
            "result": result,
            "operation_type": operation_type,

        }
        return Response(output)
