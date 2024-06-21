#!/bin/sh
source .venv/bin/activate
python -m flask --app app --debug run -p 5000 