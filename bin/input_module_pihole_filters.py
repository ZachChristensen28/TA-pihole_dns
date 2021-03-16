
# encoding = utf-8

import os
import sys
import time
import datetime
import json
from pihole_helper import *
import pihole_constants as const


def validate_input(helper, definition):
    # We have nothing to verify
    pass


def collect_events(helper, ew):
    # Get Credentials
    account = helper.get_arg('pihole_account')
    api_key = account['api_key']
    pihole_host = account['pihole_host']

    # Get Log Level
    log_level = helper.get_log_level()
    helper.set_log_level(log_level)
    helper.log_info(f'log_level="{log_level}"')

    # Start
    for filter in const.filters:
        params = {
            'auth': api_key,
            'list': filter
        }
        event_name = f'filters_{params["list"]}'
        response = sendit(pihole_host, event_name, helper, params)

        if response:
            for item in response['data']:
                item['filter_type'] = params['list']

                # Create Splunk Event
                splunk_event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(
                ), sourcetype=helper.get_sourcetype(), data=json.dumps(item), host=pihole_host)
                ew.write_event(splunk_event)

            # Checkpointer
            checkpointer(pihole_host, event_name, helper, set_checkpoint=True)
