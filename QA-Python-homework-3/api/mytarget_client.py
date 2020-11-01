from urllib.parse import urljoin
import requests
import json


class MytargetClient():

    def __init__(self, credentials, logger):
        self.base_url = 'https://target.my.com/'
        self.session = requests.Session()
        self.email = credentials['email']
        self.password = credentials['password']
        self.logger = logger
        self.login()

    def _request(self, method, url=None, params=None,
                 location=None, headers=None,
                 data=None, json=None):
        if location:
            url = urljoin(self.base_url, location)
        self.logger.info('Performing request:')
        self.logger.info(f'URL: {url}')
        self.logger.info(f'PARAMS: {params}')
        self.logger.info(f'BODY: {data}')
        self.logger.info('-' * 20 + '\n')

        response = self.session.request(method=method, url=url,
                                        headers=headers, params=params,
                                        data=data)
        response.raise_for_status()
        self.logger.info('Got response:')
        self.logger.info(f'Status code: {response.status_code}')
        self.logger.info(f'Content: {response.text}')
        self.logger.info('-' * 50 + '\n')

        if json:
            return response.json()
        return response.text

    def login(self):
        auth_url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.email,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login'
                        '%3D1%26ignore_opener%3D1#email',
            'failure': "https://account.my.com/login/"
        }

        self._request(method='POST', url=auth_url, data=data, headers=headers)
        self.csrf_token = self.get_token()

    def get_token(self):
        headers = {
            'Referer':
                'https://target.my.com/auth/mycom?state=target_login%3D1'
        }
        self._request(method='GET', location='csrf', headers=headers)
        return self.session.cookies.get('csrftoken')

    def exists(self, segment_id):
        segment_list_url = "https://target.my.com/api/v2/remarketing" \
                           "/segments.json?fields=id&limit=100&_={time.time()}"
        response = self._request(method='GET', url=segment_list_url)
        return f'"id": {segment_id}' in response

    def create_segment(self, name='Test'):
        url = 'https://target.my.com/api/v2/remarketing/segments.json'

        params = {"fields": "relations__object_type,relations__object_id,"
                            "relations__params,relations_count,id,name,"
                            "pass_condition,created,campaign_ids,users,flags"
                  }

        data = json.dumps({
            "name": name,
            "pass_condition": 1,
            "logicType": "or",
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }
            ]
        })

        headers = {
            "Content-Type": "application/json",
            "Referer": "https://target.my.com/segments/segments_list/new",
            'X-CSRFToken': self.csrf_token
        }
        response = self._request(method="POST", url=url,
                                 data=data, params=params,
                                 headers=headers, json=True)
        return response.get('id')

    def segment_remove(self, segment_id):
        url = "https://target.my.com/api/v2/remarketing/segments/" \
              f"{segment_id}.json"

        headers = {
            "Referer": "https://target.my.com/segments/segments_list",
            'X-CSRFToken': self.csrf_token
        }

        self._request(method="DELETE",
                      url=url,
                      headers=headers)
        return True
