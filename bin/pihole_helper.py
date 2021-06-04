
# encoding = utf-8

import os
import sys
import time
import datetime
import json
import pihole_constants as const


def sendit(pihole_host, event_name, helper, params=None, payload=None):
    """Send Request

    :param pihole_host: Pihole server to query
    :param event_name: Name of event performing the request
    :param helper: Splunk Helper
    :param params: Parameters for request
    :param payload: Payload to send with request
    :return: response
    """
    # Skip run if too close to previous run interval
    if not checkpointer(pihole_host, event_name, helper):
        return False

    helper.log_info(
        f'event_name="{event_name}", msg="starting {event_name} collection", hostname="{pihole_host}"')

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json'
    }
    url = f'{const.h_proto}://{pihole_host}/{const.api_system}'

    # Get Proxy Information
    proxy = helper.get_proxy()
    if proxy:
        if proxy["proxy_username"]:
            helper.log_info('msg="Proxy is configured with authenticaiton"')
            helper.log_debug(
                f'proxy_type="{proxy["proxy_type"]}", proxy_url="{proxy["proxy_url"]}", proxy_port="{proxy["proxy_port"]}", proxy_username="{proxy["proxy_username"]}"')
        else:
            helper.log_info('msg="Proxy is configured with no authentication"')
            helper.log_debug(
                f'proxy_type="{proxy["proxy_type"]}", proxy_url="{proxy["proxy_url"]}", proxy_port="{proxy["proxy_port"]}"')

    try:
        helper.log_info(
            f'event_name="{event_name}", msg="starting http request", action="starting", hostname="{pihole_host}"')
        r = helper.send_http_request(
            url, 'get', headers=headers, parameters=params, payload=payload, use_proxy=True)
    except Exception as e:
        helper.log_error(
            f'event_name="{event_name}", error_msg="Unable to complete request", action="failed", hostname="{pihole_host}"')
        helper.log_debug(
            f'event_name="{event_name}", hostname="{pihole_host}", error_msg="{e}"')
        return False

    if r.status_code == 200:
        helper.log_info(
            f'event_name="{event_name}", msg="request completed", action="success", hostname="{pihole_host}"')
        return r.json()
    else:
        helper.log_error(
            f'event_name="{event_name}", error_msg="Unable to retrieve information", action="failed", hostname="{pihole_host}"')
        helper.log_debug(
            f'event_name="{event_name}", hostname="{pihole_host}", status_code="{r.status_code}"')
        return False


def checkpointer(pihole_host, event_name, helper, set_checkpoint=False):
    """Checks and returns checkpoint

    :param pihole_host: Host to check for checkpointer
    :param event_name: Name of the event
    :param helper: Splunk Helper
    :param set_checkpoint: Whether to set a new checkpoint
    :return: bool
    """
    # Get Interval
    interval = int(helper.get_arg('interval'))
    current_time = int(time.time())
    check_time = current_time - interval + 60
    key = f'{pihole_host}_{event_name}'

    if set_checkpoint:
        new_state = int(time.time())
        helper.save_check_point(key, new_state)
        helper.log_info(
            f'msg="Updating Checkpoint", checkpoint="{new_state}", hostname="{pihole_host}", event_name="{event_name}"')
        return True

    if helper.get_check_point(key):
        old_state = int(helper.get_check_point(key))
        helper.log_info(
            f'event_name="{event_name}", msg="Checkpoint found", hostname="{pihole_host}"')
        helper.log_debug(
            f'event_name="{event_name}", msg="Checkpoint information", checkpoint="{old_state}", interval="{interval}", hostname="{pihole_host}"')

        if check_time < old_state:
            helper.log_info(
                f'event_name="{event_name}", msg="Skipping because interval is too close to previous run", '
                f'action="aborted", hostname="{pihole_host}"')
            return False
        else:
            helper.log_info(
                f'event_name="{event_name}", msg="Running scheduled Interval", hostname="{pihole_host}"')

    else:
        helper.log_info(
            f'event_name="{event_name}", msg="Checkpoint file not found", hostname="{pihole_host}"')

    return True
