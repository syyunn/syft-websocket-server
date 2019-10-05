import syft as sy
from syft.workers.websocket_server import WebsocketServerWorker
import torch

hook = sy.TorchHook(torch)


kwargs = {
    "id": 'mbp2',
    "host": 'localhost',
    "port": '8002',
    "hook": hook,
    "verbose": True,
}


if __name__ == "__main__":
    server2 = WebsocketServerWorker(**kwargs)
    tensor = torch.tensor([2])
    server2.load_data([tensor])
    print(server2._objects)
    server2.start()
