import github.GithubObject
from github import Github

USERNAME = USERNAME
PASSWORD = PASSWORD

Github_users = {Planiouser: githubuser}

def is_str(a):
    return type(a) == str


class Ticket:
    def __init__(self, title='', body='', assignee=github.GithubObject.NotSet
                 , milestone=github.GithubObject.NotSet, labels=github.GithubObject.NotSet, state=''):
        self.title = title
        self.body = body
        self.assignee = assignee
        self.milestone = milestone
        self.state = state
        self.labels = labels

    def __str__(self):
        str = 'TICKET' + '\n' + self.title + '\n' + self.body + '\n' + self.created_at + '\n' + self.closed_at + '\n'\
              + self.updated_at + '\n' + self.assignee + '\n' + self.milestone + '\n'\
              + self.state + '\n' + self.labels[0] + '\n'
        return str

    def handle_labels(self, df_value):
        if 'MasterBox' in df_value:
            self.labels = ['MasterBox']

    def handle_link(self, df_value):
        self.body = f'Original ticket link: https://vayyar.plan.io/issues/{df_value} \n\n {self.body}'

    def handle_state(self, df_value):
        if df_value != 'Solved':
            self.state = 'copy'
        else:
            self.state = 'not_copy'

    def handle_title(self, df_value):
        if is_str(df_value):
            self.title = df_value

    def handle_assignee(self, df_value):
        if is_str(df_value):
            self.assignee = Github_users[df_value]

    def handle_description(self, df_value):
        if is_str(df_value):
            self.body = f'{df_value} \n {self.body}'

    def handle_type(self, df_value):
        if is_str(df_value):
            self.body = f'{self.body} Type: {df_value} \n'

    def handle_version(self, df_value):
        if is_str(df_value):
            self.body = f'{self.body} SW version: {df_value} \n'

    def handle_release_found(self, df_value):
        if is_str(df_value):
            self.body = f'{self.body} Release found: {df_value} \n'

    def handle_commit_found(self, df_value):
        if is_str(df_value):
            self.body = f'{self.body} commit found: {df_value} \n'

    def handle_milestone(self, df_value):
        if is_str(df_value):
            self.body = f'{self.body} milestone: {df_value} \n'

    def create_github_issue(self):
        repo = None

        g = Github(USERNAME, PASSWORD)
        for repo in g.get_user().get_repos():
            if repo.name == repo_name:
                break

        if self.state == 'copy':
            title = self.title
            body = self.body
            assignee = self.assignee
            labels = self.labels

            repo.create_issue(title=title, body=body, assignee=assignee, labels=labels)
            print(f'created {self.title}')

