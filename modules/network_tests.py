import configparser
import os
import threading
import time
import networking as nw

# Initialize config object and read config file
HOME = os.getenv("HOME")
CONFIG_FILE = os.path.join(HOME, '.config'


def format_results(server_name: str, test_type: str, result: bool,
                   details: str) -> str:
    output: str=f"[{server_name}]".


def ping_test(server_name: str, server: str, ttl: int, timeout: int,
              sequence_number: int, interval: int,
              stop_event: threading.Event):
    while not stop_event.is_set():
        time_limit=interval
        ping_addr, ping_time=nw.ping(
            server, ttl, timeout, sequence_number)
        output=f"[{server_name}]".ljust(longest_name) + "[ICMP] "
        if ping_time is None:
            output += f"{Fore.RED}[FAIL]{Style.RESET_ALL}" +
                f" [{ping_addr[0]}, 'No reponse received']"
        else:
            output += f"{Fore.GREEN}[PASS]{Style.RESET_ALL}" +
                f" [{ping_addr[0]}, {ping_time:.2f}ms]"
        with print_lock:
            ts_print(output)
        while time_limit > 0:
            time.sleep(0.1)
            time_limit -= 0.1
            if stop_event.is_set():
                break


def http_test(server_name: str, server: str, interval: int,
              stop_event: threading.Event):
    while not stop_event.is_set():
        time_limit=interval
        url: str=f"http://{server}"
        output=f"[{server_name}]".ljust(longest_name) + "[HTTP] "
        server_status, response_code=check_server_http(url)
        if server_status:
            output += f"{Fore.GREEN}[PASS]{Style.RESET_ALL}"
            output += f" [{url}, " +
                f"({response_code}, '{get_http_msg(response_code)}')]"
        else:
            output += f"{Fore.RED}[FAIL]{Style.RESET_ALL}" +
                " ['No response received']"
        with print_lock:
            ts_print(output)
        while time_limit > 0:
            time.sleep(0.1)
            time_limit -= 0.1
            if stop_event.is_set():
                break


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
              interval: int, stop_event: threading.Event):
    pass


def traceroute_test(server_name: str, server: str, max_hops: int,
                    pings_per_hop: int, verbose: bool, interval: int,
                    stop_event: threading.Event):
    while not stop_event.is_set():
        time_limit=interval
        traceroute_results: str=traceroute(
            server, max_hops, pings_per_hop, verbose)
        output=f"[{server_name}]".ljust(longest_name)
        output += "[TRACE]".ljust(8)
        with print_lock:
            ts_print(output)
            print(traceroute_results)
        while time_limit > 0:
            time.sleep(0.1)
            time_limit -= 0.1
            if stop_event.is_set():
                break


tests: dict={
    'ping': ping_test,
    'traceroute': traceroute_test,
    'http': http_test,
    'https': https_test,
    'dns':  dns_test,
    'ntp': ntp_test,
    'tcp': tcp_test,
    'udp': udp_test,
    'echo': echo_test
}

if __name__ == "__main__":
    print(tests.get('ping'))
