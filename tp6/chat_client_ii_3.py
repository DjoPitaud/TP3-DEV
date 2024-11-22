import asyncio
import aioconsole

async def async_input(queue):
    
    while True:
        user_input = await aioconsole.ainput("Votre message : ")
        await queue.put(user_input)

async def async_receive(reader):
    
    while True:
        data = await reader.read(1024)
        
        print(f"Message du serveur : {data.decode('UTF-8')}")
        

async def handle_user_input(queue, writer):
    
    while True:
        user_input = await queue.get()
        if user_input.lower() == "quit":
            print("Fermeture de la connexion...")
            writer.close()
            await writer.wait_closed()
            break
        writer.write(user_input.encode("UTF-8"))
        await writer.drain()

async def tcp_echo_client():
    
    server_address = '192.168.56.102'
    server_port = 8888

    print(f"Connexion au serveur {server_address}:{server_port}...")
    reader, writer = await asyncio.open_connection(server_address, server_port)

    
    queue = asyncio.Queue()

    
    await asyncio.gather(
        async_input(queue),
        async_receive(reader),
        handle_user_input(queue, writer),
    )



asyncio.run(tcp_echo_client())