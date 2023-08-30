import os

API_BASE = os.environ.get('PRODIGILINK_BASE', "http://localhost:5000")
METRIX_BASE = API_BASE + "/metrix"