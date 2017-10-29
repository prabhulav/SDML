#!/bin/bash
echo "Starting.."
python filesplit.py
echo "second"
python extractColumns.py
echo "third"
python comments_count.py
echo "The End"