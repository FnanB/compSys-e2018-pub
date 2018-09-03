#!/usr/bin/env bash

set -euo pipefail

PORT=1339
MOUNTPOINT=$1

# mkdir local

sshfs \
  neumann@localhost:.  \
  ${MOUNTPOINT} \
  -ocache=no \
  -onolocalcaches \
  -ovolname=compSys17 \
  -oport=${PORT} 
