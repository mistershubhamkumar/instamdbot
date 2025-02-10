import instagrapi
import os
import importlib
from config import SESSION_ID, BOT_OWNER, COMMAND_PREFIX

# Instagram login using session ID
bot = instagrapi.Client()
bot.login_by_sessionid(SESSION_ID)

# Load plugins function
plugins = {}

def load_plugins():
    global plugins
    plugins = {}
    for file in os.listdir("plugins"):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            plugins[module_name] = importlib.import_module(f"plugins.{module_name}")

load_plugins()

# Command processing function
def process_command(message):
    if not message.text.startswith(COMMAND_PREFIX):
        return
    
    command_parts = message.text[len(COMMAND_PREFIX):].split(" ", 1)
    command = command_parts[0]
    args = command_parts[1] if len(command_parts) > 1 else ""

    if command == "install":
        response = install_plugin(args)
    elif command == "remove":
        response = remove_plugin(args)
    elif command in plugins:
        response = plugins[command].run(bot, message, args)
    else:
        response = "❌ Unknown command."
    
    if response:
        bot.direct_send(response, [message.user_id])

# DM message handler
@bot.event
def on_message(message):
    process_command(message)

print("🤖 Bot has started!")
bot.run()
