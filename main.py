import hikari
import json
from tanjun import *

def run() -> None:
    GatewayBot = hikari.GatewayBot(token="OTE2MDMxMzQxMDI2NTA4ODIw.YakOqg.ZZo11wLOvkL0LmGxwLObKrXWADU")
    (
        Client.from_gateway_bot(GatewayBot)
        .add_prefix('p!')
    )

    GatewayBot.run()


if __name__ == "__main__":
    run()
