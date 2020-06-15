from django.apps import AppConfig
from django.db import connections


class PollsConfig(AppConfig):
    name = 'polls'


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    try:
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    except:
        return ()


def query(cmd, db):
    with connections[db].cursor() as cursor:
        cursor.execute(cmd)
        data = dictfetchall(cursor)
        if len(data) > 0:
            return data
        else:
            return False
