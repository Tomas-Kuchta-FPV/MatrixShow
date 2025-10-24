#!/usr/bin/env bash

# Usage: ./find_ip_sonoff.sh 4f0d

if [ -z "$1" ]; then
  echo "Usage: $0 <last-4-hex-of-device-id>"
  exit 1
fi

ID="$1"

avahi-browse -a -r | grep $1 -A 1