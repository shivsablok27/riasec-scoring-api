from pydantic import BaseModel, Field, validator
from typing import Dict

# This file defines the "Shape" of the data we expect to receive and send.

class RiasecResponse(BaseModel):
    """
    This model represents the input data from the user.
    It expects 48 integer fields, one for each question.
    Each field must be between 1 (Dislike) and 5 (Enjoy).
    """
    
    # Realistic (Doers)
    R1: int = Field(..., ge=1, le=5, description="Test the quality of parts before shipment")
    R2: int = Field(..., ge=1, le=5, description="Lay brick or tile")
    R3: int = Field(..., ge=1, le=5, description="Work on an offshore oil-drilling rig")
    R4: int = Field(..., ge=1, le=5, description="Assemble electronic parts")
    R5: int = Field(..., ge=1, le=5, description="Operate a grinding machine")
    R6: int = Field(..., ge=1, le=5, description="Fix a broken faucet")
    R7: int = Field(..., ge=1, le=5, description="Assemble products in a factory")
    R8: int = Field(..., ge=1, le=5, description="Install flooring")

    # Investigative (Thinkers)
    I1: int = Field(..., ge=1, le=5, description="Study the structure of the human body")
    I2: int = Field(..., ge=1, le=5, description="Conduct biological research")
    I3: int = Field(..., ge=1, le=5, description="Study the behavior of whales")
    I4: int = Field(..., ge=1, le=5, description="Work in a biology lab")
    I5: int = Field(..., ge=1, le=5, description="Make a map of the bottom of the ocean")
    I6: int = Field(..., ge=1, le=5, description="Conduct drug research")
    I7: int = Field(..., ge=1, le=5, description="Study the stars")
    I8: int = Field(..., ge=1, le=5, description="Study the history of the universe")

    # Artistic (Creators)
    A1: int = Field(..., ge=1, le=5, description="Conduct a musical choir")
    A2: int = Field(..., ge=1, le=5, description="Direct a play")
    A3: int = Field(..., ge=1, le=5, description="Write a script for a movie or television show")
    A4: int = Field(..., ge=1, le=5, description="Write a novel")
    A5: int = Field(..., ge=1, le=5, description="Create special effects for movies")
    A6: int = Field(..., ge=1, le=5, description="Paint sets for plays")
    A7: int = Field(..., ge=1, le=5, description="Compose a song")
    A8: int = Field(..., ge=1, le=5, description="Play a musical instrument")

    # Social (Helpers)
    S1: int = Field(..., ge=1, le=5, description="Give career guidance to people")
    S2: int = Field(..., ge=1, le=5, description="Do volunteer work at a non-profit organization")
    S3: int = Field(..., ge=1, le=5, description="Help people who have problems with drugs or alcohol")
    S4: int = Field(..., ge=1, le=5, description="Teach a high-school class")
    S5: int = Field(..., ge=1, le=5, description="Help people with family-related problems")
    S6: int = Field(..., ge=1, le=5, description="Supervise the activities of children at a camp")
    S7: int = Field(..., ge=1, le=5, description="Teach an individual how to read")
    S8: int = Field(..., ge=1, le=5, description="Help elderly people with their daily activities")

    # Enterprising (Persuaders)
    E1: int = Field(..., ge=1, le=5, description="Sell restaurant franchises to individuals")
    E2: int = Field(..., ge=1, le=5, description="Sell merchandise at a department store")
    E3: int = Field(..., ge=1, le=5, description="Manage the operations of a hotel")
    E4: int = Field(..., ge=1, le=5, description="Operate a beauty salon or barber shop")
    E5: int = Field(..., ge=1, le=5, description="Manage a department within a large company")
    E6: int = Field(..., ge=1, le=5, description="Manage a clothing store")
    E7: int = Field(..., ge=1, le=5, description="Sell houses")
    E8: int = Field(..., ge=1, le=5, description="Run a toy store")

    # Conventional (Organizers)
    C1: int = Field(..., ge=1, le=5, description="Generate the payroll for a company")
    C2: int = Field(..., ge=1, le=5, description="Inventory supplies using a hand-held computer")
    C3: int = Field(..., ge=1, le=5, description="Use a computer program to generate customer bills")
    C4: int = Field(..., ge=1, le=5, description="Maintain employee records")
    C5: int = Field(..., ge=1, le=5, description="Compute and record statistical and other numerical data")
    C6: int = Field(..., ge=1, le=5, description="Operate a calculator")
    C7: int = Field(..., ge=1, le=5, description="Handle a customer's bank deposit")
    C8: int = Field(..., ge=1, le=5, description="Keep shipping and receiving records")

    # Example configuration for API documentation (Swagger UI)
    model_config = {
        "json_schema_extra": {
            "example": {
                "R1": 5, "R2": 5, "R3": 5, "R4": 5, "R5": 5, "R6": 5, "R7": 5, "R8": 5,
                "I1": 1, "I2": 1, "I3": 1, "I4": 1, "I5": 1, "I6": 1, "I7": 1, "I8": 1,
                "A1": 1, "A2": 1, "A3": 1, "A4": 1, "A5": 1, "A6": 1, "A7": 1, "A8": 1,
                "S1": 1, "S2": 1, "S3": 1, "S4": 1, "S5": 1, "S6": 1, "S7": 1, "S8": 1,
                "E1": 1, "E2": 1, "E3": 1, "E4": 1, "E5": 1, "E6": 1, "E7": 1, "E8": 1,
                "C1": 1, "C2": 1, "C3": 1, "C4": 1, "C5": 1, "C6": 1, "C7": 1, "C8": 1
            }
        }
    }

class RiasecScore(BaseModel):
    """
    This model represents the output data sent back to the user.
    """
    scores: Dict[str, float] # A dictionary of normalized scores (e.g., {"R": 0.8, "I": 0.2})
    holland_code: str        # The top 3 personality types (e.g., "RIA")
