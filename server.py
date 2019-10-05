import syft as sy
from syft.workers.websocket_server import WebsocketServerWorker
import torch

hook = sy.TorchHook(torch)


kwargs = {
    "id": 'mbp',
    "host": 'localhost',
    "port": '8001',
    "hook": hook,
    "verbose": True,
}


if __name__ == "__main__":
    server = WebsocketServerWorker(**kwargs)
    tensor = torch.tensor([1])
    server.load_data([tensor])
    print(server._objects)
    server.start()
