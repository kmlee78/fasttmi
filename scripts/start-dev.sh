#!/bin/bash
poetry install --no-interaction --no-ansi;
uvicorn fast_tmi.main:app --host 0.0.0.0 --reload;