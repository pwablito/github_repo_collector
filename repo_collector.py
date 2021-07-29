from github import Github
import pygit2
import os


class RepoCollector:
    def __init__(self, token):
        self.token = token
        self.g = Github(token)
        self.users = set()
        self.repos = []

    def fetch_connections(self, username):
        for user in self.g.get_user(username).get_following():
            self.users.add(user.login)
        for user in self.g.get_user(username).get_followers():
            self.users.add(user.login)

    def fetch_repos(self):
        for user in self.users:
            for repo in self.g.get_user(user).get_repos():
                self.repos.append(repo)

    def download_repos(self):
        for repo in self.repos:
            pygit2.clone_repository(repo.clone_url, os.path.join("downloads", repo.owner.login, repo.name))
