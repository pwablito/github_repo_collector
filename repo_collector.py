from github import Github
import pygit2
import os
import shutil


class RepoCollector:
    def __init__(self, token, download_dir):
        self.download_dir = download_dir
        self.token = token
        self.g = Github(token)
        self.users = set()
        self.repos = []

    def add_user(self, username):
        self.users.add(username)

    def fetch_connections(self):
        users = self.users.copy()
        for username in users:
            for user in self.g.get_user(username).get_following():
                self.users.add(user.login)
            for user in self.g.get_user(username).get_followers():
                self.users.add(user.login)

    def fetch_repos(self):
        for user in self.users:
            for repo in self.g.get_user(user).get_repos():
                self.repos.append(repo)

    def download_repos(self, progress=True):
        os.mkdir(self.download_dir)
        for i in range(len(self.repos)):
            if (progress):
                print("Downloading repo {} of {}: {}/{}".format(i + 1, len(self.repos), self.repos[i].owner.login, self.repos[i].name))
            repo = self.repos[i]
            destination = os.path.join(self.download_dir, repo.owner.login, repo.name)
            if os.path.exists(destination):
                shutil.rmtree(destination)
            pygit2.clone_repository(repo.clone_url, destination)
