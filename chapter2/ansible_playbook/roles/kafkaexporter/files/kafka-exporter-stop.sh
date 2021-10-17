#!/bin/bash
PIDS=$(ps ax | grep -i 'kafka\_exporter' | awk '{print $1}')

if [ -z "$PIDS" ]; then
  echo "No kafka_exporter stop"
  exit 1
else
  kill -s TERM $PIDS
fi