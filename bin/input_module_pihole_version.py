
# encoding = utf-8

from pihole_helper import *
import pihole_constants as const
import json


def validate_input(helper, definition):
    # We have nothing left to verify
    pass


def collect_events(helper, ew):
    log_level = helper.get_log_level()
    helper.set_log_level(log_level)
    helper.log_info(f'log_level="{log_level}"')

    event_name = 'pihole_version'
    pihole_host = helper.get_arg('pihole_account')['pihole_host']
    response = sendit(pihole_host, event_name, helper,
                      endpoint=const.api_version)

    if not response:
        return False

    splunk_event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(
    ), sourcetype=helper.get_sourcetype(), data=json.dumps(response), host=pihole_host)
    ew.write_event(splunk_event)

    checkpointer(pihole_host, event_name, helper, set_checkpoint=True)
