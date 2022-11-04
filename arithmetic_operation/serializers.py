from rest_framework import serializers

operation_choices = (
    ("addition", "addition"),
    ("subtraction", "subtraction"),
    ("multiplication", "multiplication")
)


class OperandSerializer(serializers.Serializer):

    operation_type = serializers.ChoiceField(
        choices=operation_choices)
    x = serializers.IntegerField()
    y = serializers.IntegerField()

    def create(self, validated_data):

        return validated_data
