import json

from user import get_user_by_id, create_user
from response import get_error_schema


def lambda_handler(event, context):
    print(event)
    route_key = event['requestContext']['routeKey'].split()
    method, path = route_key[0], route_key[1]

    path_parameters = event.get('pathParameters')
    if path_parameters is None:
        path_parameters = None

    body = event.get('body')
    if body is None:
        body = None

    results = route(method, path, path_parameters, body)

    return json.dumps(results)


def route(method, path, path_parameters, body):
    if method == 'GET' and path == '/user/{id}':
        return get_user_by_id(path_parameters)
    elif method == 'POST' and path == '/user':
        return create_user(json.loads(body))
    else:
        return get_error_schema(500, '라우팅 정보를 찾지 못했습니다.')
