def activate_hook(torch):
    import syft as sy
    return sy.TorchHook(torch)


def make_socket_serever(host, hook, id, port):
    from syft.workers.websocket_server import WebsocketServerWorker
    server = WebsocketServerWorker(host=host, hook=hook, id=id, port=port)
    return server


def main():
    import torch
    hook = activate_hook(torch)
    host = "localhost"
    id = 0
    port = 8182
    server = make_socket_serever(host=host, hook=hook, id=id, port=port)
    server.start()
    # server.list_objects()
    # server.objects_count()


if __name__ == "__main__":
    main()
