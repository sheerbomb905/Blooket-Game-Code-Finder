# ha I made this myself soo gudafdafdafsd
from discord_webhook import DiscordWebhook

import random
import requests
import threading

thread_amount = 25
frames = ['|','\\','—', '/']
lastFrame = 0
def main(lastFrame, frames):
    while 1:
        for _ in range(10000):
            #print ("\033[A                             \033[A")
            #print(frames[lastFrame])
            #lastFrame += 1
            #if lastFrame == 4:
            #    lastFrame = 0
            random_numbers = str(random.randint(100000, 999999))
            try:
                response = requests.get(
                    f"https://fb.blooket.com/c/firebase/id?id={random_numbers}")
                data = response.json()
            except Exception as e:
                print('Something went wrong: '+e)
            #print(data)
            if data["success"] == True:
                print('Valid Game Pin: ' + random_numbers)
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/975473376552452226/Pz9eOV76NGkO9fmD0cJfF_2BWPx8cMcX5BkbE4qJs-qpc9Gcmjxr5jm1tCjUNbtlFFxp', rate_limit_retry=True,
                         content='Valid Game Pin: ' + random_numbers)
                webhook.execute()
            else:
                pass
                #print('Invalid Game Pin: ' + random_numbers)


if __name__ == "__main__":
    threads = list()

    for index in range(thread_amount):
        _ = threading.Thread(target=main, args=(lastFrame, frames))

        threads.append(_)

        _.start()

    for index, thread in enumerate(threads):
        thread.join()