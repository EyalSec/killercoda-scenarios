#!/bin/bash
curl -fs "http://127.0.0.1:5000/sqli?name=alice" | grep -q alice
