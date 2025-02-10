def run(bot, message, args):
    blocked_users = bot.blocked_users()
    return "\n".join(blocked_users) if blocked_users else "❌ No blocked users."
