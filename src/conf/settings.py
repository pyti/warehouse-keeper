from pyti.wk.providers import DbDataProvider


def create_provider():
    db_conf = {
        'host': '',
        'database': '',
        'user': '',
        'password': ''
    }

    return DbDataProvider(**db_conf)
