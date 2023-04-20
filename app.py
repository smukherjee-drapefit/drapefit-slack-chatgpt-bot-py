import os
import re
from revChatGPT.V3 import Chatbot
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = App(token=SLACK_BOT_TOKEN)
client = WebClient(token=SLACK_BOT_TOKEN)

ChatGPTConfig = {
  "api_key": OPENAI_API_KEY
}
# GPT_ENGINE: `gpt-3.5-turbo`
if os.getenv("OPENAI_ENGINE"):
  ChatGPTConfig["engine"] = os.getenv("OPENAI_ENGINE")

chatbot = Chatbot(**ChatGPTConfig)

@app.event("app_mention")
def handle_message_events(body, logger):
  # Log message
  print(str(body["event"]["text"]).split(">")[1])

  client.chat_postMessage(
    channel=body["event"]["channel"],
    thread_ts=body["event"]["event_ts"],
    text=f":sunglasses: Hello from Drape Fit ChatGPT Bot!\nThanks for request. I'm on it. :hourglass:\n"
  )
  # Create prompt for ChatGPT
  prompt = re.sub('\\s<@[^, ]*|^<@[^, ]*', '', body["event"]["text"])
  try:
    response = chatbot.ask(prompt)
  except Exception as e:
    print(e)
    response = f":hot_face: We're experiencing exceptionally high demand. Please try again.\n"
  
  # Reply to thread
  client.chat_postMessage(
    channel=body["event"]["channel"],
    thread_ts=body["event"]["event_ts"],
    text=f":computer: Here you go:\n\n{response}"
  )

if __name__ == "__main__":
  SocketModeHandler(app, SLACK_APP_TOKEN).start()
