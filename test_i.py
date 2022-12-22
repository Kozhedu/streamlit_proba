from fastapi.testclient import TestClient
from i import app

client = TestClient(app)

def test_read_predict_positive():
    response = client.post("/predict/",
        json={"text": " Я всех люблю"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'