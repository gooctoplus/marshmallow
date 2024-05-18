from marshmallow.fields import Field, Nested

class List(Field):
    def __init__(self, container, **kwargs):
        super().__init__(**kwargs)
        self.container = container

    @property
    def only(self):
        if isinstance(self.container, Nested):
            return getattr(self.container, 'only', None)
        return None

    @only.setter
    def only(self, value):
        if isinstance(self.container, Nested):
            existing_only = getattr(self.container, 'only', set())
            if existing_only:
                value &= set(existing_only)
            self.container.only = value

    @property
    def exclude(self):
        if isinstance(self.container, Nested):
            return getattr(self.container, 'exclude', None)
        return None

    @exclude.setter
    def exclude(self, value):
        if isinstance(self.container, Nested):
            existing_exclude = getattr(self.container, 'exclude', set())
            if existing_exclude:
                value |= set(existing_exclude)
            self.container.exclude = value

    def _serialize(self, value, attr, obj, **kwargs):
        return [self.container._serialize(each, attr, obj, **kwargs) for each in value]

    def _deserialize(self, value, attr, data, **kwargs):
        return [self.container._deserialize(each, attr, data, **kwargs) for each in value]