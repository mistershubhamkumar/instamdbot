import os

def remove_plugin(plugin_name):
    try:
        plugin_path = f"plugins/{plugin_name}.py"
        
        if os.path.exists(plugin_path):
            os.remove(plugin_path)
            load_plugins()
            return f"✅ Plugin '{plugin_name}' has been removed successfully."
        else:
            return f"❌ Plugin '{plugin_name}' not found."
    except Exception as e:
        return f"❌ Error removing plugin: {str(e)}"

def run(bot, message, args):
    if not args:
        return "❌ Please provide a plugin name to remove."
    
    plugin_name = args
    return remove_plugin(plugin_name)
