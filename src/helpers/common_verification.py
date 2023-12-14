import requests

def verify_status_code(response_data,expected_data):
    assert response_data.status_code == expected_data, "Expected status code"+expected_data


def verify_json_key_not_null(key):
    assert key !=0,"key is not empty"+key
    assert key > 0,"Key is greater than zero"

def verify_response(key):
    assert key is not None

def verify_res_time():
    pass
