# encoding = utf-8

from hashlib import sha256
import pihole_constants as const
import json


class PHAuth:
    """Authentication for Pi-hole Server

    Required Params
    ---------------
    :param host: Pi-hole host to query
    :param password: password to authenticate
    :param helper: helper
    """

    def __init__(self, host, password, helper):
        self.host = host
        self.password = b'password'
        self.helper = helper

    def __call__(self):
        pwhash = sha256(sha256(self.password).hexdigest().encode(
            'ascii')).hexdigest().encode('ascii')
        event_name = 'authentication'
        url = f'{const.h_proto}://{self.host}/{const.api_auth}'
        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }

        try:
            r = self.helper.send_http_request(
                url, 'get', headers=headers, use_proxy=True)
        except Exception as e:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to complete request", action="failed", hostname="{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", error_msg="{e}"')
            return False

        if r.status_code == 200:
            self.helper.log_info(
                f'event_name="{event_name}", msg="request completed", action="success", hostname="{self.host}"')
            request = r.json()
            challenge = request['challenge'].encode('ascii')
            response = sha256(challenge + b':' +
                              pwhash).hexdigest().encode('ascii')
        else:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to retrieve information", action="failed", hostname="{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", status_code="{r.status_code}"')
            return False

        try:
            event_name = f'{event_name}:session'
            s = self.helper.send_http_request(
                url, 'post', headers=headers, payload={'response': response}, use_proxy=True)

        except Exception as e:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to complete request", action="failed", hostname="{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", error_msg="{e}"')
            return False

        if s.status_code == 200:
            session = s.json()

            if session['session']['valid'] and session['session']['sid'] != 'null':
                return session['session']['sid']
        else:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to retrieve information", action="failed", hostname="{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", status_code="{r.status_code}"')
            return False
