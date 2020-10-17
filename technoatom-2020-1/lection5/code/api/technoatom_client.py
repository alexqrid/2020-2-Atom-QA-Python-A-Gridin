from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class TechnoatomClient:

    def __init__(self, user, password):
        self.base_url = 'https://technoatom.mail.ru'

        self.session = requests.Session()
        self.csrf_token = None

        self.user = user
        self.password = password
        self.login()

    def _request(self, method, location, status_code=200, headers=None, params=None, data=None, json=True):
        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, params=params, data=data)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')

        if json:
            json_response = response.json()

            if json_response.get('bStateError'):
                error = json_response['sErrorMsg']
                raise RequestErrorException(f'Request "{url}" dailed with error "{error}"!')
            return json_response
        return response

    def get_token(self):
        location = 'pages/index/'
        headers = self._request('GET', location, json=False).headers
        return headers['Set-Cookie'].split(';')[0].split('=')[-1]

    def login(self):
        location = 'login/'

        csrf_token = self.get_token()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': f'csrftoken={csrf_token}'
        }

        data = {
            'csrfmiddlewaretoken': csrf_token,
            'login': self.user,
            'password': self.password
        }

        response = self._request('POST', location, headers=headers, data=data, json=False)
        cookies = response.headers['Set-Cookie'].split(';')
        new_csrf_token = [c for c in cookies if c.startswith('csrftoken=')][0].split('=')[-1]
        session_id_gtp = [c for c in cookies if 'secure, sessionid_gtp=' in c][0].split('=')[-1]

        self.csrf_token = new_csrf_token
        self.session.cookies = cookiejar_from_dict({'csrftoken': new_csrf_token, 'sessionid_gtp': session_id_gtp})

        return response.json()

    def get_feed(self, feed_type='my'):
        location = 'feed/update/stream/'
        params = {'type': feed_type}

        return self._request('GET', location, params=params)

    def post_topic(self, title, text, blog_id=299, publish=True):
        location = 'blog/topic/create/'

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {
            'csrfmiddlewaretoken': self.csrf_token,
            'title': title,
            'text': text,
            'blog': blog_id,
            'publish': 'on' if publish else ''
        }
        return self._request('POST', location, headers=headers, data=data)

    def delete_topic(self, topic_id):
        location = f'blog/topic/delete/{topic_id}/'

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {
            'csrfmiddlewaretoken': self.csrf_token,
            'submit': 'Удалить',
        }
        return self._request('POST', location, headers=headers, data=data, json=False)
