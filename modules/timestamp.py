# Developed on Python 3.12.0
# Provided during CS372 by Bram Lewis

import datetime


def ts_print(*args, **kwargs):
    """
    Custom print function that adds a timestamp to the beginning of the message.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments. These are passed to the built-in print function.
    """
    # Get the current time and format it
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the timestamp followed by the original message
    print(f"[{timestamp}]:", *args, **kwargs)
