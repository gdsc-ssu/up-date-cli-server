import json

from user import get_user
from response import get_error_schema


def lambda_handler(event, context):
    route_key = event['requestContext']['routeKey'].split()
    method, path = route_key[0], route_key[1]
    path_parameters = event['pathParameters']

    results = route(method, path, path_parameters)

    return json.dumps(results)


# request body도 대응해야 함
def route(method, path, path_parameters):
    if method == 'GET' and path == '/user/{id}':
        return get_user(path_parameters)
    else:
        return get_error_schema(500, '라우팅 정보를 찾지 못했습니다.')
