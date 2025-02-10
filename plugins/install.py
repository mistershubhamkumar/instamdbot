import os
import subprocess

def install_plugin(github_url):
    try:
        repo_name = github_url.split("/")[-1].replace(".git", "")
        plugin_folder = f"plugins/{repo_name}"
        
        if not os.path.exists(plugin_folder):
            subprocess.run(["git", "clone", github_url, plugin_folder])
            load_plugins()
            return f"✅ Plugin '{repo_name}' has been installed successfully."
        else:
            return f"❌ Plugin '{repo_name}' already exists."
    except Exception as e:
        return f"❌ Error installing plugin: {str(e)}"

def run(bot, message, args):
    if not args:
        return "❌ Please provide a valid GitHub URL."
    
    github_url = args
    return install_plugin(github_url)
