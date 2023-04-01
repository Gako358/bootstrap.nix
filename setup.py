#!/usr/bin/env python3

import subprocess
import os
import sys


def run_command(command):
    subprocess.run(command, shell=True, check=True, text=True)


def main():
    if len(sys.argv) != 2:
        print("Usage: ./setup.py [desktop|laptop]")
        sys.exit(1)

    device_type = sys.argv[1]

    if device_type == "desktop":
        print("Running mkfs_desktop...")
        mkfs_desktop()
        print("Running setup_desktop...")
        setup_desktop()
    elif device_type == "laptop":
        print("Running mkfs_laptop...")
        mkfs_laptop()
        print("Running setup_laptop...")
        setup_laptop()
    else:
        print(f"Invalid device type: {device_type}")
        print("Usage: ./setup.py [desktop|laptop]")
        sys.exit(1)


if __name__ == "__main__":
    main()
