from FastGen.generators.project import generate_project


def main():
    print('Hello from FastGen')
    project = input('Enter Project Name: ')
    generate_project(project)
