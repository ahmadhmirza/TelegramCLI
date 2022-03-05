async def send_message(t_client, recipient):
    await t_client.send_message(recipient, "Test Message")
    print("message sent successfully.")


async def get_user(t_client, user_name):
    print(f"Getting user {user_name}")
    user = await t_client.get_entity(user_name)
    return user


def get_messages(t_client, user_name):
    for message in t_client.iter_messages(user_name):
        print(message.sender_id, ':', message.text)


async def get_all_chats_count(t_client):
    count = 0
    async for dialog in t_client.iter_dialogs():
        count = count + 1
    print(f"Total chats: {count}")
