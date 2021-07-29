#!/usr/bin/env python3

from github import Github
import argparse
from repo_collector import RepoCollector


def main():
    parser = argparse.ArgumentParser("Collect Github repositories by uer")
    parser.add_argument("-u", "--users", required=True, nargs="+")
    parser.add_argument("-t", "--token", required=True)
    parser.add_argument("-l", "--layers", required=False, type=int)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    collector = RepoCollector(args.token)
    for user in args.users:
        collector.add_user(user)
    if args.layers:
        for _ in range(args.layers):
            collector.fetch_connections()
    if args.verbose:
        print("Included users: {}".format(", ".join(collector.users)))
    collector.fetch_repos()
    collector.download_repos(progress=args.verbose)


if __name__ == "__main__":
    main()
