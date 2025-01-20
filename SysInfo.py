# author: bzym2
# describe: another exAMPLE PluGIN H YAY yAyAY
import os
import subprocess

def onLoad():
    print("[SystemInfo Plugin] Loaded successfully.")

def preHook():
    print("[SystemInfo Plugin] Pre-hook triggered.")

def afterHook():
    print("[SystemInfo Plugin] After-hook triggered.")

def registerCommands():
    return {
        'uptime': uptime_command,
        'df': df_command,
        'free': free_command
    }

def uptime_command(args):
    """Displays system uptime."""
    uptime = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
    print(uptime.stdout.strip())

def df_command(args):
    """Displays disk space usage."""
    df = subprocess.run(['df', '-h'], capture_output=True, text=True)
    print(df.stdout)

def free_command(args):
    """Displays memory usage."""
    free = subprocess.run(['free', '-h'], capture_output=True, text=True)
    print(free.stdout)

def getStyles():
    return {
        'systeminfo_theme': 'systeminfo> $ '  # Custom theme for system info commands
    }
