#!/usr/bin/python3

from typing import List


def validate_command(command: str, arguments: tuple) -> bool:
    return False


prompt_commands: List = ['create', 'list', 'help',
                         'update', 'delete', 'monitor', 'status']
