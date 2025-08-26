"""
Concurrence:
Concurrency is the ability of a program to make progress on multiple tasks at the same time 
(or appear to do so), even if it has a single CPU core.
✅ Concurrency is a good thing — it helps performance, responsiveness, and efficiency.

Race condition:
Where multiple tasks/threads access to one shared resource at the same time.
The final outcome would depends on timing and order
❌ Race condition is a bad side effect of poorly handled concurrency.

Deadlock:
When two or more threads are waiting on each other to release resources, causing a permanent block
"""


def test_same_payload_concurrence():
    import time
    import threading
    from datetime import datetime

    print()
    thread_count = 2
    lock = threading.Lock()
    start_gate = threading.Event()
    shared = {"amount": 100}

    def worker(i, offset):
        # Read is outside the lock, so race condition here. To prevent it, move below line to lock section.
        amount = shared["amount"]

        print(f"{datetime.now()} Thread {i} waited, {shared["amount"]}")
        start_gate.wait()
        print(f"{datetime.now()} Thread {i} started, {shared["amount"]}")
        with lock:
            shared["amount"] = amount + offset
        print(
            f"{datetime.now()} Thread {i} proceeded offset {offset}, final {shared["amount"] }"
        )

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

    print(f"{datetime.now()} Final shared amount {shared["amount"]}")