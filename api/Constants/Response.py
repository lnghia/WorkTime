response = {
    'is_success': 0,
    'data': None,
    'errors': None
}


def make_response(is_success=0, data=None, errors=None):
    response['is_success'] = is_success
    response['data'] = data
    response['errors'] = errors
    return response
