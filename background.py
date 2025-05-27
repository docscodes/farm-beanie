import json
from time import sleep


def delayed_task(username: str) -> None:
    sleep(5)
    print(f"User just logged in: {username}")
