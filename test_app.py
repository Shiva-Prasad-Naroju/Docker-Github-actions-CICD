from app import app
def test_home():
    response = app.test_client().get("/")
    
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello World"  # ✅ Convert bytes to string
