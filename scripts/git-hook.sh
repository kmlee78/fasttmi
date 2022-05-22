#!/bin/bash

# pre-commit hook install from pip
pre-commit install

# symlink
ln -sf ../../scripts/commit-msg-hook.py .git/hooks/commit-msg

# implement permission
chmod +x .git/hooks/commit-msg