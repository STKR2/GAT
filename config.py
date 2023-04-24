## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAGFRW8AN9biZhAIB_X7rubbTCwNtc48oa-geXlaVsQbV9M1emAEV_iGPw_W-lNP1HGbOuQgF9NAUIxlp8-6rgN16-7Upuhst2wCxewyx0VP7Cxb5k_9EXap6_xeU2v4So9RZMt95XYxhGc4hWO_ikd9P46iHLMjXW8GjQAnGvY-bIrM6XqIXF1yeC3vixEa8knOHGkedZU3FYyLhEILy8TV6eH5jOGvsyw5o7xFElb2zZId_vlYO--B3xSWIMUR6zyH8wozehe9tIn0jZptYjY1rqWOMoYS9wtqvBThVazL60nrgL-KdikJC9beDJLLR0C-wzuAtARPCZ-JK6oG-gVAAAAAUM3evYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5204315005:AAESU5QWieHCKgbyN29DPhsdiUO_zziupNc")
BOT_NAME = getenv("BOT_NAME", "Music")
API_ID = int(getenv("API_ID", "14262335"))
API_HASH = getenv("API_HASH", "c616a7e91bac7ec7bc7db434f1e7fb0c")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "DUSHO")
BOT_USERNAME = getenv("BOT_USERNAME", "Saiadjabot")
OWNER_ID = getenv("OWNER_ID", "1854384004")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Chelpe")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xl444")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/GAT")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
