from fastapi import FastAPI
from schemas import RiasecResponse, RiasecScore
from scoring import calculate_riasec_score

# Initialize the FastAPI application
# This is the main entry point for the API server
app = FastAPI(
    title="RIASEC Scoring API",
    description="API to calculate Holland Code (RIASEC) from user responses.",
    version="1.0.0"
)

# Define the POST endpoint for scoring
# This function handles requests sent to http://.../score
# It expects a JSON body matching the RiasecResponse schema
@app.post("/score", response_model=RiasecScore)
def get_score(response: RiasecResponse):
    """
    Calculate RIASEC score and Holland Code from 48 user responses.
    Input: 48 integer ratings (1-5)
    Output: Normalized scores (0-1) and the 3-letter Holland Code
    """
    # Pass the user's responses to the calculation logic in scoring.py
    return calculate_riasec_score(response)

# Define a simple root endpoint to check if the API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the RIASEC Scoring API. Use /score to get your Holland Code."}
