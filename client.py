"""
peer-review-verifier-skill: Client SDK
Evaluates peer references to extract skill validation levels and filter out generic fluff.
"""
from __future__ import annotations
from typing import Optional


class PeerReviewVerifierClient:
    """
    SDK for recruiting reference verification.
    """

    def verify_references(
        self,
        peer_feedbacks: list[str],
        candidate_skills: list[str],
    ) -> dict:
        feedbacks_lower = [f.lower() for f in peer_feedbacks]
        
        verified = {}
        fluff_detected = 0

        for skill in candidate_skills:
            s_low = skill.lower()
            matching_mentions = 0
            
            for f in feedbacks_lower:
                if s_low in f:
                    matching_mentions += 1
                if "amazing" in f or "great guy" in f or "pleasure" in f:
                    fluff_detected += 1

            if matching_mentions >= 2:
                verified[skill] = "highly_verified"
            elif matching_mentions == 1:
                verified[skill] = "partially_verified"
            else:
                verified[skill] = "unverified"

        # Calculate authenticity score (more specific skill mentions vs generic praise fluff)
        total_mentions = sum(1 for v in verified.values() if v != "unverified")
        denom = max(1, total_mentions + fluff_detected)
        authenticity = round(total_mentions / denom, 2)

        return {
            "verified_skills_score": verified,
            "authenticity_score": authenticity,
            "credibility_grade": "A" if authenticity >= 0.7 else "B" if authenticity >= 0.4 else "C"
        }
