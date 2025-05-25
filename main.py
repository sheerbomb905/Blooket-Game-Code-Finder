# CONFIG AREA BELOW
useWebhook = True # Use a discord webhook or not, if yes, fill in the line below
webhook = https://discord.com/api/webhooks/1376017751805788240/CyEgC9_DSYexgohuVIe_9MgRi61iL8QMq-eGjFU18EWYpeazPHZBDd0Ro5_VaDHLtF1G
thread_amount = 8 # How many threads to use? Put it below 10 if using on your home computer. 25 max (also fastest)
logInvalids = False # Don't enable unless you want to have your console spammed (does not send to discord)
# Config area end, do not edit below code

from discord_webhook import DiscordWebhook

import random
import requests
import threading


def main():
    while 1:
        for _ in range(10000):
            random_numbers = str(random.randint(100000, 999999))
            try:
                response = requests.get(
                    f"https://fb.blooket.com/c/firebase/id?id={random_numbers}")
                data = response.json()
            except Exception as e:
                print('Something went wrong: '+e)
            if data["success"]:
                print('Valid Game Pin: ' + random_numbers)
                if useWebhook:
                    webhook = DiscordWebhook(url=webhook, rate_limit_retry=True,
                             content='Valid Game Pin: ' + random_numbers)
                    webhook.execute()
            else:
                if logInvalids:
                    print('Invalid Game Pin: ' + random_numbers)


if __name__ == "__main__":
    threads = list()

    for index in range(thread_amount):
        _ = threading.Thread(target=main)

        threads.append(_)

        _.start()

    for index, thread in enumerate(threads):
        thread.join()
