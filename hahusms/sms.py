# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
"""
Base classes for SMS handling.
"""
import json
import requests

class Response:
    """Custom Response class for SMS handling."""
    # constructor

    def __init__(self, dict1):
        self.__dict__.update(dict1)


class SMS:
    """Base SMS Class for sending SMS"""
    api_url = "https://sms.hahucloud.com"

    def __init__(self, api_key, device=None, sim=None, priority=None, response_format="json"):
        self.api_key = api_key
        self.params = dict(key=self.api_key)
        self.response_format = response_format
        self.request = requests.Session()
        if device:
            self.device = device
        if sim:
            self.sim = sim
        if priority:
            self.priority = priority

    def send_request(self, url, method, params=None, data=None):
        """Send request to the API

        Args:
            url (str): the url to send the request to
            method (str): the request method
            params (Any, optional): The paramater to send with the request. Defaults to None.
            data (Any, optional): The data to send with the request. Defaults to None.

        Raises:
            ValueError: if the method is invalid
        """

        if params and isinstance(params, dict):
            params.update(self.params)
        elif params and not isinstance(params, dict):
            raise ValueError("params must be a dict")
        else:
            params = self.params

        req_method = getattr(self.request, method)
        if not req_method:
            raise ValueError("Invalid request method!")

        response = req_method(url, params=params, data=data)
        return getattr(response, "json", lambda: response.text)()

    def convert_response(self, response):
        """Convert Response data to a Response object

        Args:
            response (dict): The response data to convert

        Returns:
            Response: The converted response
        """
        if not isinstance(response, dict):
            return response

        return json.loads(json.dumps(response), object_hook=Response)

    def _construct_request(self, *args, **kwargs):
        """Construct the request to send to the API"""
        res = self.send_request(*args, **kwargs)
        if self.response_format == "obj" and isinstance(res, dict):
            return self.convert_response(res)
        return res

    # Address Book
    def create_contact(self, data, params=None, endpoint="api/create/contact", method="post"):
        """Create and save a new contact to your account"""

        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def create_group(self, data, endpoint="api/create/group", method="post"):
        """Create and save a new contact group to your account"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, data=data)

    def delete_contact(self, data=None, params=None, endpoint="api/delete/contact", method="get"):
        """Delete saved contact number from your account"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def delete_group(self, data=None, params=None, endpoint="api/delete/group", method="get"):
        """Delete contact group from your account"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def get_contacts(self, data=None, params=None, endpoint="api/get/contacts", method="get"):
        """Get the list of your saved contacts"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def get_groups(self, data=None, params=None, endpoint="api/get/groups", method="get"):
        """Get the list of your cantact groups"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    # Devices
    def get_device(self, data=None, params=None, endpoint="api/get/device", method="get"):
        """Get details about a registered device on your account"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def get_devices(self, data=None, params=None, endpoint="api/get/devices", method="get"):
        """Get the list of registered devices on your account"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    # Messages
    def get_pending(self, data=None, params=None, endpoint="api/get/pending", method="get"):
        """Get the list of pending messages for sending"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def get_received(self, data=None, params=None, endpoint="api/get/received", method="get"):
        """Get the list of received messages on your account"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def get_sent(self, data=None, params=None, endpoint="api/get/sent", method="get"):
        """Get the list of sent messages on your account"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def send(self, data=None, params=None, endpoint="api/send", method="get"):
        """Send an sms to defined phone recipient"""
        url = f"{self.api_url}/{endpoint}"
        return self._construct_request(url, method, params=params, data=data)

    def send_message(self, to, message, data=None, params=None, endpoint="api/send", method="get"):
        """Send an sms to defined phone recipient"""
        url = f"{self.api_url}/{endpoint}"
        if params:
            params.update({"phone": to, "message": message})
        else:
            params = {"phone": to, "message": message}
        return self._construct_request(url, method, params=params, data=data)