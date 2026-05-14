import os
from dotenv import load_dotenv

load_dotenv()

GSC_PROPERTY = os.getenv("GSC_PROPERTY", "https://exampilot.io")
GSC_CREDENTIALS_PATH = os.getenv("GSC_CREDENTIALS_PATH", "")

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "ExamPilot Marketing Monitor v1.0")

TARGET_SUBREDDITS = [
    "alevel",
    "6thForm",
    "CambridgeInternational",
    "Edexcel",
]

BRAND_KEYWORDS = [
    "exampilot",
    "exam pilot",
    "exampilot.io",
]

TOPIC_KEYWORDS = [
    "cambridge 9709",
    "edexcel ial",
    "wma11",
    "wma12",
    "a level maths revision",
    "pure maths revision",
    "spaced repetition maths",
]
