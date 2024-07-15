import requests

url = "http://localhost:8080"
exp_id = "d54da7dd-0769-4361-be17-c255cb3c7412"
response = requests.get(
    f"{url}/pipeline/apis/v2beta1/experiments",
    cookies={
        "auth": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoxLCJsb2NhbGUiOiJ6aC10dyIsInZpZXdNb2RlIjoibW9zYWljIiwic2luZ2xlQ2xpY2siOmZhbHNlLCJwZXJtIjp7ImFkbWluIjp0cnVlLCJleGVjdXRlIjp0cnVlLCJjcmVhdGUiOnRydWUsInJlbmFtZSI6dHJ1ZSwibW9kaWZ5Ijp0cnVlLCJkZWxldGUiOnRydWUsInNoYXJlIjp0cnVlLCJkb3dubG9hZCI6dHJ1ZX0sImNvbW1hbmRzIjpbXSwibG9ja1Bhc3N3b3JkIjpmYWxzZSwiaGlkZURvdGZpbGVzIjpmYWxzZSwiZGF0ZUZvcm1hdCI6ZmFsc2V9LCJpc3MiOiJGaWxlIEJyb3dzZXIiLCJleHAiOjE3MjA2MDMyMzYsImlhdCI6MTcyMDU5NjAzNn0.hr2JbIkKpAM6pW2bSk75m_PFAYjM0OdFKEzV988ntgY",
        "authservice_session": "MTcyMTAxNjYxNnxOd3dBTkZaUlRETkxRbGREVDBKTVVEZFZUMWRaVms4eVNrOUpTVmd5V0ZGSFF6VkJXVUpYUWtkUE5ESlZURE5YTmtKR1VreGFOVUU9fLb4B2hb4rRTmHhFDIjsgunGx4vFkwVo6Ct0HGi_ESeh"
    },
    params={
        "namespace": "kubeflow-user-example-com"
    })
print(response.text)