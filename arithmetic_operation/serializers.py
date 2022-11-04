from rest_framework import serializers
import openai

operation_choices = (
    ("addition", "addition"),
    ("subtraction", "subtraction"),
    ("multiplication", "multiplication")
)


class OperandSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=operation_choices)
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    # response = openai.Completion.create(
    #     model="text-davinci-002",

    #     prompt=operation_type,
    #     temperature=0.7,
    #     max_tokens=256,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )


class ComplexCaseSeializer(serializers.Serializer):
    operation_type = serializers.CharField(max_length=300)


def create(self, validated_data):

    return validated_data
