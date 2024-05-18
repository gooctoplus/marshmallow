import datetime as dt
from marshmallow import ValidationError

class Field:
    # Placeholder for existing Field code
    def _bind_to_schema(self, field_name, schema):
        raise NotImplementedError

class DateTime(Field):
    def __init__(self, format=None, **kwargs):
        self.format = format or '%Y-%m-%dT%H:%M:%S'
        super().__init__(**kwargs)

    def _bind_to_schema(self, field_name, schema):
        self.field_name = field_name
        self.parent = schema
        if hasattr(schema, 'opts'):
            self.opts = schema.opts
        else:
            self.opts = None

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.strftime(self.format)

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return dt.datetime.strptime(value, self.format)
        except (ValueError, TypeError) as err:
            raise ValidationError(f"Invalid datetime format: {err}")

class List(Field):
    def __init__(self, inner_field, **kwargs):
        self.inner = inner_field
        super().__init__(**kwargs)

    def _bind_to_schema(self, field_name, schema):
        self.field_name = field_name
        self.parent = schema
        self.inner._bind_to_schema(field_name, self)
        if hasattr(schema, 'opts'):
            self.opts = schema.opts
        else:
            self.opts = None

class Tuple(Field):
    def __init__(self, inner_fields, **kwargs):
        self.inner_fields = inner_fields
        super().__init__(**kwargs)

    def _bind_to_schema(self, field_name, schema):
        self.field_name = field_name
        self.parent = schema
        for inner_field in self.inner_fields:
            inner_field._bind_to_schema(field_name, self)
        if hasattr(schema, 'opts'):
            self.opts = schema.opts
        else:
            self.opts = None