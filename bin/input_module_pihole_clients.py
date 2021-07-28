
# encoding = utf-8

from pihole_helper import *
import pihole_constants as const
from phauth import PHAuth
import json


def validate_input(helper, definition):
    # We have nothing to verify
    pass


def collect_events(helper, ew):
    event_name = 'pihole_clients'

    # Get Log Level
    log_level = helper.get_log_level()
    helper.set_log_level(log_level)
    helper.log_info(f'log_level="{log_level}"')

    # Authenticate
    s = PHAuth(helper)
    pihole_host = s.host
    s.start_session(event_name)

    if not s.sid:
        return False

    # Collect domain information
    response = sendit(pihole_host, event_name, helper,
                      endpoint=const.api_clients, sid=s.sid)

    # log out of current session
    s.logout(event_name)

    if response:
        for item in response['clients']:
            # Create Splunk Event
            splunk_event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(
            ), sourcetype=helper.get_sourcetype(), data=json.dumps(item), host=pihole_host)
            ew.write_event(splunk_event)

        # Checkpointer
        checkpointer(pihole_host, event_name, helper, set_checkpoint=True)
        return True
    else:
        return False