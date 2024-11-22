import asyncio

from handle.handle_echo import handle_echo


async def main():
    server = await asyncio.start_server(handle_echo, "192.168.56.102", 8888)

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())