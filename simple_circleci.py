import urllib
import requests
import json

"""
  here is a wrapper for the circleci API
  Built by Harper Reed (harper@nata2.org) - @harper
  git@github.com:harperreed/simple-circleci.git

"""


class simple_circleci:

    token = ''
    base_url = 'https://circleci.com/api/v1/'

    def __init__(self, token=None):
        self.token = token

    def make_request(self, url, params=None, method='GET', ):
        api_creds = {
            'circle-token': self.token,
        }
        params.update(api_creds)
        headers = {'Accept': 'application/json'}
        if params:
            params = urllib.urlencode(params, True).replace('+', '%20')
        if method == 'GET':
            r = requests.get(url, params=params, headers=headers)
        elif method == 'POST':
            r = requests.post(url, params=params, headers=headers)

        data = r.text
        response = json.loads(data)

        return response

    def me(self):
        url = self.base_url + "me"
        params = {}
        result = self.make_request(url=url, params=params, method='GET')
        return result

    def projects(self):
        url = self.base_url + "projects"
        params = {}
        result = self.make_request(url=url, params=params, method='GET')
        return result

    def recent_builds(self):
        url = self.base_url + "recent-builds"
        params = {}
        result = self.make_request(url=url, params=params, method='GET')
        return result

    def project(self, username, project):
        url = self.base_url + "project/" + username + "/" + project
        params = {}
        result = self.make_request(url=url, params=params, method='GET')
        return result

    def build(self, username, project, build_number):
        url = self.base_url + "project/" + username + "/" + project + "/" \
            + str(build_number)
        params = {}
        result = self.make_request(url=url, params=params, method='GET')
        return result

    def artifacts(self, username, project, build_number):
        url = self.base_url + "project/" + username + "/" + project + "/" \
            + str(build_number) + "/artifacts"
        params = {}
        result = self.make_request(url=url, params=params, method='GET')
        return result

    def build_retry(self, username, project, build_number, ssh=False):
        if ssh:
            url = self.base_url + "project/" + username + "/" + project + "/" \
                + str(build_number) + "/ssh"
        else:
            url = self.base_url + "project/" + username + "/" + project + "/" \
                + str(build_number) + "/retry"

        print url

        params = {}
        result = self.make_request(url=url, params=params, method='POST')
        return result

    def build_cancel(self, username, project, build_number):
        url = self.base_url + "project/" + username + "/" + project + "/" \
            + str(build_number) + "/cancel"
        params = {}
        result = self.make_request(url=url, params=params, method='POST')
        return result


if __name__ == "__main__":
    token = "your_api_key"
    username = "your_username"
    project = "your_project"
    build_number = 1
    api = simple_circleci(token=token)
    #print api.me()
    #print api.projects()
    #print api.recent_builds()
    #print api.project(username=username, project=project)
    #print api.build(username=username, project=project, build_number=build_number)
    #print api.artifacts(username=username, project=project, build_number=build_number)
    #print api.build_retry(username=username, project=project, build_number=build_number)
    #print api.build_cancel(username=username, project=project, build_number=build_number)
