# NOTE: Modify sections marked with `TODO` and then rename the file.

# {{ cookiecutter.project_slug }}

{{ cookiecutter.short_description }}

## Getting Started

{% if cookiecutter.project_homepage != "none" %} * Website: {{ cookiecutter.project_homepage }} {% endif %}
{% if cookiecutter.documentation_homepage != "none" %} * Documentation: {{ cookiecutter.documentation_homepage }} {% endif %}
* Mailing List: {{ cookiecutter.mailing_list }}

## Support

Create a [new issue](https://github.com/{{ cookiecutter.github_repo_url }}/issues/new) on GitHub.

## Contributing

We feel that a welcoming community is important and we ask that you follow Twitter's
[Open Source Code of Conduct](https://github.com/twitter/code-of-conduct/blob/master/code-of-conduct.md)
in all interactions with the community.

## Authors

* {{ cookiecutter.author_full_name }} <{{ cookiecutter.author_email }}>

A full list of [contributors](https://github.com/{{ cookiecutter.github_repo_url }}/graphs/contributors?type=a) can be found on GitHub.

Follow [@TwitterOSS](https://twitter.com/twitteross) on Twitter for updates.

## License

Copyright {{ cookiecutter.release_year }} Twitter, Inc.

Licensed under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0

## Security Issues?

Please report sensitive security issues via Twitter's bug-bounty program (https://hackerone.com/twitter) rather than GitHub.

### TODO: Create your own [Awesome README](https://github.com/matiassingers/awesome-readme)!
