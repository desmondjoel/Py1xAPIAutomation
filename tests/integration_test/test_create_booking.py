from src.helpers.api_requests_wrapper import post_request,patch_request,put_request
from src.constants.api_constants import url_create_booking,base_url
from src.helpers.utils import common_headers
from src.helpers.payload_manager import create_booking
from src.helpers.common_verification import verify_response,verify_status_code
import requests
import pytest

class TestCreateBooking(object):
    def test_create_booking_tc01(self):
        response=post_request(url=url_create_booking(),auth=None,headers=common_headers(),payload=create_booking(),in_json=False)
        print(response)
        #verify_response(response.json()["bookingid"])
        #verify_status_code(response,200)
        bookingid= response.json()["bookingid"]
        print(bookingid)

    def test_create_booking_tc02(self):
        response = post_request(url=url_create_booking(), auth=None, headers=common_headers(), payload={},
                                in_json=False)

        # verify_response(response.json()["bookingid"])
        verify_status_code(response,500)

