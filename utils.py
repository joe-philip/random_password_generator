from flask import jsonify


def fail(error, status: int = 400):
    response = jsonify(
        {
            'status': False,
            'message': 'fail',
            'error': error
        }
    )
    response.status_code = status
    return response


def success(data, status: int = 200):
    response = jsonify(
        {
            'status': True,
            'message': 'success',
            'data': data
        }
    )
    response.status_code = status
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
