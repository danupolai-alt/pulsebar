#!/bin/bash
cd "$(dirname "$0")"
echo "🚀 Starting PulseBar v9.0..."
pip3 install -q rumps requests yfinance 2>/dev/null
python3 main.py &
