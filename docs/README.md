Command to watch and rebuild all bases when things change:

From this directory:

watchmedo shell-command --patterns="*.html" --recursive --command='python build_page.py --all' templates