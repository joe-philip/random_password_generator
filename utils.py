from flask import jsonify


def fail(error, status: int = 400):
    response = jsonify(
        {
            'status': False,
            'message': 'fail',
            'error': error
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
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
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = status
    return response
