# NOTE: Modify sections marked with `TODO` and then rename the file.

# How to Contribute

We'd love to get patches from you!

## Getting Started

### TODO: If you have 'good-first-issue' or 'easy' labels for newcomers, mention them here.

## Building dependencies

### TODO

## Building the Project

### TODO

## Workflow

We follow the [GitHub Flow Workflow](https://guides.github.com/introduction/flow/)

### TODO: Example below (from finatra)

1.  Fork finatra 
1.  Check out the `develop` branch 
1.  Create a feature branch
1.  Write code and tests for your change 
1.  From your branch, make a pull request against `twitter/finatra/develop` 
1.  Work with repo maintainers to get your change reviewed 
1.  Wait for your change to be pulled into `twitter/finatra/develop`
1.  Delete your feature branch

## Checklist

### TODO: Example below (from finatra)

There are a number of things we like to see in pull requests. Depending
on the scope of your change, there may not be many to take care of, but
please scan this list and see which apply. It's okay if something is missed;
the maintainers will help out during code review.

1. Include [tests](CONTRIBUTING.md#testing).
1. Update the [changelog](CHANGELOG.md) for new features, API breakages, runtime behavior changes,
   deprecations, and bug fixes.
1. All public APIs should have [Scaladoc][scaladoc].
1. When adding a constructor to an existing class or arguments to an existing
   method, in order to preserve backwards compatibility for Java users, avoid
   Scala's default arguments. Instead use explicit forwarding methods.
1. The second argument of an `@deprecated` annotation should be the current
   date, in `YYYY-MM-DD` form.

## Testing

### TODO

## Compatibility

We try to keep public APIs stable for the obvious reasons. Often,
compatibility can be kept by adding a forwarding method. Note that we
avoid adding default arguments because this is not a compatible change
for our Java users.  However, when the benefits outweigh the costs, we
are willing to break APIs. The break should be noted in the Breaking
API Changes section of the [changelog](CHANGELOG.md). Note that changes to
non-public APIs will not be called out in the [changelog](CHANGELOG.md).

## Style

### TODO: Code style guide

## Issues

### TODO: Confirm

When creating an issue please try to ahere to the following format:

    module-name: One line summary of the issue (less than 72 characters)

    ### Expected behavior

    As concisely as possible, describe the expected behavior.

    ### Actual behavior

    As concisely as possible, describe the observed behavior.

    ### Steps to reproduce the behavior

    List all relevant steps to reproduce the observed behavior.

## Pull Requests

### TODO: Confirm

Comments should be formatted to a width no greater than 80 columns.

Files should be exempt of trailing spaces.

We adhere to a specific format for commit messages. Please write your commit
messages along these guidelines. Please keep the line width no greater than 80
columns (You can use `fmt -n -p -w 80` to accomplish this).

    module-name: One line description of your change (less than 72 characters)

    Problem

    Explain the context and why you're making that change.  What is the problem
    you're trying to solve? In some cases there is not a problem and this can be
    thought of being the motivation for your change.

    Solution

    Describe the modifications you've done.

    Result

    What will change as a result of your pull request? Note that sometimes this
    section is unnecessary because it is self-explanatory based on the solution.

Some important notes regarding the summary line:

* Describe what was done; not the result 
* Use the active voice 
* Use the present tense 
* Capitalize properly 
* Do not end in a period — this is a title/subject 
* Prefix the subject with its scope

## Code Review

### TODO: Example below (from finatra)

The Finatra repository on GitHub is kept in sync with an internal repository at
Twitter. For the most part this process should be transparent to Finatra users,
but it does have some implications for how pull requests are merged into the
codebase.

When you submit a pull request on GitHub, it will be reviewed by the Finatra
community (both inside and outside of Twitter), and once the changes are
approved, your commits will be brought into Twitter's internal system for
additional testing. Once the changes are merged internally, they will be pushed
back to GitHub with the next sync.

This process means that the pull request will not be merged in the usual way.
Instead a member of the Finatra team will post a message in the pull request
thread when your changes have made their way back to GitHub, and the pull
request will be closed (see [this pull request][pull-example] for an example).
The changes in the pull request will be collapsed into a single commit, but the
authorship metadata will be preserved.

## Documentation

### TODO: Example below (from finatra)

We also welcome improvements to the Finatra documentation or to the existing
Scaladocs. Please file an [issue](https://github.com/twitter/finatra/issues).

[master-branch]: https://github.com/twitter/finatra/tree/master
[develop-branch]: https://github.com/twitter/finatra/tree/develop
[pull-example]: https://github.com/twitter/finagle/pull/267
[twitter-server-repo]: https://github.com/twitter/twitter-server 
[finagle-repo]: https://github.com/twitter/finagle 
[util-repo]: https://github.com/twitter/util
[effectivescala]: https://twitter.github.io/effectivescala/ 
[wordspec]: http://doc.scalatest.org/2.2.1/#org.scalatest.WordSpec 
[scalatest]: http://www.scalatest.org/ 
[scala-style-guide]: http://docs.scala-lang.org/style/scaladoc.html 
[sbt]: http://www.scala-sbt.org/
[travis-ci]: https://travis-ci.org/twitter/finatra 
[test-trait]: https://github.com/twitter/finatra/blob/develop/inject/inject-core/src/test/scala/com/twitter/inject/Test.scala
[scaladoc]: http://docs.scala-lang.org/style/scaladoc.html
[scalacheck]: https://www.scalacheck.org/
[gendrivenprop]: http://www.scalatest.org/user_guide/generator_driven_property_checks

## License 

By contributing your code, you agree to license your contribution under the 
terms of the APLv2: https://github.com/twitter/finatra/blob/master/LICENSE

## Code of Conduct

Read our [Code of Conduct](CODE_OF_CONDUCT.md) for the project.
