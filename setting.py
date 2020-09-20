import os
from dotenv import load_dotenv

# .envファイルの内容を読み込みます
load_dotenv()

MAIL = os.environ.get("MAIL_ADDRESS")
PSW = os.environ.get("UTOKYO_PSW")
URL = os.environ.get("URL")
