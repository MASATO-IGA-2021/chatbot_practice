import requests
import json

def send_message(access_token, user_id, message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    data = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message. Status code:", response.status_code)
        
def getJsonFile():
    file_path = "./JSON/information.json"
    json_file = open(file_path,"r")
    json_load = json.load(json_file)
    return json_load
    
    

if __name__ == "__main__":
    json_load = getJsonFile()
    access_token = json_load["line_information"]["access_token"]
    user_id = json_load["line_information"]["user_id"]
    message = "Hello, this is your LINE chatbot!お試しちゃっとボットです！！！"
    send_message(access_token, user_id, message)
