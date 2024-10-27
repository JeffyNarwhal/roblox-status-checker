import requests
import json
from discord_webhook import DiscordWebhook
from datetime import datetime
import time

req = requests.Session()

def getuser(userMain):
    userMain = (req.get(
        f'https://users.roblox.com/v1/users/{userMain}').json())["name"]
    return  userMain

def main():
    while True:
        with open("config.json") as f:
            data = json.load(f)

        z = ""
        for i in range(len(data["userLooker"])):
            friends = req.get(
                f'https://friends.roblox.com/v1/users/{data["userLooker"][i]}/friends').json()

            value = 0
            for element in friends["data"]:
                if element["id"] == data["userMain"][i]:
                    try:
                        value = element["presenceType"]
                    except:
                        pass
                    break

            if value != data["value"][i]:
                userMain = getuser(data["userMain"][i])
                x = True
                if value == 0:
                    if len(data["discord_webhook_link"]) > 0:
                        mentions = ""
                        for y in data["discord_webhook_mention_ids"]:
                            mentions += f"<@{y}> "
                        DiscordWebhook(url=data["discord_webhook_link"], content=f"{mentions}\nUser [{userMain}](<https://www.roblox.com/users/{data["userMain"][i]}/profile>) is offline").execute()
                    print(f"User {userMain} is offline")
                    z += f" - User {userMain} is offline"
                elif value == 1:
                    if len(data["discord_webhook_link"]) > 0:
                        mentions = ""
                        for y in data["discord_webhook_mention_ids"]:
                            mentions += f"<@{y}> "
                        DiscordWebhook(url=data["discord_webhook_link"], content=f"{mentions}\nUser [{userMain}](<https://www.roblox.com/users/{data["userMain"][i]}/profile>) is online").execute()
                    print(f"User {userMain} is online")
                    z += f" - User {userMain} is online"
                elif value == 2:
                    if len(data["discord_webhook_link"]) > 0:
                        mentions = ""
                        for y in data["discord_webhook_mention_ids"]:
                            mentions += f"<@{y}> "
                        DiscordWebhook(url=data["discord_webhook_link"], content=f"{mentions}\nUser [{userMain}](<https://www.roblox.com/users/{data["userMain"][i]}/profile>) is in game").execute()
                    print(f"User {userMain} is in game")
                    z += f" - User {userMain} is in game"
                data["value"][i] = value

        try:
            if x:
                with open("config.json", "w") as f:
                    json.dump(data, f, indent=4)
                try:
                    with open("gol.json") as f:
                        log = json.load(f)
                    log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
                    with open("gol.json", "w") as f:
                        json.dump(log, f, indent=4)
                except:
                    log = []
                    log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
                    with open("gol.json", "w") as f:
                        json.dump(log, f, indent=4)
        except:
            pass

        try:
            with open("log.json") as f:
                log = json.load(f)
            log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
            with open("log.json", "w") as f:
                json.dump(log, f, indent=4)
        except:
            log = []
            log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
            with open("log.json", "w") as f:
                json.dump(log, f, indent=4)

        if data["loop"]:
            time.sleep(data["loop_time_mins"] * 60 + data["loop_time_seconds"])
        else:
            break

if __name__ == "__main__":
    main()
