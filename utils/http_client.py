import requests
import allure
import json


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, path, method="GET", headers=None, params=None, json_data=None):
        url = f"{self.base_url}{path}"
        headers = headers or {}

        if json_data != None:
            method = "POST"

        # Log request
        self._log_request(method, url, headers, params, json_data)

        response = requests.request(
            method, url, headers=headers, params=params, json=json_data
        )

        # Log response
        self._log_response(response)

        return response

    def _log_request(self, method, url, headers, params, json_data):
        request_info = f"➡️ REQUEST:\nMETHOD: {method}\nURL: {url}\nHEADERS: {headers}\nPARAMS: {params}\nBODY: {json.dumps(json_data, indent=2)}"
        print(request_info)
        allure.attach(
            request_info,
            name=f"request: {url}",
            attachment_type=allure.attachment_type.TEXT,
        )

    def _log_response(self, response):
        response_info = f"⬅️ RESPONSE:\nSTATUS: {response.status_code}\nHEADERS: {dict(response.headers)}\nBODY: {response.text}"
        print(response_info)
        allure.attach(
            response_info,
            name=f"response",
            attachment_type=allure.attachment_type.TEXT,
        )
