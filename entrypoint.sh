#!/bin/sh
gunicorn --bind 0.0.0.0:8080 wsgi:application -w 1
