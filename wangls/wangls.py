from halo import Halo
import socket
import subprocess
import os
import re
import sys
import click


def get_my_ip():
    """
    Find my IP address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def get_base_ip():
    """
    Gets the base ip.
    :return:
    """
    ip_parts = get_my_ip().split(".")
    base_ip = "{0}.{1}.{2}.".format(*ip_parts)
    return base_ip


@Halo(text="Scanning...", spinner="dots")
def is_nmap_installed():
    """Check whether `nmap` is on PATH and marked as executable."""

    from shutil import which

    return which("nmap") is not None


@Halo(text="Scanning...", spinner="dots")
def get_local_ips():
    """
      Gets the IP of devices connected to the local network
    """

    ip_range = f"{get_base_ip()}0/24"

    ips = subprocess.run(
        f"nmap -sn {ip_range} | grep report | awk '{{print $NF}}'",
        shell=True,
        capture_output=True,
        text=True,
    )
    return [[ip] for ip in ips.stdout.strip().split("\n")]


def get_ips_and_os():
    """
    Gets the IP and OS of devices connected to the local network
    """
    # Check if user is root
    if os.getuid() != 0:
        click.echo("TCP/IP fingerprinting (for OS scan) requires root privileges. Run sudo wangls -o")
        sys.exit()

    # my_ip = get_my_ip()
    ip_range = f"{get_base_ip()}0/24"
    with Halo(text="Scanning...", spinner="dots"):
        command_response = subprocess.run(
            f"nmap -sT -O {ip_range}", shell=True, capture_output=True, text=True
        )

    response_entries = command_response.stdout.split("\n\n")

    organized_data = []
    for i, entry in enumerate(response_entries):
        if i == len(response_entries) - 1:
            continue
        try:
            ip = re.search(r"(?<=Nmap scan report for)\s.*", entry).group(0).strip()
        except:
            ip = "n/a"

        # if ip == my_ip:
        #     continue
        try:
            mac_address = (
                re.search(r"(?<=:).([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}).*", entry)
                    .group(0)
                    .strip()
            )
        except:
            mac_address = "n/a"
        try:
            operating_system = re.search(r"(?<=OS details:)\s.*", entry).group(0).strip()
        except:
            operating_system = "n/a"

        map_list = [ip, mac_address, operating_system]
        if ip == "n/a":
            continue
        organized_data.append(map_list)
    return organized_data
