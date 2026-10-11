#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -c 'import sys; assert sys.version_info[:2] == (3,12), "Select Python 3.12 for this environment"'
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
MPLBACKEND=Agg .venv/bin/python verify_environment.py
.venv/bin/python -m pip check
.venv/bin/python -m pip freeze > requirements.resolved.txt
echo 'Research dependencies installed and verified.'
