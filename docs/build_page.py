import argparse
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIR = 'templates/'
EXCLUDE_TEMPLATES = ['base']


def render_template(template_name: str):
    if template_name in EXCLUDE_TEMPLATES:
        print("Trying to build excluded template {}, stopping".format(template_name))
        return

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(['html', 'xml'])
    )
    print("Loading template for template {}...".format(template_name))
    template = env.get_template('{}.html'.format(template_name))

    outfilename = '{}.html'.format(template_name)
    print("Writing rendered template to {}...".format(outfilename))
    with open(outfilename, "w") as outfile:
        outfile.write(template.render())
    print("Done")


def render_all():
    for file in os.listdir(TEMPLATE_DIR):
        template_name = file.split(".html")[0]
        print("Rendering {}".format(template_name))
        render_template(template_name)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build templates for Lando project')
    parser.add_argument('template_name', nargs='?', help='Template to use')
    parser.add_argument('--all', help='Build all templates', action='store_true')
    args = parser.parse_args()
    if args.all:
        render_all()
    else:
        render_template(args.template_name)
