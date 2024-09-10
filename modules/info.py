import os
import datetime
import configparser
from colorama import Style

LOG_FILE: str = '/var/log/netmonitor/netmonitor.log'


def log(*args, **kwargs):
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"[{timestamp}]: " + " ".join(map(str, args)) + " " + \
            " ".join(f"{k}={v}" for k, v in kwargs.items())
        log.write(msg)
        log.write("\n")
        print(msg)


def print_title():
    width = os.get_terminal_size().columns
    title: str = rf"""{Style.BRIGHT}
  _   _ ______ _______ __  __  ____  _   _ _____ _______ ____  _____
 | \ | |  ____|__   __|  \/  |/ __ \| \ | |_   _|__   __/ __ \|  __ \
 |  \| | |__     | |  | \  / | |  | |  \| | | |    | | | |  | | |__) |
 | . ` |  __|    | |  | |\/| | |  | | . ` | | |    | | | |  | |  _  /
 | |\  | |____   | |  | |  | | |__| | |\  |_| |_   | | | |__| | | \ \
 |_| \_|______|  |_|  |_|  |_|\____/|_| \_|_____|  |_|  \____/|_|  \_\
    {Style.RESET_ALL}"""
    if width >= 80:
        print(title)


def print_intro_msg():
    intro_msg: str = f"""
 Welcome to {Style.BRIGHT}Netmonitor{Style.RESET_ALL}! Netmonitor provides a service that retrieves information
 about servers and their services based on user configuration, such as:

    - ICMP (Ping, Traceroute)   - DNS
    - HTTP/HTTPS                - NTP
    - UDP                       - TCP

 While configuration is stored locally, be mindful of any servers/services that
 you are testing, especially those that you don't own.

 Use the {Style.BRIGHT}'help'{Style.RESET_ALL} command to learn more about using and configuring Netmonitor.
 Otherwise, use the {Style.BRIGHT}'start'{Style.RESET_ALL} command to run the program with the default
 configuration.
    """
