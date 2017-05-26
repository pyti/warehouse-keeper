def get_cls(package):
    components = package.split('.')
    imp = __import__(components[0])
    for comp in components[1:]:
        imp = getattr(imp, comp)
    return imp


def create_provider():
    import conf.settings as settings

    cls_name = settings.DATA_PROVIDER.get('class')
    if not cls_name:
        raise ValueError('Data provider class not defined')

    cls = get_cls(cls_name)
    args = settings.DATA_PROVIDER.get('args')
    if args:
        return cls(**args)
    return cls()
