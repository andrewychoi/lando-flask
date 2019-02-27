import argparse

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main(template_name: str):
    env = Environment(
        loader=FileSystemLoader('templates/'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    print("Loading template for template {}...".format(template_name))
    template = env.get_template('{}.html'.format(template_name))

    outfilename = '{}.html'.format(template_name)
    print("Writing rendered template to {}...".format(outfilename))
    with open(outfilename, "w") as outfile:
        outfile.write(template.render())
    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('template_name', help='an integer for the accumulator')
    args = parser.parse_args()
    main(args.template_name)
