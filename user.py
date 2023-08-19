import pymysql
import dbinfo

from response import get_success_schema, get_error_schema

connection = pymysql.connect(
    host=dbinfo.db_host,
    user=dbinfo.db_username,
    passwd=dbinfo.db_password,
    db=dbinfo.db_name,
    port=dbinfo.db_port
)

cursor = connection.cursor()  # DB에 접속 및 DB 객체를 가져옴


def get_user(path_parameters):
    query = f"""
select
    u.id,
    u.email
from
    users u
where
    u.id = '{path_parameters['id']}';
    """

    cursor.execute(query)
    rows = list(cursor.fetchall())

    if len(rows) == 0:
        return get_error_schema(404, '존재하지 않는 유저입니다.')
    else:
        user = rows[0]
        result = {
            'id': user[0],
            'email': user[1]
        }

        return get_success_schema(200, result)