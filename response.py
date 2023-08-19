def get_success_schema(status_code, body):
    response = {
        "statusCode": status_code,
        "body": body
    }

    return response


def get_error_schema(status_code, reason):
    response = {
        "statusCode": status_code,
        "body": {
            "error": reason

        }
    }

    return response
