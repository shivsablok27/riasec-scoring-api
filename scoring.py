from schemas import RiasecResponse, RiasecScore

def calculate_riasec_score(response: RiasecResponse) -> RiasecScore:
    """
    This function takes the user's 48 responses and calculates the final RIASEC scores.
    """
    
    # 1. Calculate raw sums for each category
    # We add up the 8 responses for each personality type (R, I, A, S, E, C)
    raw_scores = {
        "R": sum([response.R1, response.R2, response.R3, response.R4, response.R5, response.R6, response.R7, response.R8]),
        "I": sum([response.I1, response.I2, response.I3, response.I4, response.I5, response.I6, response.I7, response.I8]),
        "A": sum([response.A1, response.A2, response.A3, response.A4, response.A5, response.A6, response.A7, response.A8]),
        "S": sum([response.S1, response.S2, response.S3, response.S4, response.S5, response.S6, response.S7, response.S8]),
        "E": sum([response.E1, response.E2, response.E3, response.E4, response.E5, response.E6, response.E7, response.E8]),
        "C": sum([response.C1, response.C2, response.C3, response.C4, response.C5, response.C6, response.C7, response.C8]),
    }

    # 2. Normalize scores to a 0-1 range
    # The minimum possible sum is 8 (if user answered 1 to all 8 questions)
    # The maximum possible sum is 40 (if user answered 5 to all 8 questions)
    # The range is 40 - 8 = 32
    # Formula: (Raw Score - Min Score) / Range
    scores = {k: round((v - 8) / 32, 2) for k, v in raw_scores.items()}

    # 3. Sort the categories by score (Highest to Lowest)
    # This helps us find the dominant personality types
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    
    # 4. Get top 3 types for the Holland Code (e.g., "RIA")
    top_3 = [item[0] for item in sorted_scores[:3]]
    holland_code = "".join(top_3)

    # Return the final result object
    return RiasecScore(scores=scores, holland_code=holland_code)
