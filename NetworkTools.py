# author: bzym2
# describe: ExamplLLLLE PLuGiN
import subprocess

def onLoad():
    print("[NetworkTools Plugin] Loaded successfully.")

def preHook():
    print("[NetworkTools Plugin] Pre-hook triggered.")

def afterHook():
    print("[NetworkTools Plugin] After-hook triggered.")

def registerCommands():
    return {
        'ping': ping_command,
        'ifconfig': ifconfig_command,
        'wget': wget_command
    }

def ping_command(args):
    """Pings a host."""
    if len(args) > 1:
        host = args[1]
        ping = subprocess.run(['ping', host], capture_output=True, text=True)
        print(ping.stdout)
    else:
        print("Usage: ping <host>")

def ifconfig_command(args):
    """Displays network interfaces."""
    ifconfig = subprocess.run(['ifconfig'], capture_output=True, text=True)
    print(ifconfig.stdout)

def wget_command(args):
    """Downloads a file from the internet."""
    if len(args) > 1:
        url = args[1]
        wget = subprocess.run(['wget', url], capture_output=True, text=True)
        print(wget.stdout)
    else:
        print("Usage: wget <url>")

def getStyles():
    return {
        'network_theme': 'network> $ '  # Custom theme for network tools commands
    }
