def follow(bot, message, args):
    # Example of following a user
    user_to_follow = args
    bot.user_follow(user_to_follow)
    return f"✅ Followed {user_to_follow}"

def unfollow(bot, message, args):
    # Example of unfollowing a user
    user_to_unfollow = args
    bot.user_unfollow(user_to_unfollow)
    return f"✅ Unfollowed {user_to_unfollow}"

def run(bot, message, args):
    if args == "follow":
        return follow(bot, message, args)
    elif args == "unfollow":
        return unfollow(bot, message, args)
    else:
        return "❌ Invalid command. Use '.follow' or '.unfollow'"
