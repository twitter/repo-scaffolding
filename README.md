# repo-scaffolding

Scaffolding tools for creating and maintaining projects based on Twitter Open Source standards and best practices. The project has 3 parts -

1. [Cookiecutter template to generate Twitter OSS policy files e.g. LICENSE, CONTRIBUTING, etc.](https://github.com/twitter/repo-scaffolding#1-cookiecutter)
2. [Script to add License headers to all source files in a project](https://github.com/twitter/repo-scaffolding#2-license-headers-script)
3. [Lint a repository for common missing files (repolinter)](https://github.com/twitter/repo-scaffolding#3-linting-repolinter)

---

## 1. Cookiecutter template to generate OSS policy files

A [cookiecutter](https://github.com/audreyr/cookiecutter) template to generate necessary files for a Twitter Open Source project.

### Requirements
Install `cookiecutter` command line: `pip install cookiecutter`

---
`pip` is the package manager for Python.

Note: `cookiecutter` can be installed with both `pip` and `pip3`.


### Usage

Run cookiecutter against this repository.

`cookiecutter https://github.com/twitter/repo-scaffolding`

or

`cookiecutter gh:twitter/repo-scaffolding`

or

You can also run it locally after cloning this repository:

`cookiecutter /path/to/directory/`

See [documentation](https://github.com/audreyr/cookiecutter#readme) for more usage instructions.

### Inputs

See [cookiecutter.json](/cookiecutter.json) for all the variables required as input. Here is the list of places they are used

 - `author_full_name`: 1 time in `README.md` in the `Authors` section.
 - `author_email`: 1 time in `README.md` in the `Authors` section
 - `project_slug`: 1 time in `README.md` and also for the name of the parent directory
 - `github_repo_url`:  2 times in `README.md` and 4 times in `CONTRIBUTING.md` for the GitHub repo links
 - `short_description`: 1 time in `README.md`
 - `project_homepage`: 1 time in `README.md`
 - `documentation_homepage`: 1 time in `README.md`
 - `mailing_list`: 1 time in `README.md`
 - `release_year`: 1 time in `LICENSE` and 1 time in `README.md`

### Notes
 - Make sure to update the `TODO` sections in `README.md` and `CONTRIBUTING.md` after generating the files

## 2. License Headers

All source files [must have a license header](http://go/licenseheaders) at the top.
If you need to add headers to a lot of files, we recommend using the [google/addlicense](https://github.com/google/addlicense) tool.

## Installation

Download the [latest release](https://github.com/google/addlicense/releases/latest) for your operating system,
and place the binary someone in your shell path (like `/usr/local/bin/`).
Alternately, follow the [instructions for running with Docker](https://github.com/google/addlicense#running-in-a-docker-container).

## Usage

First, check to see which files addlicense would add headers to:

```
$ cd <path_to_source_dir>
$ addlicense -check .
```

If that looks right, add the appropriate Twitter headers:

```
$ addlicense -c "Twitter, Inc." -l "Apache-2.0" -s=only .
```

If you have third-party source in a `vendor` or `node_modules` directory, you
can ignore those with the `-ignore` flag to addlicense.


## 3. Linting (repolinter)

Lint all the necessary files in the project. - [Project Homepage](https://github.com/todogroup/repolinter)

- To run against a directory, use `npx repolinter /my/code/dir`
- To run against a git repository, use the --git option: `npx repolinter --git https://my.git.code/awesome`
- Note, if you are running a version of npm < 5.2.0, run `npm install npx` first.


---

## Authors

* TwitterOSS <opensource [at] twitter [dot] com>

Follow [@TwitterOSS](https://twitter.com/twitteross) on Twitter for updates.
