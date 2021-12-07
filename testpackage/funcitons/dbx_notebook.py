import requests


class DbxApi:
    def __init__(self, token, name):
        self.token = token
        self.name = name

    def notebook(self, path):
        job_payload = {
            "run_name": self.name,
            "existing_cluster_id": '1206-202358-eapp8gqr',
            "notebook_task":
                {
                    "notebook_path": path
                }
        }

        resp = requests.post('https://adb-4725571060990474.14.azuredatabricks.net/api/2.0/jobs/runs/submit', json=job_payload, headers={'Authorization': 'Bearer ' + self.token})
        return resp.text
