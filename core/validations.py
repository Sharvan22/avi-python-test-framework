from utils.logger import logger

def find_virtual_service(vservices, target_name):
    for vs in vservices:
        if vs.get("name") == target_name:
            return vs
    raise Exception("Target Virtual Service not found")

def pre_validate(vs):
    if vs.get("enabled") is not True:
        raise Exception("Virtual Service is not enabled")
    logger.info("Pre-validation passed (VS is enabled)")

def post_validate(client, uuid):
    vs = client.get(f"/api/virtualservice/{uuid}")
    if vs.get("enabled") is not False:
        raise Exception("Post-validation failed")
    logger.info("Post-validation passed (VS disabled)")
