import os
import re
import time
from threading import Thread
from revChatGPT.V3 import Chatbot
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = App(token=SLACK_BOT_TOKEN)

ChatGPTConfig = {
  "api_key": OPENAI_API_KEY
}
# GPT_ENGINE: `gpt-3.5-turbo`
if os.getenv("OPENAI_ENGINE"):
  ChatGPTConfig["engine"] = os.getenv("OPENAI_ENGINE")

chatbot = Chatbot(**ChatGPTConfig)

@app.event("app_mention")
def event_test(event, say):
  prompt = re.sub('\\s<@[^, ]*|^<@[^, ]*', '', event["text"])
  user = event["user"]
  # Log message
  print("app_mention:", f"@{user} {prompt}")

  try:
    response = chatbot.ask(prompt)
    sendmsg = f"<@{user}> {response}"
  except Exception as e:
    print(e)
    sendmsg = f":hot_face: We're experiencing exceptionally high demand. Please try again."

  # Send a reply
  say(sendmsg)

@app.event("message")
def event_test(event, say):
  prompt = re.sub('\\s<@[^, ]*|^<@[^, ]*', '', event["text"])
  if (prompt == event["text"]):
    # Log message
    print("message:", event["text"])

    try:
      response = chatbot.ask(prompt)
      sendmsg = f"{response}"
    except Exception as e:
      print(e)
      sendmsg = f":hot_face: We're experiencing exceptionally high demand. Please try again."

    # Reply message
    say(sendmsg)

def chatgpt_refresh():
  while True:
    time.sleep(60)

if __name__ == "__main__":
  thread = Thread(target=chatgpt_refresh)
  thread.start()
  SocketModeHandler(app, SLACK_APP_TOKEN).start()
