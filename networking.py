import os
import subprocess
from dataclasses import dataclass
import re
from typing import List


@dataclass
class WifiScan:
    channel: int
    address: str
    freq: str
    power: str
    essid: str
    mode: str

    def __lt__(self, other):
        return self.power < other.power


def start_managed_mode(interface: str):
    os.system(f"ifconfig {interface} down")
    os.system(f"iwconfig {interface} mode managed")
    os.system(f"ifconfig {interface} up")


def scan_wifi(interface: str) -> List[WifiScan]:
    """
    Scan wifi and return result.
    """
    ret = []

    # Scan wifi
    result = subprocess.run(
        ['iwlist', interface, 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = result.stdout.decode()
	
    # Read output with custom regex and save to "filtered_matches"
    pattern = r'(Cell \d+.*\n(?:\s{20}.*\n)+)'
    compiled_pattern = re.compile(pattern, re.MULTILINE)

    m = re.findall(compiled_pattern, out)

    filtered_matches = []
    for match in m:
        lines = match.split('\n')
        # Remove IE: Unkown: lines
        lines = [line for line in lines if "IE: Unknown:" not in line]
        filtered_matches.append(lines)

    for cell in filtered_matches:
        address = re.search("Address: (.*)", cell[0]).group(1)
        channel = int(re.search("Channel:(\d+)", cell[1]).group(1))
        freq = re.search("Frequency:(.+GHz)", cell[2]).group(1)
        power = re.search("Signal level=(.*dBm)", cell[3]).group(1)
        essid = re.search("ESSID:\"(.*)\"", cell[5]).group(1)
        mode = re.search("Mode:(.*)", cell[9]).group(1)

        wifiscan = WifiScan(channel, address, freq, power, essid, mode)
        ret.append(wifiscan)
    return ret
