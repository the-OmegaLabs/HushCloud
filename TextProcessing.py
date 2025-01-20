# author: bzym2
# describe: eXAmPlepLuGiN
import subprocess

def onLoad():
    print("[TextProcessing Plugin] Loaded successfully.")

def preHook():
    print("[TextProcessing Plugin] Pre-hook triggered.")

def afterHook():
    print("[TextProcessing Plugin] After-hook triggered.")

def registerCommands():
    return {
        'grep': grep_command,
        'cat': cat_command,
        'head': head_command,
        'tail': tail_command
    }

def grep_command(args):
    """Search for a pattern in a file."""
    if len(args) > 2:
        pattern, file = args[1], args[2]
        grep = subprocess.run(['grep', pattern, file], capture_output=True, text=True)
        print(grep.stdout)
    else:
        print("Usage: grep <pattern> <file>")

def cat_command(args):
    """Displays the content of a file."""
    if len(args) > 1:
        file = args[1]
        with open(file, 'r') as f:
            print(f.read())
    else:
        print("Usage: cat <file>")

def head_command(args):
    """Displays the first 10 lines of a file."""
    if len(args) > 1:
        file = args[1]
        with open(file, 'r') as f:
            print(''.join([next(f) for _ in range(10)]))
    else:
        print("Usage: head <file>")

def tail_command(args):
    """Displays the last 10 lines of a file."""
    if len(args) > 1:
        file = args[1]
        with open(file, 'r') as f:
            lines = f.readlines()[-10:]
            print(''.join(lines))
    else:
        print("Usage: tail <file>")

def getStyles():
    return {
        'textprocessing_theme': 'textproc> $ '  # Custom theme for text processing commands
    }
