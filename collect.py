#!/usr/bin/env python3

from github import Github
import argparse
from repo_collector import RepoCollector


def main():
    parser = argparse.ArgumentParser("Collect Github repositories by uer")
    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-t", "--token", required=True)
    args = parser.parse_args()

    collector = RepoCollector(args.token)

    collector.fetch_connections(args.user)
    collector.fetch_repos()
    collector.download_repos()


if __name__ == "__main__":
    main()
