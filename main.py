from datetime import datetime
from telethon import events
import Session_Helper as sh
import Telegram_Client_Helper as tClientHelper
import Yaml_Reader as yr


# get the info for creating the client
api_id, api_hash = yr.get_api_info()
# create the client
client = sh.create_session(api_id, api_hash)


@client.on(events.NewMessage)
async def new_message_event_handler(event):
    try:
        user_details = await client.get_entity(event.message.peer_id.user_id)
        print(f"New message from {user_details.first_name}: {event.message.message}")
    except:
        print("Error getting the user")
        print(event)


@client.on(events.UserUpdate)
async def user_update_event_handler(event):
    print(event)
    print(f"User ID: {event.user_id}, Action: {event.status}")
    print ("---")
    if event.online:
        try:
            user_id = event.user_id
            user_details = await client.get_entity(user_id)
            print(f" {user_details.first_name}, came online at: {datetime.now()}")
        except:
            print (event)
    print("------------------------------------------------------------------------")


class Main:
    def __init__(self, client):
        self.client = client

    def run_routine(self):
        with self.client:
            #self.program_routine()
            self.client.run_until_disconnected()

    def program_routine(self):
        # send message
        #client.loop.run_until_complete(send_message(client, "me"))
        #client.loop.run_until_complete(tClientHelper.send_message(client, "Tahmed28"))
        # get messages from a particular chat
        # tClientHelper.get_messages(self.client, kate["phone_no"])

        # get user info
        user = self.client.loop.run_until_complete(tClientHelper.get_user(self.client, "phone_no"))
        print(f"User {user.first_name} online status: {user.status}")

        self.client.loop.run_until_complete(tClientHelper.get_all_chats_count(self.client))
        # client.loop.run_until_complete(logout(client))


# Main function
if __name__ == '__main__':
    print("---Starting session---")
    telegramClient = Main(client)
    print("---Session running----")
    telegramClient.run_routine()
    print("---Session ended------")
