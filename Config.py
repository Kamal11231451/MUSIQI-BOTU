import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "3218473"))
    API_HASH = os.environ.get("API_HASH", "8395cd90c60ba9626630ee21023068ca")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5946828530:AAGOFeljhUVBUwtQej6A8FXGLGfk1ARro5w")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu4xEKwQrgx5WNYv28NdoOoSbqEnZFRn06zEFtimhTikfAmXLSu0rB8ZoSIv_IDSX-VFeRY0efGtnLc0L0U5BkuxrG803xNAExoex54tN0Gzg_MZxJxwhvbBkAnlZrEYFtQolFM8cvIbEYhMCPmM8YW9xvce1tS48TBzDAB5UOuocuHPRL4a5E17QniESbnjfZoiTwiBuoivq8FgCOlcX4fj1klqeF5ZbuHBfy5p4L4F_GRFucw2keDaRsTotOacguyCWAVzJ3-pMUsTOknbofFxwjvkxvCc3L1iUov31H-Ffx-Go_LWBKmbUtkW9JJs5sdsZ2jxRNqiXaTHrpjF_d-0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Duo1_robot")
    SUPPORT = os.environ.get("SUPPORT", "GROOTSERVICEMUSIC") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "GROOTSERVICEMUSIC") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/7af0ede8d54ad0b4610fd.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/e15386aa5dd916356c806.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5548218202")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
