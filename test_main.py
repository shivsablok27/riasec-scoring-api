from fastapi.testclient import TestClient
from main import app
from schemas import RiasecResponse

# Create a test client to simulate requests to our API
client = TestClient(app)

def test_read_main():
    """
    Test the root endpoint ("/") to ensure the API is up and running.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the RIASEC Scoring API. Use /score to get your Holland Code."}

def test_score_realistic():
    """
    Test Case 1: Realistic Dominance
    We simulate a user who LOVES Realistic tasks (all 5s) and HATES everything else (all 1s).
    Expected Result: 
    - Holland Code starts with "R"
    - "R" score is 1.0 (Maximum)
    """
    # Create a response where Realistic scores are high (5) and others are low (1)
    data = {
        "R1": 5, "R2": 5, "R3": 5, "R4": 5, "R5": 5, "R6": 5, "R7": 5, "R8": 5, # Total: 40 -> Normalized: 1.0
        "I1": 1, "I2": 1, "I3": 1, "I4": 1, "I5": 1, "I6": 1, "I7": 1, "I8": 1, # Total: 8  -> Normalized: 0.0
        "A1": 1, "A2": 1, "A3": 1, "A4": 1, "A5": 1, "A6": 1, "A7": 1, "A8": 1, # Total: 8  -> Normalized: 0.0
        "S1": 1, "S2": 1, "S3": 1, "S4": 1, "S5": 1, "S6": 1, "S7": 1, "S8": 1, # Total: 8  -> Normalized: 0.0
        "E1": 1, "E2": 1, "E3": 1, "E4": 1, "E5": 1, "E6": 1, "E7": 1, "E8": 1, # Total: 8  -> Normalized: 0.0
        "C1": 1, "C2": 1, "C3": 1, "C4": 1, "C5": 1, "C6": 1, "C7": 1, "C8": 1, # Total: 8  -> Normalized: 0.0
    }
    response = client.post("/score", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["holland_code"].startswith("R")
    assert result["scores"]["R"] == 1.0

def test_score_mixed():
    """
    Test Case 2: Mixed Scores
    We simulate a user with varied interests to check the calculation logic.
    - R: All 5s (Total 40 -> 1.0)
    - I: All 4s (Total 32 -> 0.75)
    - A: All 3s (Total 24 -> 0.50)
    - Others: Low
    Expected Result: Holland Code "RIA"
    """
    # Test a mixed case
    data = {}
    for i in range(1, 9):
        data[f"R{i}"] = 5
        data[f"I{i}"] = 4
        data[f"A{i}"] = 3
        data[f"S{i}"] = 2
        data[f"E{i}"] = 1
        data[f"C{i}"] = 1
    
    response = client.post("/score", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["holland_code"] == "RIA"
    assert result["scores"]["R"] == 1.0
    assert result["scores"]["I"] == 0.75
    assert result["scores"]["A"] == 0.5
