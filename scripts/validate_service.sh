#!/bin/bash

# Basic check to confirm the web app is running on port 8080 (Playwright default)
sleep 10
curl --fail http://localhost:8080/ || exit 1
