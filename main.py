#!/usr/bin/env python3

import sys
import base64
import argparse

if __name__ == "__main__":
    print("PSSH Gen v.1 by m0style\n")

# TODO argparse --url, --file, --verbose

cli = argparse.ArgumentParser()
cli.add_argument("--verbose", "--v", help="enable verbose outpot", action="store_true")
cli.add_argument("--url", help="URL to attempt MPD download from")
cli.add_argument("--file", help="path to existing MPD")
# cli.add_argument("--debug", help="URL to attempt MPD download from")
args = cli.parse_args()
if not (args.url or args.file):
    print("Unmet requirement!  You must specify --url or --file")
    sys.exit(1)
elif args.file and args.url:
    print("Too many options!  You must specify only one of --url or --file")
