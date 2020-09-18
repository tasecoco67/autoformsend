import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MAIL = os.environ.get("MAIL_ADDRESS")
PSW = os.environ.get("UTOKYO_PSW")
