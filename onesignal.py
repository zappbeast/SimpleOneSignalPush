import requests
import json
from .config import REST_API_KEY, APP_ID

def send_push_notification(player_id, message, additionalData):
    header = {"Content-Type": "application/json; charset=utf-8", "Authorization": "Basic " + REST_API_KEY}
    payload = {"app_id": APP_ID, "include_player_ids": [player_id], "contents": {"en": message}, "data": additionalData}
    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
    print(req.status_code, req.reason)

