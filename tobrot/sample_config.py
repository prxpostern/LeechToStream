import os

class Config(object):
    # get a token from @BotFather TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    TG_BOT_TOKEN = "2023175667:AAE3kJW4sfeGoymWUjNnZHgm95SVpz7vKNo"
    # The Telegram API things APP_ID = int(os.environ.get("APP_ID", 12345)) API_HASH = os.environ.get("API_HASH") OWNER_ID = int(os.environ.get("OWNER_ID", 12345))
    APP_ID = 7513175
    API_HASH = "c0601a8e7ca81691231fb46767fdc1b7"
    OWNER_ID = 742920327
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in "742920327 -1001485315506".split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl")
    PYTDL_COMMAND = os.environ.get("PYTDL_COMMAND", "pytdl")
    #RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    RCLONE_CONFIG = """
        type = drive
        scope = drive
        root_folder_id = 1OvqOeA4GBmd2siJnlIzdmCJPbukCYiGN
        token = {"access_token":"ya29.a0ARrdaM-IuYfNrLO_a0oi1GX5N1ix9aEQoPswaSNhx5An2X4rclRj8Uyk6IRaZfqj3vbWX7OC4M3cau4i0vFSKo2B4LA19EqFiYzD1CGekDvDcO56P5M4L0CFvrgukHwFf0mmcMFxfm7ohzuCy2KEmmjli3BWJw","token_type":"Bearer","refresh_token":"1//03V7lSoUrYfg6CgYIARAAGAMSNwF-L9Irk7Bfgg8iu7FsZcslReVluucV900vbgFyL8iT8Q0qqC3gtbncafBB2ZSoYfjxyTD6hD8","expiry":"2021-11-01T08:48:39.884954738Z"}
        team_drive = 0AHULFtC6nOrpUk9PVA
    """    
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    #INDEX_LINK = os.environ.get("INDEX_LINK", "")
    INDEX_LINK = "https://pdrive.fr-postern-001.workers.dev"
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail")
    CLEAR_UNDELETED = os.environ.get("CLEAR_UNDELETED", "clearall")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "getlog") 
