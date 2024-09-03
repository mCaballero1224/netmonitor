import threading
import time
from typing import List, Tuple
from globals import config
import tests


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
                target=tests.icmp_test,
                args=(section, server, ttl, timeout, sequence_number, interval,
                      stop_event,))
            # append thread to list
            threads.append(t)

        # HTTP test
        if config.getboolean(section, 'test_http'):
            print(f"HTTP test initialized for {section}")
            interval = config.getint(section, 'http_interval')
            t = threading.Thread(
                target=tests.http_test,
                args=(section, server, interval, stop_event,))
            threads.append(t)

        # HTTPS test
        if config.getboolean(section, 'test_https'):
            print(f"HTTPS test initialized for {section}")
            interval = config.getint(section, 'https_interval')
            t = threading.Thread(
                target=tests.https_test,
                args=(section, server, interval, stop_event,))
            threads.append(t)

        # DNS test
        if config.getboolean(section, 'test_dns'):
            print(f"DNS test initialized for {section}")
            interval = config.getint(section, 'dns_interval')
            dns_records = config.get(section, 'dns_records')
            t = threading.Thread(
                target=tests.dns_test,
                args=(section, server, dns_records, interval, stop_event,))
            threads.append(t)

        # NTP test
        if config.getboolean(section, 'test_ntp'):
            print(f"NTP test initialized for {section}")
            interval = config.getint(section, 'ntp_interval')
            t = threading.Thread(
                target=tests.ntp_test,
                args=(section, server, interval, stop_event,))
            threads.append(t)

        # TCP test
        if config.getboolean(section, 'test_tcp'):
            print(f"TCP test initialized for {section}")
            interval = config.getint(section, 'tcp_interval')
            port = config.getint(section, 'tcp_port')
            t = threading.Thread(
                target=tests.tcp_test,
                args=(section, server, port, interval, stop_event,))
            threads.append(t)

        # UDP test
        if config.getboolean(section, 'test_udp'):
            print(f"UDP test initialized for {section}")
            interval = config.getint(section, 'udp_interval')
            port = config.getint(section, 'udp_port')
            t = threading.Thread(
                target=tests.udp_test,
                args=(section, server, port, interval, stop_event,))
            threads.append(t)

        # Echo test
        if config.getboolean(section, 'test_echo'):
            print(f"Echo test initialized for {section}")
            echo_type = config.get(section, 'echo_type')
            port = config.getint(section, 'echo_port')
            t = threading.Thread(
                target=tests.echo_test,
                args=(section, server, echo_type, port, stop_event,))
            threads.append(t)

        # Traceroute Test
        if config.getboolean(section, 'traceroute_test'):
            print(f"Traceroute test initialized for {section}")

    print("Threads generated!")
    return [threads, stop_event]


if __name__ == "__main__":
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
