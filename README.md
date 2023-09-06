# FastGen

Django style project generation made easy for FastApi

## Goal

My goal to produce a cli which will be able to generate project, app, deployment configuration out of the box.
Initially I am planning to create project boilarplate, using them you can be able to generate project and its component.
In the future, it might be able to do some smart action.

## What is/will be included

### Databases

| Database | Supported           | Priority |
|----------|---------------------|----------|
| Mongo DB | On Development      | Highest  |
| SQL      | Planning to support | Low      |

### Features

| Features       | Supported           | Priority |
|----------------|---------------------|----------|
| Versioning     | On Development      | High     |
| Deployment     | Planning to support | Medium   |
| Authentication | Planning to support | Medium   |
| Authorization  | Planning to support | Medium   |

## What is being used

I am using `jinja2` templating system to generate the project and `prompt_toolkit` for taking users input

## Needed Help

Any kind of help is appriciated, Please create an issue if -

1. I am missing something here
2. You want to help in creating some feature

## Instalation

1. Using pipx `pipx install git+https://github.com/PySign/FastGen.git` (Recomanded)
2. Using pip `pip install git+https://github.com/PySign/FastGen.git`

## Commands available

1. Generate project `fastgen -p` or `fastgen --project`
2. Get help `fastgen -h` or `fastgen --help`
