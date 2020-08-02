import logging

import requests


logger = logging.getLogger(__name__)


class RequestsClient:

    def get(self, url, params=None, api_key=None):
        if api_key:
            headers = {'X-Auth-Token': api_key}
        else:
            headers = None

        response = requests.get(
            url,
            params=params,
            headers=headers,
        )

        if not response.ok:
            logger.error(
                'Error calling %s status_code:%s response:%s',
                url, response.status_code, response.text,
            )
            return None

        return response.json()
