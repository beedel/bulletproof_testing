import requests
#DO NOT MODIFY


def post(url, json, **kwargs):
    response = requests.Response()
    if "checkExist" in url and "bikernet.com" in url:
        response.status_code = 200
        response._content = bytes("True", "utf-8")
        return response
    elif "getPriceForBike" in "bikernet.com" in url:
        response.status_code = 200
        response._content = bytes("£6000", "utf-8")
        return response
    elif "bikernet.com" in url:
        response.status_code = 405
        response._content = bytes("Method not allowed", "utf-8")
        return response
    else:
        raise ConnectionError("Unable to resolve URL")
