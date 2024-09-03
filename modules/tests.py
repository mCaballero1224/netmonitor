import threading
import time
import network_functions as nf
from colorama import Fore, Back, Style
from globals import longest_name
from timestamp import ts_print


def icmp_test(server_name: str, server: str, ttl: int, timeout: int,
              sequence_number: int, interval: int,
              stop_event: threading.Event):
    while not stop_event.is_set():
        time_limit = interval
        ping_addr, ping_time = nf.ping(server, ttl, timeout, sequence_number)
        output = f"[{server_name}]".ljust(longest_name) + " [ICMP] "
        if ping_time is None:
            output += Fore.RED + \
                "[FAIL]".ljust(6) + Style.RESET_ALL + \
                f"[{ping_addr[0]}, 'No reponse received']"
        else:
            output += Fore.GREEN + \
                "[OK]".ljust(6) + Style.RESET_ALL + \
                f"[{ping_addr[0]}, {ping_time:.2f}ms]"
        ts_print(output)
        while time_limit > 0:
            time.sleep(0.1)
            time_limit -= 0.1
            if stop_event.is_set():
                break


def http_test(server_name: str, server: str, interval: int,
              stop_event: threading.Event):
    pass


def https_test(server_name: str, server: str, interval: int,
               stop_event: threading.Event):
    pass


def dns_test(server_name: str, server: str, dns_records: str,
             interval: int, stop_event: threading.Event):
    pass


def ntp_test(server_name: str, server: str, interval: int,
             stop_event: threading.Event):
    pass


def tcp_test(server_name: str, server: str, port: int, interval: int,
             stop_event: threading.Event):
    pass


def udp_test(server_name: str, server: str, port: int, interval: int,
             stop_event: threading.Event):
    pass


def echo_test(server_name: str, server: str, type: str, port: int,
              stop_event: threading.Event):
    pass
