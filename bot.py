from roblox import Client
import asyncio
import aiohttp

client = Client()

async def search(message):
    input_data = message.strip()
    try:
        if input_data.isdigit():
            user = await client.get_user(int(input_data))
        else:
            user = await client.get_user_by_username(input_data, expand=True)
            
        avatar_api = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user.id}&size=420x420&format=png"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(avatar_api) as resp:
                data = await resp.json()
                avatar_url = data["data"][0]["imageUrl"] if data["data"] else None

        reply = (
            f"ID: {user.id}\n"
            f"Username: {user.name}\n"
            f"Display Name: {user.display_name}\n"
            f"Date creation {user.created.strftime('%m/%d/%Y, %H:%M:%S')}\n"
            f"Description : {user.description}"
        )
        print(reply)
    except Exception as e:
        print("Error: ", e)

async def main():
	while True:
		await search(input("Enter Username or Id: "))
asyncio.run(main())
