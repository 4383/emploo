# Contributing to emploo

First off, thanks for taking the time to contribute!

The following as a set of guidelines for contributing to emploo.
These are mostly guidelines, not rules. Use your best judgment, and feel
free to propose changes to this document in a pull request.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for emploo.
Following these guidelines helps maintainers and the community
understand your report, reproduce the behavior, and find related reports.

Before creating bug reports, please perform a
[cursory search](https://github.com/4383/emploo/issues?q=is%3Aissue%20is%3Aopen%20)
to see if the problem has already been reported.
If it has and the issue is still open, add a comment to
the existing issue instead of opening a new one.
When you are creating a bug report, please [include as many details as possbile](#how-do-i-submit-a-good-bug-report).

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/).

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you use the emploo command line, e.g. which command exactly you used in the terminal. When listing steps, **don't just say what you did, but explain how you did it**.
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**


Provide more context by answering these questions:

* **Did the problem start happening recently** (e.g. after updating to a new version of emploo) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older version of emploo?** What's the most recent version in which the problem doesn't happen? You can install older versions of emploo from [the pypi repository](https://pypi.org/project/emploo/).
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.

Include details about your configuration and environment:

* **Which version of emploo are you using?** You can get the exact version by running `pip freeze | grep "emploo"` in your terminal.
* **What's the name and version of the OS you're using**?
* **What's the version of python you're using**?

### Writing docs and examples

Community needs docs and real examples to know how to use emploo. If you
want you can propose this kind of changes and help other people to use this
software.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for emploo, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion and find related suggestions.

When you are creating an enhancement suggestion, please [include as many details as possible](#how-do-i-submit-a-good-enhancement-suggestion) and including the steps that you imagine you would take if the feature you're requesting existed.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/).

Provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of emploo which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **Explain why this enhancement would be useful** to most emploo users.
* **List some other tools or applications where this enhancement exists.**
* **Specify which version of emploo you're using.** You can get the exact version by running `pip freeze| grep "emploo"` in your terminal.
* **Specify the name and version of the OS you're using.**
* **Specify the version of python you're using**

## Code Contribution

### Hacking on emploo

If you're hitting a bug in emploo or just want to experiment with adding a feature, follow these steps.

#### Prerequisites

- [tox](https://tox.readthedocs.io/en/latest/)
- python 3.9+

#### Cloning

```shell
$ git clone https://github.com/4383/emploo
```

#### Setup your environment

From there, you can navigate into the directory where you've cloned
the emploo source code:

```shell
$ cd emploo
```

You can install the development tools by using:
```
python3.11 -m pip install --editable ".[dev]"
```

And enabling `pre-commit` for emploo:
```
$ pre-commit install
```

`tox` allow you to use emploo directly in a dedicated virtual environment
already configured (requirements, etc):

```shell
$ tox -e venv -- emploo -h
...
___________________ summary ______________
  venv: commands succeeded
  congratulations :)

$ tox -e venv -- emploo init
...
```

#### Make your changes

First create your working branch:

```shell
$ git checkout -b somefeature origin/master
```

> Be sure to create your working branch from `master` and be sure your master are up-to-date

Make our changes:

```shell
$ vim <file-to-edit>
$ git commit -am 'I did some changes'
```

#### Ensure everything work fine

Every following checks are automaticaly executed on pull requests so need to
be sure that all of these checks run successfully before submit your pull request
on github.

Code formating and PEP8 validation:
```shell
$ tox -e pep8
```

Unit tests:
```shell
$ tox # by default run tests with all the python versions specified in tox.ini
```

> Note: If you have just a specific version of python installed on your system, you can test like this:
```shell
$ tox -e py311 # test with python 3.11
```

### Pull Requests

If everything work fine you can create your pull request.

Before ensure you have [squash your commits](http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html).

> Be sure to submit your pull request on the upstream `master` branch!

You can create your pull request manually directly from github:
* Include examples, outputs, etc... whenever possible.
* Include screenshots and animated GIFs in your pull request whenever possible.

### Deploy emploo on PyPi

```
pip install --editable ".[dev]"
python -m build
twine check dist/*
twine upload dist/*
```
