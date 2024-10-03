#!/bin/bash
set -e

virtualenv --without-pip virtualenv

pip install -r requirements.txt --target virtualenv/lib/python3.11/site-packages

GEOIP_COUNTRIES="GeoLite2-Country.mmdb"
GEOIP_ASN="GeoLite2-ASN.mmdb"

curl -fsL --retry 5 -o "$GEOIP_COUNTRIES" "https://git.io/GeoLite2-Country.mmdb"
if [ -s "$GEOIP_COUNTRIES" ]; then
  echo "GeoIP Country database downloaded successfully."
else
  echo "Error: Download failed or file is empty." >&2
  exit 1
fi

curl -fsL --retry 5 -o "$GEOIP_ASN" "https://git.io/GeoLite2-ASN.mmdb"
if [ -s "$GEOIP_ASN" ]; then
  echo "GeoIP ASN database downloaded successfully."
else
  echo "Error: Download failed or file is empty." >&2
  exit 1
fi


