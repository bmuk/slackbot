import logging
import subprocess
import sys
from slouch import Bot, help

class OpsBot(Bot):
    def prepare_connection(self, config):
        print("MY NAME IS: {}".format(self.name))
        print("MY ID IS: {}".format(self.id))
        print("MY MENTION IS: {}".format(self.my_mention))

# Provides help on available commands
OpsBot.command(help)

@OpsBot.command
def update(opts, bot, event):
    """
    Usage: update

    Updates all laptops in the lab.
    """
    proc = subprocess.Popen(["nixops"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if err:
        return "Error: {}".format(err)
    else:
        return out

def main():
    try:
        token = sys.argv[1]
    except:
        print("Must provide API token.")
        sys.exit(2)
    log = logging.getLogger("slouch")
    log.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    log.addHandler(console_handler)
    bot = OpsBot(token, {})
    bot.run_forever()

if __name__ == "__main__":
    main()
