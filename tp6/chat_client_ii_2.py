import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '192.168.56.102', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode("UTF-8"))
    await writer.drain()

    data = await reader.read(1024)
    print(f'Received: {data.decode("UTF-8")!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello'))