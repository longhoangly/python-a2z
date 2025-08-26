"""
✅ Idempotence Tests

Same Payload + Same Key
→ Expect same result every time, only one operation performed.

Same Payload + Different Key
→ Each treated as a new request; expect multiple operations.

Different Payload + Same Key
→ Expect server to reject due to key conflict with different data.

Concurrent Requests with Same Key
→ Expect no race conditions, single operation handled correctly.

Failure + Retry with Same Key
→ Expect server to return previously completed result.
"""

import requests


def test_same_key_same_payload():
    respone1 = requests.post(url="", headers="", json={})
    respone2 = requests.post(url="", headers="", json={})
    assert respone1.json()["status"] == 200
    assert respone2.json()["status"] == 200
    assert respone1.json() == respone2.json()


def test_same_key_diff_payload():
    respone1 = requests.post(url="", headers="", json={})
    respone2 = requests.post(url="", headers="", json={})
    assert respone1.json()["status"] == 200
    assert respone2.json()["status"] != 200
    assert respone1.json() != respone2.json()


def test_diff_key_same_payload():
    respone1 = requests.post(url="", headers="", json={})
    respone2 = requests.post(url="", headers="", json={})
    assert respone1.json()["status"] == 200
    assert respone2.json()["status"] == 200
    assert respone1.json() != respone2.json()


def test_same_payload_concurrence():
    import time
    import threading
    from datetime import datetime

    print()
    thread_count = 2
    start_gate = threading.Event()
    responses = []

    def worker(i, offset):
        print(f"{datetime.now()} Thread {i} waited")
        start_gate.wait()
        print(f"{datetime.now()} Thread {i} started")
        response = requests.post(url="", headers="", json={})
        responses.append(response.json())

    threads = [
        threading.Thread(target=worker, args=(i, i * 10))
        for i in range(1, thread_count + 1)
    ]
    for t in threads:
        t.start()

    time.sleep(0.5)
    start_gate.set()

    for t in threads:
        t.join()

    print(f"{datetime.now()} Final responses {responses}")
    for res in responses:
        assert res == responses[0]
