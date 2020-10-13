from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url, logger):
        self.base_url = base_url
        self.logger = logger

    def _request(self, method, location, status_code=200, params=None, data=None):
        url = urljoin(self.base_url, location)

        self.logger.info('Performing request:')
        self.logger.info(f'URL: {url}')
        self.logger.info(f'PARAMS: {params}')
        self.logger.info(f'BODY: {data}')
        self.logger.info('-' * 20 + '\n')

        response = requests.request(method, url, params=params, data=data)

        self.logger.info('Got response:')
        self.logger.info(f'Status code: {response.status_code}')
        self.logger.info(f'Content: {response.text}')
        self.logger.info('-' * 50 + '\n')

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')

        return response.json()

    def get_users(self):
        location = 'users'
        return self._request('GET', location)

    def get_posts(self, users_id: int = None):
        location = 'posts'

        params = {}
        if users_id is not None:
            params['userId'] = users_id

        return self._request('GET', location, params=params)

    def post_posts(self, title, body, user_id):
        location = 'posts'
        body = {'title': title, 'body': body, 'userId': user_id}

        return self._request('POST', location, status_code=201, data=body)

    def post_posts_failed(self, title, body, user_id):
        location = 'postsssssssssssss'
        body = {'title': title, 'body': body, 'userId': user_id}

        return self._request('POST', location, status_code=404, data=body)

    def delete_posts(self, post_id):
        location = f'posts/{post_id}'
        return self._request('DELETE', location)
