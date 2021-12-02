import hikari
import os
from tanjun import *

def run() -> None:
    GatewayBot = hikari.GatewayBot(token=os.environ.get("token"))
    (
        Client.from_gateway_bot(GatewayBot)
        .add_prefix('p!')
    )

    GatewayBot.run()


if __name__ == "__main__":
    run()
