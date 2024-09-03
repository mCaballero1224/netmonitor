import configparser

# pull configuration from '../config.ini'
config = configparser.ConfigParser()
config.read('../config.ini')

longest_name: int = 0

# update longest name based on config
for section in config.sections():
    if len(section) > longest_name:
        longest_name = len(section)

longest_name += 2  # account for brackets in output
print(longest_name)
