# repo-scaffolding

A [cookiecutter](https://github.com/audreyr/cookiecutter) template to generate necessary files for a Twitter Open Source project.

## Requirements
Install `cookiecutter` command line: `pip install cookiecutter`

---
`pip` is the package manager for Python. If you don't have pip, install Python.
```
brew install python
```

Note: `cookiecutter` can be installed with both `pip` and `pip3`.


## Usage

Run cookiecutter against this repository.

`cookiecutter https://github.com/twitter/repo-scaffolding`

or

`cookiecutter gh:twitter/repo-scaffolding`

or

You can also run it locally after cloning this repository:

`cookiecutter /path/to/directory/`

See [documentation](https://github.com/audreyr/cookiecutter#readme) for more usage instructions.

## Inputs

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

## Notes
 - Make sure to update the `TODO` sections in `README.md` and `CONTRIBUTING.md` after generating the files

## Authors

* TwitterOSS <opensource [at] twitter [dot] com>

Follow [@TwitterOSS](https://twitter.com/twitteross) on Twitter for updates.

## Security Issues?

Please report sensitive security issues via Twitter's bug-bounty program (https://hackerone.com/twitter) rather than GitHub.

## License

This project is licensed under the terms of the [Apache 2.0](/LICENSE)
