def activate_hook(torch):
    import syft as sy
    return sy.TorchHook(torch)


def make_socket_serever(host, hook, id, port, log_msgs=True, verbose=True):
    from syft.workers.websocket_server import WebsocketServerWorker
    server = WebsocketServerWorker(host=host, hook=hook, id=id, port=port,
                                   log_msgs=log_msgs, verbose=verbose)
    return server


# def pickle_socket_server(server, pickle_path="./server.pkl"):
#     import pickle
#     with open(pickle_path, 'wb') as f:
#         pickle.dump(server, f)


def main():
    import torch
    hook = activate_hook(torch)
    host = "localhost"
    id = 0
    port = 8182
    server = make_socket_serever(host=host, hook=hook, id=id, port=port)
    # pickle_socket_server(server)
    server.start()
    # server.list_objects()
    # server.objects_count()


if __name__ == "__main__":
    main()
