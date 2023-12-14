import pytest

from src.helpers.api_requests_wrapper import post_request,patch_request,put_request
from src.constants.api_constants import url_create_booking,base_url,url_create_token
from src.helpers.utils import common_headers
from src.helpers.payload_manager import create_booking,create_token
from src.helpers.common_verification import verify_response,verify_status_code

class Testcases(object):
    def test_create_token(self):
        response=post_request(url=url_create_token(),auth=None,headers=common_headers(),payload=create_token(),in_json=False)
        print(response)
        token=response.json()["token"]
        print(token)
        verify_status_code(response,200)
        print(response.json())


    def create_booking(self):
        response = post_request(url=url_create_booking(), auth=None, headers=common_headers(), payload=create_booking(),
                                in_json=False)
        print(response)
        # verify_response(response.json()["bookingid"])
        # verify_status_code(response,200)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        return bookingid

    def update_booking(self):
        token
        response = put_request(url=u(), auth=None, headers=common_headers(), payload=create_booking(),
                                in_json=False)
        print(response)
        # verify_response(response.json()["bookingid"])
        # verify_status_code(response,200)
        bookingid = response.json()["bookingid"]
        print(bookingid)

    def delete_booking(self):
        pass