# encoding = utf-8

from hashlib import sha256
import pihole_constants as const


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
        self.password = password
        self.helper = helper

    def start_session(self):
        """Start a new session

        :return: Session Id (sid)
        """
        event_name = 'authentication'
        self.helper.log_info(f'event_name="{event_name}", msg="starting challenge response authentication", '
                             f'action="starting"')

        # hash password
        pwhash = sha256(sha256(self.password.encode('UTF-8')).hexdigest().encode(
            'ascii')).hexdigest().encode('ascii')

        # Construct URL
        url = f'{const.h_proto}://{self.host}:{const.p_port}/{const.api_auth}'

        # JSON headers
        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }

        # Get Challenge
        try:
            self.helper.log_info(f'event_name="{event_name}", msg="retrieving auth challenge"')
            r = self.helper.send_http_request(url, 'get', headers=headers, use_proxy=True)
        except Exception as e:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Failed to get challenge", action="failed", hostname='
                f'"{self.host}"')
            self.helper.log_debug(f'event_name="{event_name}", hostname="{self.host}", error_msg="{e}"')
            return False

        if r.status_code == 200:
            self.helper.log_info(
                f'event_name="{event_name}", msg="successfully obtained challenge from server", action="success", '
                f'hostname="{self.host}"')
            request = r.json()
            challenge = request['challenge'].encode('ascii')
            response = sha256(challenge + b':' + pwhash).hexdigest().encode('ascii')
        else:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to retrieve challenge from server", action="failed", '
                f'hostname="{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", status_code="{r.status_code}"')
            return False

        # Send Challenge Response
        try:
            event_name = f'{event_name}:session'
            self.helper.log_info(f'event_name="{event_name}", msg="sending challenge response"')
            s = self.helper.send_http_request(
                url, 'post', headers=headers, payload={'response': response}, use_proxy=True)

        except Exception as e:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to obtain challenge response", action="failed", '
                f'hostname='
                f'"{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", error_msg="{e}"')
            return False

        if s.status_code == 200:
            self.helper.log_info(f'event_name="{event_name}", msg="successfully created session", action="success"')
            session = s.json()

            if session['session']['valid'] and session['session']['sid'] != 'null':
                return session['session']['sid']
        else:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to retrieve session", action="failed", hostname='
                f'"{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", status_code="{r.status_code}"')
            return False
