#!/bin/bash
echo "Starting vulnerable-python. This takes about half a minute..."
while [ ! -f /tmp/eyalsec-ready ]; do sleep 1; done
clear
echo "vulnerable-python is running on http://127.0.0.1:5000/"
