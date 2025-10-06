import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "7716690774", "6511631892").split()))

API_ID = int(os.getenv("API_ID", "27095838"))

API_HASH = os.getenv("API_HASH", "28c51c248482f0ca68d091397e2e491b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8367633363:AAES46kXP707cECaTNJjWC3pAgoHsoWvjf8")

OWNER_ID = int(os.getenv("OWNER_ID", "7716690774", "6511631892"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "ybwGCgqJngeYGQLiWAjxrYoz")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ZeroneOffcial:ZeroneOffcial@cluster0.3ypqmpw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = os.getenv("LOGS_MAKER_UBOT", "-1002920999560")

USER_GROUP = os.getenv("USER_GROUP", "@pbrafatharcode444")
