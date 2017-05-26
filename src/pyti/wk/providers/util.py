def get_cls(cls):
    components = cls.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def create_provider():
    import conf.settings as cs
    cls = get_cls(cs.PROVIDER['class'])
    args = cs.PROVIDER['args']
    return cls(**args)
