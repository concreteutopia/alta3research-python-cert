#!/bin/bash

reason=$1

cd ~/alta3research-python-cert/
git status
git add ~/alta3research-python-cert/*
git commit -m "$1"
git push origin main
