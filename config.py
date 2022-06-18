## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgA7jD7ne1ezcqVPn9G7mF1_KV_JXiPXRQlDeZzw6H6M1j1Qyx8O8RwpF-1LKo-q6POEzZJWmPM5J9S0pZWxJG6i8RiAGGn8bwohlusK_sll3TEMO2_nxTbIgh65WdUf51V1SALrTZd5VTHgAFiVBVgC1AyHYbD-HAG7fFDyWqNxM3rQMQJxgVg663K3LWRVA8C31AA78OmzQwynRH5W09rVIH3Gv5aalkmVc_br1tV2Dc0fiCyiO1canLOzsF-Azab7cpgDIjm9YXVWzK3WwgEastEMhAFnhv-1Fy6qZwu-lvDGiPxUmxnbzXd6mxO4bom1GaUQLx7BCJ-LZgfuUzOoAAAAAUlR7vYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5194920434:AAGxHd5BcnUg3YqOiQccjxIVphW64i0WN1g")
BOT_NAME = getenv("BOT_NAME", "Music")
API_ID = int(getenv("API_ID", "14262335"))
API_HASH = getenv("API_HASH", "c616a7e91bac7ec7bc7db434f1e7fb0c")
OWNER_NAME = getenv("OWNER_NAME", "Dusho")
OWNER_USERNAME = getenv("OWNER_USERNAME", "CC999")
ALIVE_NAME = getenv("ALIVE_NAME", "DUSHO")
BOT_USERNAME = getenv("BOT_USERNAME", "JHHJBOT")
OWNER_ID = getenv("OWNER_ID", "1398221569")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Chelpe")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CC999")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "cKuBa")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
