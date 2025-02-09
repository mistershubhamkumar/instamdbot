import instagrapi
import os
import importlib
from config import SESSION_ID, BOT_OWNER, COMMAND_PREFIX

# इंस्टाग्राम लॉगिन
bot = instagrapi.Client()
bot.login_by_sessionid(SESSION_ID)

# सभी फीचर लोड करने का फंक्शन
plugins = {}

def load_plugins():
    global plugins
    plugins = {}
    for file in os.listdir("plugins"):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            plugins[module_name] = importlib.import_module(f"plugins.{module_name}")

load_plugins()

# मेसेज प्रोसेसिंग फंक्शन
def process_command(message):
    if not message.text.startswith(COMMAND_PREFIX):
        return
    
    command_parts = message.text[len(COMMAND_PREFIX):].split(" ", 1)
    command = command_parts[0]
    args = command_parts[1] if len(command_parts) > 1 else ""

    if command in plugins:
        response = plugins[command].run(bot, message, args)
        if response:
            bot.direct_send(response, [message.user_id])

# डीएम मैसेज हैंडलर
@bot.event
def on_message(message):
    process_command(message)

print("🤖 बॉट शुरू हो चुका है!")
bot.run()
