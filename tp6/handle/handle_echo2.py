async def handle_echo(reader, writer):
    data = await reader.read(1024)
    response = data.decode("UTF-8")
    addr = writer.get_extra_info('peername')

    print(f"Message received from {addr!r}: {response!r}")

    
    writer.write(f"hello {addr!r}".encode("utf-8"))
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()