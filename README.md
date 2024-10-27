# Roblox Friend Checker
Checks to see if the users account is offline, online, or in game

## Config
*userLooker* is the friend of the account we are checking, and *userMain* is the account we are checking

If you want to add multiple, add them into the list respectively and add either true or false into the *value* list

If you want to loop it, simply set *loop* to true, and set *loop_time_mins* to however many minutes between checks

If you want to add a discord webhook, simply add the link into *discord_webhook_link*, and if you want to mention any user, add their user id into *discord_webhook_mention_ids*

## Running
Run *main.vbs*

If you want it to run at startup, simply create a shortcut of *main.vbs* and put it in the folder *Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup*

**To close it you have to go into task manager and close python, still a bit janky rn but imma fix it trust**
