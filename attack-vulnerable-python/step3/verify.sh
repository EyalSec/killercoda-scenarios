#!/bin/bash
expected=$(docker exec vulnerable-python whoami)
[ -n "$expected" ] && grep -qx "$expected" /root/app-user.txt
