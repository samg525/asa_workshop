# Day 1
## Best Practices
[Table of some python best practices](<best practices.png>)
## Project Structure
A way to setup project directories:
```bash
├── README.md          <- Description of this project
├── bin                <- Your compiled code can be stored here (not tracked by git)
├── config             <- Configuration files, e.g., for sphinx or for your model if needed
├── data               <- Data used by your project (not tracked by git)
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final data sets for analysis.
│   └── raw            <- The original, immutable data dump.
├── docs               <- Documentation, e.g., sphinx or reference papers (not tracked by git)
├── env                <- Python environment specific to this project
├── notebooks          <- Jupyter or R notebooks
├── reports            <- For a manuscript source, e.g., LaTeX, Markdown, etc., or any project reports
│   └── figures        <- Figures for the manuscript or reports
└── src                <- Source code for this project
    ├── external       <- Any external source code, e.g., pull other git projects libraries
    └── tools          <- Any helper scripts go here
```
## Coding Style
- use functions
- use pylint or blax?

Structuring code
- use a 'shebang' a ```python #!``` line like ```python #! /usr/bin/env python``` on the first line
- a docstring for this module (if it’s a module, see later)
- import all the modules/clasess/functions that you need (and no more)
- global (static) variables
- define classes
- define functions
- a main() function if you use one
- an if __name__ clause if you want one
These rules mean no code is in global scope.

## Python Packages
A good structure is:
```bash
├── README.md          <- Description of this project
├── LICENSE.md         <- License for others to re use your work
├── requirements.txt   <- python dependency management
├── setup.py           <- for installing your module
├── docs               <- (dir) documentation for your module
├── mymodule           <- (dir) code for your module
|   └── data           <- (dir) data bundled with your module
├── scripts            <- (dir) scripts for users to interact with
└── tests              <- (dir) test for your module
```

```python __name__``` is name of current module
The top level file you run gets given the __name__ '__main__' so we can check if a file is the top one.

To find info on installing and making packages go to: https://packaging.python.org/en/latest/
Google isn't reliable.
Blog post by pip developer explaining the difference between setup.py and requirements.txt: https://web.archive.org/web/20130723114307/https://caremad.io/blog/setup-vs-requirements/

pipe your current setup into a file requirements.txt
pip list --format=freeze > requirements.txt

Can then install the packages somewhere else and it helps with reproducability
pip install requirements.txt

If you have the right structure in your repository on github (see later), then pip can install directly from github using the following: pip install git+https://github.com/[user]/[repo].git

You can even select a branch by appending @branchname to the github link, or @commit-id to select a particular commit.

Can write executables with python. Need to run chmod +x <filename>

Youtube video with a physical demo of the git repository: https://www.youtube.com/watch?v=1ffBJ4sVUb4

## Git things
Making a new branch
```bash
git branch feature-1
git checkout feature-1
```
or
```bash
git checkout -b feature-1
```
Always want to merge changes into main. So checkout to main then 
```bash
git merge feature-1
```
To use pull requests, commit things on a branch, push the branch then go to github website and make a pull request.

To delete a branch
```bash
git branch -d <branch name>
```

Lowercase ```-d``` won't force it and will warn you if there's errors. Upper case ```-D``` will force the delete.

A pretty way of looking at the git history/log is 
```bash
git log --graph --decorate --oneline
```
Can also get extensions like git graph instead.