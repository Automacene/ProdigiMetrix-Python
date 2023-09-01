from prodigi_metrix.resources.basic import Basic
from prodigi_metrix.resources.keyword import Keyword
import asyncio

plugin_id = "79904822928323603"
auth_token = "3be39ab97e5ef62f16b068057190143420c8c2ed9c31996837f68595a85bc3b9"

def main():
    try:
        basic = Basic(plugin_id, auth_token)
        response = asyncio.run(basic.log_now())
        assert response.status_code == 200
    except AssertionError:
        print(f"Basic test failed: status code was {response.status_code}")
    except Exception as e:
        print(f"Basic test failed: {e}")

    try:
        keyword = Keyword(plugin_id, auth_token)
        response = asyncio.run(keyword.log_now(["test"]))
        assert response.status_code == 200
    except AssertionError:
        print(f"Keyword test failed: status code was {response.status_code}")
    except Exception as e:
        print(f"Keyword test failed: {e}")

    try:
        metrics = basic.get()
        assert metrics.status_code == 200
        assert metrics.json()["plugin_name"] == "ProdigiLink Video"
        print(metrics.json())
    except AssertionError:
        print(f"Basic get test failed: status code was {metrics.status_code}")

    try:
        metrics = keyword.get()
        assert metrics.status_code == 200
        assert metrics.json()["plugin_name"] == "ProdigiLink Video"
        print(metrics.json())
    except AssertionError:
        print(f"Keyword get test failed: status code was {metrics.status_code}")

    print("All tests passed.")
    
if __name__ == "__main__":
    main()