from argparse import ArgumentParser

from FastGen.generators.project import generate_project


def create_args_parser():
    parser = ArgumentParser()
    # parser.add_argument('-e', '--exclude', metavar='PATTERN', dest='excludes', action='append', default=[])
    # parser.add_argument('-o', '--output', metavar='file_path', dest='output', default='dist')

    parser.add_argument('project')
    return parser


def main():
    parser = create_args_parser()
    options, unknown = parser.parse_known_args()
    project = options.project
    generate_project(project)


if __name__ == '__main__':
    main()
