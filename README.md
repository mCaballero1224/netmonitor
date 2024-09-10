# netmonitor

A python application that monitors services based on user configuration.

## Installation

## Download the Git repo
Download the application and necessary files, then enter the directory with the following commands:

```
git clone https://github.com/mCaballero1224/netmonitor.git
cd ./netmonitor
```

## Initial Configuration

You'll need to change a few things before running the install script. First, you'll edit the `Environment` attribute in the file `netmonitor/service/netmonitor.service` to match your environment's `XDG_CONFIG_HOME`. If you don't know it, you can find it with this command:

```
echo $XDG_CONFIG_HOME
```

## Running the Install Script

The install script `nm-install` relies on the user's environment variables while also requiring elevated privileges. Use the `--preserve-env` or `-E` option with sudo to ensure smooth installation.

```
chmod +x ./nm-install
sudo -E python ./nm-install
```

The script does the following:

- Creates the configuration directory in your `XDG_CONFIG_HOME` and places `config.ini` and the `modules` directory within it.
- Creates the log directory in `/var/log/netmonitor` along with two log files `netmonitor.log` and `error.log` within the directory.
- Places the `netmonitor` script in `/usr/bin`
- Places the `nmcli` client script in `/usr/bin`
- Places the `netmonitor.service` file within `/etc/systemd/user/netmonitor.service` so that it can be ran as a user service by systemd.

The script also changes file/user permissions for executables (`nmcli`/`netmonitor`) and the config directory (`.config/netmonitor`), but you'll need to change the permissions for the log directory:

```
chown -R your_username /var/log/netmonitor/
```


### Running the Service

Reload systemd:
```
systemctl --user daemon-reload
```

Run the service with systemd as a user service:
```
# sets the serivce to run on boot
systemctl --user enable netmonitor.service
# starts the service
systemctl --user start netmonitor.service
```

### Accessing Netmonitor

Use the `nmcli` client to access the service. You can access it via a Unix socket:

```
# You can also specify to use the Unix socket with the --local flag
nmcli
```

Or you can access it via a TCP socket connection:
```
# The default port is 2077
# Specify a port with the --port or -p option
# Specify the hostname with the --hostname option
# You can change this default in the config.ini file
nmcli --hostname 127.0.0.1 --port 20777
```



## Requirements

1. Network Monitoring Application
    1. Create an application that uses the configuration information in Requirement 2 to automatically check the status of servers and services.
    2. Application should run continuously using a loop until it is terminated by the user (i.e. this is not a one-time check).
2. User-Defined Monitoring Configuration
    1. Configure a list of servers (IP addresses or domain name) and services they want to monitor (HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP).
    2. Setting parameters for each service check, such as URL for HTTP/HTTPS, server address for DNS/NDP, port numbers for TCP/UDP, etc.
    3. Set the frequency or interval of checks for each service. 

## Configuration

Placeholder. To be written

## Motivation

Placeholder. To be written
