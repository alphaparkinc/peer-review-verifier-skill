"""
example_usage.py -- Demonstrates PeerReviewVerifierClient
"""
from client import PeerReviewVerifierClient

def main():
    client = PeerReviewVerifierClient()
    result = client.verify_references(
        peer_feedbacks=[
            "He has strong Python coding skills and worked on data models.",
            "Great guy to work with. Absolute pleasure.",
            "Yes, he developed the backend Python API and managed SQL queries."
        ],
        candidate_skills=["Python", "SQL", "Project Management"]
    )
    print("[Peer Review Verification Result]")
    print(f"Skills Scored: {result['verified_skills_score']}")
    print(f"Trust: {result['authenticity_score']} (Grade: {result['credibility_grade']})")

if __name__ == "__main__":
    main()
