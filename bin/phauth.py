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
        self.password = password
        self.helper = helper
        self.sid = None
        self.url = f'{const.h_proto}://{self.host}:{const.p_port}/{const.api_auth}'
        self.headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }

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


        # Get Challenge
        try:
            self.helper.log_info(f'event_name="{event_name}", msg="retrieving auth challenge"')
            r = self.helper.send_http_request(self.url, 'get', headers=self.headers, use_proxy=True)
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
            response = str(sha256(challenge + b':' + pwhash).hexdigest().encode('ascii')).lstrip('b\'').rstrip('\'')
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
            payload = {
                'response': response
            }
            self.helper.log_info(f'event_name="{event_name}", msg="sending challenge response"')
            s = self.helper.send_http_request(
                self.url, 'post', headers=self.headers, payload=json.dumps(payload), use_proxy=True)

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

            self.helper.log_info(f'event_name="{event_name}", msg="session status", isValid='
                                 f'"{session["session"]["valid"]}"')
            if session['session']['valid']:
                self.sid = session['session']['sid']
            else:
                return False
        else:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to retrieve session", action="failed", hostname='
                f'"{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", status_code="{s.status_code, s.reason}"')
            return False

    def logout(self):
        """Logout of Session"""
        event_name = 'authentication:logout'
        self.helper.log_info(f'event_name="{event_name}", msg="Logging out of session"')
        self.headers['sid'] = self.sid
        try:
            l = self.helper.send_http_request(
                self.url, 'delete', headers=self.headers, use_proxy=True)
        except Exception as e:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to Logout", action="failed", '
                f'hostname='
                f'"{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", error_msg="{e}"')
            return False

        if l.status_code == 410:
            self.helper.log_info(f'event_name="{event_name}", msg="Logging out successful", action="success"')
            return True
        else:
            self.helper.log_error(
                f'event_name="{event_name}", error_msg="Unable to Logout", action="failed", '
                f'hostname='
                f'"{self.host}"')
            self.helper.log_debug(
                f'event_name="{event_name}", hostname="{self.host}", error_msg="{l.status_code} {l.reason}"')
            return False


