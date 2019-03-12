#! /bin/bash

echo "Watching for changes to template files..."
firefox .
watchmedo shell-command --patterns="*.html" --recursive --command='python build_page.py --all' templates
