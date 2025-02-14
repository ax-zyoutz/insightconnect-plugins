import sys
import os
from komand_proofpoint_tap.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_proofpoint_tap.connection.schema import Input
import json
import logging

sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.SERVICE_PRINCIPAL: {"secretKey": "44d88612-fea8-a8f3-6de8-2e1278abb02f"},
                Input.SECRET: {"secretKey": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"

            def json(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if kwargs.get("json"):
            urls = kwargs.get("json", {}).get("urls")
            if len(urls) == 1:
                return MockResponse("decode_single_url", 200)
            if len(urls) == 2:
                return MockResponse("decode_few_urls", 200)

        threat_id = kwargs.get("params", {}).get("threatId")
        campaign_id = kwargs.get("params", {}).get("campaignId")
        include_campaign_forensics = kwargs.get("params", {}).get("includeCampaignForensics")
        interval = kwargs.get("params", {}).get("interval")
        threat_type = kwargs.get("params", {}).get("threatType")
        threat_status = kwargs.get("params", {}).get("threatStatus")
        window = kwargs.get("params", {}).get("window")
        page = kwargs.get("params", {}).get("page")

        if window and page == 1:
            return MockResponse("top_clickers", 200)
        if window and page == 2:
            return MockResponse("top_clickers_empty_users", 200)
        if interval == "2021-08-24T14:00:00/2021-08-24T15:00:00":
            return MockResponse("delivered_messages_without_time_start", 200)
        if interval == "2021-08-24T13:00:00/2021-08-24T14:00:00":
            return MockResponse("delivered_messages_without_time_end", 200)
        if interval == "2021-08-24T12:00:00/2021-08-24T13:00:00" and threat_status == "falsePositive":
            return MockResponse("delivered_messages_without_subject", 200)
        if interval == "2021-08-24T12:00:00/2021-08-24T13:00:00" and threat_status == "cleared":
            return MockResponse("delivered_messages_cleared_status", 200)
        if interval == "2021-08-24T12:00:00/2021-08-24T13:00:00" and threat_status == "active":
            return MockResponse("delivered_messages_active_status", 200)
        if interval == "2021-08-24T12:00:00/2021-08-24T13:00:00":
            return MockResponse("delivered_messages", 200)
        if interval == "2021-08-23T14:00:00/2021-08-23T15:00:00":
            return MockResponse("blocked_messages_without_time_start", 200)
        if interval == "2021-08-23T13:00:00/2021-08-23T14:00:00":
            return MockResponse("blocked_messages_without_time_end", 200)
        if interval == "2021-08-23T12:00:00/2021-08-23T13:00:00" and threat_status == "falsePositive":
            return MockResponse("blocked_messages_without_subject", 200)
        if interval == "2021-08-23T12:00:00/2021-08-23T13:00:00" and threat_status == "cleared":
            return MockResponse("blocked_messages_cleared_status", 200)
        if interval == "2021-08-23T12:00:00/2021-08-23T13:00:00" and threat_status == "active":
            return MockResponse("blocked_messages_active_status", 200)
        if interval == "2021-08-23T12:00:00/2021-08-23T13:00:00":
            return MockResponse("blocked_messages", 200)
        if interval == "2021-08-22T14:00:00/2021-08-22T15:00:00":
            return MockResponse("permitted_clicks_without_time_start", 200)
        if interval == "2021-08-22T13:00:00/2021-08-22T14:00:00":
            return MockResponse("permitted_clicks_without_time_end", 200)
        if interval == "2021-08-22T12:00:00/2021-08-22T13:00:00" and threat_status == "falsePositive":
            return MockResponse("permitted_clicks_without_url", 200)
        if interval == "2021-08-22T12:00:00/2021-08-22T13:00:00" and threat_status == "cleared":
            return MockResponse("permitted_clicks_cleared_status", 200)
        if interval == "2021-08-22T12:00:00/2021-08-22T13:00:00" and threat_status == "active":
            return MockResponse("permitted_clicks", 200)
        if interval == "2021-08-21T14:00:00/2021-08-21T15:00:00":
            return MockResponse("blocked_clicks_without_time_start", 200)
        if interval == "2021-08-21T13:00:00/2021-08-21T14:00:00":
            return MockResponse("blocked_clicks_without_time_end", 200)
        if interval == "2021-08-21T12:00:00/2021-08-21T13:00:00" and threat_status == "falsePositive":
            return MockResponse("blocked_clicks_without_url", 200)
        if interval == "2021-08-21T12:00:00/2021-08-21T13:00:00" and threat_status == "cleared":
            return MockResponse("blocked_clicks_cleared_status", 200)
        if interval == "2021-08-21T12:00:00/2021-08-21T13:00:00" and threat_status == "active":
            return MockResponse("blocked_clicks", 200)
        if interval == "2021-08-20T14:00:00/2021-08-20T15:00:00":
            return MockResponse("all_threats_without_time_start", 200)
        if interval == "2021-08-20T13:00:00/2021-08-20T14:00:00":
            return MockResponse("all_threats_without_time_end", 200)
        if threat_status == "cleared" and threat_type == "url":
            return MockResponse("all_threats_cleared_status", 200)
        if threat_status == "active":
            return MockResponse("all_threats_active_status", 200)
        if not threat_type and not threat_status and interval:
            return MockResponse("all_threats", 200)
        if threat_id == "blacklisted_as_boolean_and_integer":
            return MockResponse("forensics_blacklisted_as_boolean_and_integer", 200)
        if threat_id == "blacklisted_as_boolean":
            return MockResponse("forensics_blacklisted_as_boolean", 200)
        if threat_id == "blacklisted_as_integer":
            return MockResponse("forensics_blacklisted_as_integer", 200)
        if campaign_id and not threat_id:
            return MockResponse("campaign_id", 200)
        if threat_id and not campaign_id and include_campaign_forensics is True:
            return MockResponse("threat_id_and_include_campaign_forensic", 200)
        if threat_id and not campaign_id and include_campaign_forensics is False:
            return MockResponse("threat_id_without_include_campaign_forensic", 200)
        return MockResponse("error", 404)
