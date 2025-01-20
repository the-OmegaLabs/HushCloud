# author: bzym2
# describe: Example Plugin LOLOLOLOL LMAO
import os
import signal
import subprocess

def onLoad():
    print("[ProcessManager Plugin] Loaded successfully.")

def preHook():
    print("[ProcessManager Plugin] Pre-hook triggered.")

def afterHook():
    print("[ProcessManager Plugin] After-hook triggered.")

def registerCommands():
    return {
        'ps': ps_command,
        'kill': kill_command,
        'top': top_command
    }

def ps_command(args):
    """Displays the current running processes."""
    processes = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    print(processes.stdout)

def kill_command(args):
    """Kills a process by its PID."""
    if len(args) == 2:
        try:
            pid = int(args[1])
            os.kill(pid, signal.SIGTERM)
            print(f"Killed process {pid}.")
        except ValueError:
            print("Error: PID must be a number.")
        except ProcessLookupError:
            print(f"Error: No process found with PID {pid}.")
    else:
        print("Usage: kill <PID>")

def top_command(args):
    """Displays the system's top processes."""
    subprocess.run(['top', '-n', '1'])  # Run top command once

def getStyles():
    return {
        'process_theme': 'process> $ '  # Custom theme for process commands
    }
