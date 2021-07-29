#!/usr/bin/env python3

from github import Github
import argparse


def main():
	parser = argparse.ArgumentParser("Collect Github repositories by uer")
	parser.add_argument("-u", "--user", required=True)
	parser.add_argument("-t", "--token", required=True)
	args = parser.parse_args()
	g = Github(args.token)
	for repo in g.get_user().get_repos():
    		print(repo.name)

if __name__ == "__main__":
	main()

