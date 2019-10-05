import torch

import syft as sy
from syft.workers import websocket_client as wsc

hook = sy.TorchHook(torch)

data = torch.tensor([[0., 0.], [0., 2.]], requires_grad=True)
# target = torch.tensor([[0.], [0.]], requires_grad=True)

kwargs_websocket = {"hook": hook,
                    "verbose": True,
                    "host": "127.0.0.1"}

mbp = wsc.WebsocketClientWorker(id="mbp",
                                port=8001,
                                **kwargs_websocket)
print(mbp.list_objects_remote())
data.send(mbp)
print(mbp.list_objects_remote())


if __name__ == "__main__":
    pass
