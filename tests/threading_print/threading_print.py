from colorama import Fore, Style
import threading
import time
import sys
from queue import Queue
from typing import List
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.patch_stdout import patch_stdout


def handle_queue(q: Queue, stop_event: threading.Event):
    while not stop_event.is_set():
        if not q.empty():
            print(q.get())
            time.sleep(1)


def print_pass(q: Queue, stop_event: threading.Event):
    while not stop_event.is_set():
        q.put(f"{Fore.GREEN}[PASS]{Style.RESET_ALL}")
        time.sleep(1)


def print_fail(q: Queue, stop_event: threading.Event):
    while not stop_event.is_set():
        q.put(f"{Fore.RED}[FAIL]{Style.RESET_ALL}")
        time.sleep(1)


def main():
    output_queue: Queue = Queue()
    threads: List[threading.Thread] = []
    stop_event: threading.Event = threading.Event()

    queue_thread: threading.Thread = threading.Thread(
        target=handle_queue,
        args=(output_queue, stop_event,)
    )

    queue_thread.start()

    for i in range(10):
        t: threading.Thread = threading.Thread(
            target=print_pass, args=(output_queue, stop_event,))
        threads.append(t)
        t = threading.Thread(
            target=print_fail, args=(output_queue, stop_event,))
        threads.append(t)

    for thread in threads:
        thread.start()
        time.sleep(0.1)

    # Command completer for auto-completion
    # This is where you will add new auto-complete commands
    command_completer: WordCompleter = WordCompleter(
        ['exit'], ignore_case=True)

    # Create a prompt session
    session: PromptSession = PromptSession(completer=command_completer)

    # Variable to control the main loop
    is_running: bool = True

    try:
        with patch_stdout(raw=True):
            while is_running:
                # Using prompt-toolkit for input with auto-completion
                user_input: str = session.prompt("Enter command: ")

                # This is where you create the actions for your commands
                if user_input == "exit":
                    print("Exiting application...")
                    is_running = False
    finally:
        # Signal the worker thread to stop and wait for its completion
        stop_event.set()
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    main()
