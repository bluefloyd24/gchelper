from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 25048157))
    API_HASH = getenv("API_HASH", "f7af78e020826638ce203742b75acb1b")
    ARQ_API_KEY = "PUYWNL-IEPXJF-YAIIMI-GVJRPO-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "7323855879:AAFJg2DZeBg3hO2zat1YfAU5WFB_-bhDowE")
    OWNER_ID = int(getenv("OWNER_ID", 6037364404))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "usaniih")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "bluetsst")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002370079234"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://satumailseribuakuntele:dimarb24@cluster0.o10mi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
    DB_NAME = getenv("DB_NAME", "Bluetsst")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
