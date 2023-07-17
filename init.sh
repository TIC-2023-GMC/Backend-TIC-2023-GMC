#!/bin/bash
python3 docker-entrypoint-initdb.d/initial_data_script.py
echo "Initial data script executed"
