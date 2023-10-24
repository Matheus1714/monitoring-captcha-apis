from src.utils.model.ResponseDTOModel import ResponseDTOModel

def test_default_constructor():
    response = ResponseDTOModel()
    assert response.error == 0
    assert response.status == 200
    assert response.message == ''
    assert response.get_response() == {'error': 0, 'status': 200, 'message': ''}

def test_custom_constructor():
    response = ResponseDTOModel(error=404, status=500, message='Not Found')
    assert response.error == 404
    assert response.status == 500
    assert response.message == 'Not Found'
    assert response.get_response() == {'error': 404, 'status': 500, 'message': 'Not Found'}

def test_get_response_method():
    response = ResponseDTOModel(error=403, status=401, message='Unauthorized')
    response_data = response.get_response()
    assert response_data == {'error': 403, 'status': 401, 'message': 'Unauthorized'}