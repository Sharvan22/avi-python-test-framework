from concurrent.futures import ThreadPoolExecutor
from utils.yaml_loader import load_yaml
from core.auth import register_and_login
from core.api_client import APIClient
from executor.runner import run_testcase

def main():
    config = load_yaml("config/config.yaml")
    testcases = load_yaml("config/testcases.yaml")["testcases"]

    token = register_and_login(
        config["api"]["base_url"],
        config["auth"]["username"],
        config["auth"]["password"]
    )

    client = APIClient(config["api"]["base_url"], token)

    with ThreadPoolExecutor(max_workers=2) as executor:
        for tc in testcases:
            executor.submit(run_testcase, client, tc)

if __name__ == "__main__":
    main()
