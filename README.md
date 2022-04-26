# API Guide for Hahu Cloud SMS Gateway

This is simple python api for [hahucloud sms](https://sms.hahucloud.com). It is a RESTful API, and you can use it to send SMS messages to your customers. It is a simple and easy to use API.

This is **unofficial API**, and it is **not** supported by **Hahu Clouds**. It is just a guide for you to use Hahu SMS API. If you have any questions, please contact us.

Contact Information:

    - Email: chapimenge3@gmail.com
    - Telegram: @chapimenge
    - Twitter: @chapimenge
    - Linkedin: https://www.linkedin.com/in/chapimenge/

## Installation

hahusms is available on PyPI:

```bash
python -m pip install hahusms
```

Hahusms officially supports Python 3.7 and above.

## User Guide

Simple API Reference:

```python
from hahusms import SMS

sms = SMS(api_key='your_api_key')

response = sms.send_message(to='+86xxxxxxxx', message='Hello world!')
print(response['status'])
print(response['message'])
print(response['data'])

# Or you can use the following to make the response from json to object

sms = SMS(api_key='your_api_key', response_format="obj")
response = sms.send_message(to='+86xxxxxxxx', message='Hello world!')
print(response.status)
print(response.message)
print(response.data.message)
```

## API Reference

The SMS class the base class for all API calls. You can set the following parameters when you initialize the SMS class:

    - api_key: Your API key.
    - response_format: The response format. It can be "json" or "obj".
    - device (optional): The device id to set your own default device.
    - sim (optional): The sim slot to set your own default sim slot.
    - priority (optional): The priority of the message. It can be 0 or 1.

To use the above parameters we can use as below

```python

from hahusms import SMS
sms = SMS(api_key='your_api_key', response_format="json",
          device='your_device_id(int)', sim='your_sim_slot(int)',
          priority=1)

```

You can pass the parameters when you call the API.

```python
sms = SMS(api_key='your_api_key', response_format="obj")
params = {
    "id": 1
}
response = sms.get_device(params=params)
print(response.status)
print(response.message)
print(response.data.name) # The response is object type because we set response_format="obj"
```

you can always override the SMS class and define your own custom methods to call the API.

## Available Methods

**SMS** class have the following methods:

    - create_contact
    - create_group
    - delete_contact
    - delete_group
    - get_contacts
    - get_groups
    - get_device
    - get_devices
    - get_pending
    - get_received
    - get_received
    - send
    - send_message - required parameters: to, message

You can find the official **Postman Collection** for each method in the [API Reference](https://sms.hahucloud.com/HahuCloudSMS.postman_collection.json).
