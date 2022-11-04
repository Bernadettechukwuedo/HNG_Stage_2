from django.shortcuts import render
from .serializers import OperandSerializer, ComplexCaseSeializer
from rest_framework.response import Response
import json
from rest_framework import generics
from .key import get_openai

# Create your views here.


class ArithmeticCreateAPIView(generics.CreateAPIView):

    serializer_class = OperandSerializer

    def post(self, request):
        complex_serializer = ComplexCaseSeializer(data=request.data)
        if complex_serializer.is_valid():
            operation_type = complex_serializer.validated_data.get(
                'operation_type')
            if operation_type != "addition" and operation_type != "subtraction" and operation_type != "multiplication":
                try:
                    result = get_openai(operation_type)
                    result = [int(s) for s in result.split() if s.isdigit()]
                    result = result[len(result) - 1]
                    response = {"operation_type": operation_type,
                                "result": result, "slackUsername": "Berny"}
                    return Response(response)
                except IndexError:
                    print("oopsss you made an invalide entry")

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        operation_type = serializer.validated_data.get('operation_type')
        x = serializer.validated_data.get('x')
        y = serializer.validated_data.get('y')

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


# 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
