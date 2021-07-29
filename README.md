# Github Repo Collector

A tool to download Github repositories by user

To use this tool, you will need a Github access token. For more information on how to get one, see [Github's documentation](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)


## Installation
First, install dependencies:
`python3 -m pip install --user -r requirements.txt`

## Usage
To run, use `./collect.py`:

```
usage: Collect Github repositories by user [-h] -u USERS [USERS ...] -t TOKEN [-l LAYERS] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -u USERS [USERS ...], --users USERS [USERS ...]
  -t TOKEN, --token TOKEN
  -l LAYERS, --layers LAYERS
  -v, --verbose
```

Author: Paul Spencer
