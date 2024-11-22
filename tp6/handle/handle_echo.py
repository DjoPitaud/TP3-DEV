
async def handle_echo(reader, writer):
    data = await reader.read(1024)
    response = data.decode("UTF-8")
    addr = writer.get_extra_info('peername')

    print(f"Received {response!r} from {addr!r}")

    
    writer.write(f"hello {addr!r}")
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()