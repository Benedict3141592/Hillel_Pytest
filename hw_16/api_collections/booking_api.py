from hw_16.utilities.api_utilities.base_api import BaseAPI


class BookingAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__booking_url = env.summary_url

    def get_bookings_ids(self, headers=None):
        response = self.get(f"{self.__booking_url}", headers=headers)
        return response

    def get_booking_by_id(self, booking_id, headers=None):
        response = self.get(f"{self.__booking_url}/{booking_id}", headers=headers)
        return response

    def get_booking_by_invalid_id(self, invalid_id, headers=None):
        response = self.get(f"{self.__booking_url}/{invalid_id}", headers=headers)
        return response

    def create_booking(self, booking, headers=None):
        response = self.post(self.__booking_url, booking.get_dict(), headers=headers)
        return response

    def put_booking(self, body, booking_id, headers=None):
        response = self.put(f"{self.__booking_url}/{booking_id}", body.get_dict(), headers=headers)
        return response

    def patch_booking(self, booking_id, body, headers=None):
        response = self.patch(f"{self.__booking_url}/{booking_id}", body, headers=headers)
        return response

    def delete_booking(self, deleted_id, headers=None):
        response = self.delete(f"{self.__booking_url}/{deleted_id}", headers=headers)
        return response

    def delete_booking_invalid_id(self, invalid_id, headers=None):
        response = self.delete(f"{self.__booking_url}/{invalid_id}", headers=headers)
        return response
