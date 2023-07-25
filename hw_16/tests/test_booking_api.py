from http import HTTPStatus
import time

from hw_16.api_collections.data_classes.booking_data import Booking
from hw_16.api_collections.booking_api import BookingAPI


def test_get_bookings_ids(env):
    booking_api = BookingAPI(env)
    response = booking_api.get_bookings_ids()
    assert response.status_code == HTTPStatus.OK, "Status code is not as expected"


def test_response_time(env):
    start_time = time.time()
    BookingAPI(env).get_bookings_ids()
    end_time = time.time()
    max_time = 1
    actual_time = end_time - start_time
    assert actual_time < max_time, "Waiting time exceeded"


def test_get_booking_by_id(env, create_mock_booking):
    booking_api = BookingAPI(env)
    response = booking_api.get_booking_by_id()
    actual_main_page = Booking(**response.json())
    assert create_mock_booking.get_dict() == actual_main_page.get_dict()
    assert response.status_code == HTTPStatus.OK, "Status code is not as expected"


def test_get_booking_via_invalid_id(env):
    booking_api = BookingAPI(env)
    response = booking_api.get_booking_by_invalid_id()
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_create_booking(env, create_mock_booking):
    booking_api = BookingAPI(env)
    response = booking_api.create_booking(create_mock_booking)
    assert response.status_code == HTTPStatus.OK, "Status code is not as expected"


def test_put_booking(env, create_mock_booking):
    booking_api = BookingAPI(env)
    response = booking_api.put_booking(create_mock_booking)
    assert response.status_code == HTTPStatus.OK, "Status code is not as expected"


def test_patch_booking(env):
    booking_api = BookingAPI(env)
    response = booking_api.patch_booking({"firstname": "Leo", "lastname": "Messi"})
    assert response.status_code == HTTPStatus.OK, "Status code is not as expected"


def test_patch_via_invalid_data(env):
    booking_api = BookingAPI(env)
    response = booking_api.patch_booking({"some field": "Abagagalamaga"})
    assert response.status_code == HTTPStatus.BAD_REQUEST, "Status code is not as expected"


def test_delete_booking(env):
    booking_api = BookingAPI(env)
    response = booking_api.delete_booking()
    assert response.status_code == HTTPStatus.CREATED, "Status code is not as expected"


def test_delete_invalid_id(env):
    booking_api = BookingAPI(env)
    response = booking_api.delete_booking_invalid_id()
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, "Status code is not as expected"
