import configparser
import threading
import time
from typing import List, Tuple
from timestamp import ts_print
from network_functions import *

# pull configuration from '../config.ini'
config = configparser.ConfigParser()
config.read('../config.ini')


def icmp_test(server_name: str, server: str, ttl: int, timeout: int,
              sequence_number: int, interval: int,
              stop_event: threading.Event):
    while not stop_event.is_set():
        time_limit = interval
        ping_addr, ping_time = ping(server, ttl, timeout, sequence_number)
        output = f"[{server_name}]".ljust(longest_name) + " [ICMP] "
        if ping_time is None:
            output += "[FAIL]".ljust(6) + \
                f"[{ping_addr[0]}, 'No reponse received']"
        else:
            output += "[OK]".ljust(6) + f"[{ping_addr[0]}, {ping_time:.2f}ms]"
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


def generate_threads() -> Tuple[List[threading.Thread], threading.Event]:
    global t  # global since this value will change often
    global section, server
    # list of threads that have been generated
    threads: List[threading.Thread] = []
    # stop event to signal when threads should cease operation
    stop_event = threading.Event()

    # generate the threads based on config.init
    for section in config.sections():
        # grap the ip/domain name of the server
        server = config.get(section, 'server', fallback='')
        if not server:
            print(f"No value for 'domain_name' or 'ip_address' given for \
            {section}. Check the file 'config.ini' for missing values.")
            continue  # move onto the next server configuration

        # Check each test's boolean value to create a thread if True

        # ICMP check
        if config.getboolean(section, 'test_icmp'):
            print(f"ICMP test initialized for {section}")
            # grab interval
            interval = config.getint(section, 'icmp_interval')
            ttl = config.getint(section, 'icmp_ttl')
            timeout = config.getint(section, 'icmp_timeout')
            sequence_number = config.getint(section, 'icmp_sequence_number')
            # create thread
            t = threading.Thread(
                target=icmp_test, args=(section, server, ttl, timeout,
                                        sequence_number, interval,
                                        stop_event,))
            # append thread to list
            threads.append(t)

        # HTTP test
        if config.getboolean(section, 'test_http'):
            print(f"HTTP test initialized for {section}")
            interval = config.getint(section, 'http_interval')
            t = threading.Thread(
                target=http_test, args=(section, server, interval,
                                        stop_event,))
            threads.append(t)

        # HTTPS test
        if config.getboolean(section, 'test_https'):
            print(f"HTTPS test initialized for {section}")
            interval = config.getint(section, 'https_interval')
            t = threading.Thread(
                target=https_test, args=(section, server, interval,
                                         stop_event,))
            threads.append(t)

        # DNS test
        if config.getboolean(section, 'test_dns'):
            print(f"DNS test initialized for {section}")
            interval = config.getint(section, 'dns_interval')
            dns_records = config.get(section, 'dns_records')
            t = threading.Thread(
                target=dns_test, args=(section, server, dns_records, interval,
                                       stop_event,))
            threads.append(t)

        # NTP test
        if config.getboolean(section, 'test_ntp'):
            print(f"NTP test initialized for {section}")
            interval = config.getint(section, 'ntp_interval')
            t = threading.Thread(
                target=ntp_test, args=(section, server, interval, stop_event,))
            threads.append(t)

        # TCP test
        if config.getboolean(section, 'test_tcp'):
            print(f"TCP test initialized for {section}")
            interval = config.getint(section, 'tcp_interval')
            port = config.getint(section, 'tcp_port')
            t = threading.Thread(
                target=tcp_test, args=(section, server, port, interval,
                                       stop_event,))
            threads.append(t)

        # UDP test
        if config.getboolean(section, 'test_udp'):
            print(f"UDP test initialized for {section}")
            interval = config.getint(section, 'udp_interval')
            port = config.getint(section, 'udp_port')
            t = threading.Thread(
                target=udp_test, args=(section, server, port, interval,
                                       stop_event,))
            threads.append(t)

        # Echo test
        if config.getboolean(section, 'test_echo'):
            print(f"Echo test initialized for {section}")
            echo_type = config.get(section, 'echo_type')
            port = config.getint(section, 'echo_port')
            t = threading.Thread(
                target=echo_test, args=(section, server, echo_type, port,
                                        stop_event,))
            threads.append(t)

        # Traceroute Test
        if config.getboolean(section, 'traceroute_test'):
            print(f"Traceroute test initialized for {section}")

    print("Threads generated!")
    return [threads, stop_event]


if __name__ == "__main__":
    global longest_name

    longest_name: int = 0
    for section in config.sections():
        if len(section) > longest_name:
            longest_name = len(section)
    longest_name += 2

    threads, stop_event = generate_threads()

    for thread in threads:
        thread.start()
        time.sleep(0.1)

    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\nStopping all tests...")
        stop_event.set()
