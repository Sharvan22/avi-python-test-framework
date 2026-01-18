from core.prefetcher import prefetch_resources
from core.validations import find_virtual_service, pre_validate, post_validate
from mocks.ssh import mock_ssh
from mocks.rdp import mock_rdp
from utils.logger import logger

def run_testcase(client, testcase):
    logger.info(f"Running test case: {testcase['name']}")

    mock_ssh()
    mock_rdp()

    vservices = prefetch_resources(client)

    vs = find_virtual_service(vservices, testcase["target_vs_name"])
    uuid = vs["uuid"]

    pre_validate(vs)

    logger.info("Disabling Virtual Service...")
    client.put(f"/api/virtualservice/{uuid}", {"enabled": False})

    post_validate(client, uuid)
