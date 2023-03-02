def fail(error):
    response = {
        'status': False,
        'message': 'fail',
        'error': error
    }
    return response


def success(data):
    response = {
        'status': True,
        'message': 'success',
        'data': data
    }
    return response