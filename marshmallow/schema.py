from marshmallow.base import SchemaABC

class BaseSchema(SchemaABC):
    # Existing methods and properties

    def __apply_nested_option(self, field, attribute, value):
        try:
            if isinstance(field, Nested):
                existing_value = getattr(field, attribute, set())
                if existing_value:
                    if attribute == 'only':
                        value &= set(existing_value)
                    elif attribute == 'exclude':
                        value |= set(existing_value)
                setattr(field, attribute, value)
            elif isinstance(field, List) and isinstance(field.container, Nested):
                existing_value = getattr(field.container, attribute, set())
                if existing_value:
                    if attribute == 'only':
                        value &= set(existing_value)
                    elif attribute == 'exclude':
                        value |= set(existing_value)
                setattr(field.container, attribute, value)
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise e