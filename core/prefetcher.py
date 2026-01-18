from utils.logger import logger

def prefetch_resources(client):
    tenants = client.get("/api/tenant")
    vservices = client.get("/api/virtualservice")
    engines = client.get("/api/serviceengine")

    logger.info(f"Tenants found: {len(tenants)}")
    logger.info(f"Virtual Services found: {len(vservices)}")
    logger.info(f"Service Engines found: {len(engines)}")

    return vservices
