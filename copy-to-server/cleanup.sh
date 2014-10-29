#!/bin/bash
yes | gluster volume stop $1 >/dev/null 2>/dev/null
yes | gluster volume delete $1 >/dev/null 2>/dev/null
rm -rf /tmp/brick9*
rm -rf /tmp/copy-to-server

