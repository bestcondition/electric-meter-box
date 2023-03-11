from os import environ


class EnvConfigBase:
    """env var priority"""
    _CONFIG_SUFFIX = ''

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattribute__(self, item: str):
        def _get_real_attr(_key):
            return object.__getattribute__(self, _key)

        __dict__ = _get_real_attr('__dict__')
        if item in __dict__:
            return __dict__[item]

        _CONFIG_SUFFIX = _get_real_attr('_CONFIG_SUFFIX')
        key_list = [
            _CONFIG_SUFFIX + item,
            _CONFIG_SUFFIX.upper() + item.upper(),
            _CONFIG_SUFFIX.upper() + item.lower(),
            _CONFIG_SUFFIX.lower() + item.upper(),
            _CONFIG_SUFFIX.lower() + item.lower(),
        ]
        key_set = set(key_list)
        value = None
        __annotations__ = _get_real_attr('__annotations__')
        for key in key_set:
            value = environ.get(key)
            if value is not None:
                _expected_type = __annotations__.get(item, str)
                value = _expected_type(value)
                break
        if value is None:
            value = _get_real_attr(item)
        __dict__[item] = value
        return value
