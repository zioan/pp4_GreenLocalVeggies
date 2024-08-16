from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder


class DecimalEncoder(DjangoJSONEncoder):
    """
    Custom JSON encoder to handle Decimal objects.

    This encoder extends Django's default JSON encoder to support
    serialization of Decimal objects by converting them to floats.
    """

    def default(self, obj):
        """
        Override the default method to handle Decimal objects.

        Args:
            obj (Any): The object to encode. Can be any type that is
                serializable.

        Returns:
            Any: The encoded value. Converts Decimal to float; otherwise,
                calls the superclass method for other types.
        """
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)
