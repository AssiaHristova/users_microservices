import json
import os
import httpx


TRANSACTION_INFO_HOST_URL = 'http://localhost:8000/info/generate/id'
url = os.environ.get('TRANSACTION_INFO_HOST_URL') or TRANSACTION_INFO_HOST_URL


def get_transaction_info():
    max_count = 0
    try:
        response = httpx.get(url)
        if response.status_code == 200:
            max_count = 0
            return json.loads(response.text)
        if max_count < 10:
            max_count += 1
            return retry()
        return Exception
    except Exception:
        if max_count < 10:
            max_count += 1
            return retry()
        return Exception


def retry():
    return get_transaction_info()


def parse_transaction_info():
    transaction_info = get_transaction_info()
    id = transaction_info["id"]
    date_of_execution = transaction_info["dateOfExecution"]
    return [id, date_of_execution]
