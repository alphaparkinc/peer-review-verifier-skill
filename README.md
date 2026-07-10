# genpark-peer-review-verifier-skill

> **GenPark AI Agent Skill** -- Proof-of-work peer reference validator.

## Quick Start

```python
from client import PeerReviewVerifierClient
client = PeerReviewVerifierClient()
res = client.verify_references(["He writes Python"], ["Python"])
print(res["verified_skills_score"])
```
