import types
from datetime import datetime
from telethon import events
import Session_Helper as sh
import Telegram_Client_Helper as tClientHelper
from telethon import types
import utils

logger = utils.get_logger("main.py", "INFO")
# get the info for creating the client
api_id, api_hash = utils.get_api_info()
# create the client
client = sh.create_session(api_id, api_hash)


def write_to_file(file_name, msg):
    with open(file_name, "a") as myfile:
        myfile.write(msg)


@client.on(events.NewMessage)
async def new_message_event_handler(event):
    try:
        user_details = await client.get_entity(event.message.peer_id.user_id)
        print(f"New message from {user_details.first_name}: {event.message.message}")
    except Exception as e:
        logger.error("Error getting user info")
        logger.info(event)
        print(event.message.message)


@client.on(events.UserUpdate)
async def user_update_event_handler(event):
    logger.debug(event)
    if event.online:
        try:
            user_details = await client.get_entity(event.user_id)
            print(f" {user_details.first_name}, came online at : {datetime.now()}")
            msg = "{fname}, came online at :  {time}\n".format(fname=user_details.first_name, time=datetime.now())
            write_to_file("status_journal.log", msg)
        except Exception as e:
            logger.error(e)
            print(event)
    elif isinstance(event.status, types.UserStatusOffline):
        try:
            user_details = await client.get_entity(event.user_id)
            print(f" {user_details.first_name}, went offline at: {datetime.now()}")
            msg = "{fname}, went offline at :  {time}\n".format(fname=user_details.first_name, time=datetime.now())
            write_to_file("status_journal.log", msg)
        except Exception as e:
            logger.error(e)
    else:
        "UserUpdate event occurred, see log for more info."


class Main:
    def __init__(self, client):
        self.client = client

    def run_routine(self):
        with self.client:
            # self.program_routine()
            self.client.run_until_disconnected()

    def program_routine(self):
        # send message
        # client.loop.run_until_complete(send_message(client, "me"))
        # client.loop.run_until_complete(tClientHelper.send_message(client, "Tahmed28"))
        # get messages from a particular chat
        # tClientHelper.get_messages(self.client, kate["phone_no"])

        # get user info
        user = self.client.loop.run_until_complete(tClientHelper.get_user(self.client, "phone_no"))
        print(f"User {user.first_name} online status: {user.status}")

        self.client.loop.run_until_complete(tClientHelper.get_all_chats_count(self.client))
        # client.loop.run_until_complete(logout(client))


# Main function
if __name__ == '__main__':
    logger.info("---Starting session---")
    telegramClient = Main(client)
    logger.info("---Session running----")
    telegramClient.run_routine()
    logger.info("---Session ended------")
