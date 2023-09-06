from argparse import ArgumentParser

from FastGen.generators.project.main import Project


def create_args_parser():
    parser = ArgumentParser()
    # parser.add_argument('-v', '--version', metavar='VERSION', dest='vesrion', default=None)
    # parser.add_argument('-o', '--output', metavar='file_path', dest='output', default='dist')

    parser.add_argument(
        '-p', '--project', dest='project',
        help='Initialize a project in current directory',
        action='store_true'
    )
    parser.add_argument(
        '-a', '--app', dest='app',
        help='Create a new app inside current project',
        action='store_true'
    )
    parser.add_argument(
        '-f', '--force', dest='force',
        help='Override existing app or project',
        action='store_true'
    )
    return parser


def main():
    parser = create_args_parser()
    options, _ = parser.parse_known_args()
    if options.project:
        Project(options.force)


if __name__ == '__main__':
    main()
