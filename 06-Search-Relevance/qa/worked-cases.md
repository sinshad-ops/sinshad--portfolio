# Worked Cases — Search Relevance Evaluation

These cases use actual repository records. Decisions are provisional or geometry-derived as stated; they are not completed human reviews.

## Case 1: `S1`
**Input/evidence:** Kerala tourism official itinerary planner

**Candidate/output:** Kerala Tourism Itinerary Planner — A fictional local planning tool for organizing routes, stays, and attractions across Kerala. — relevance 3
Kerala Backwaters Travel Guide — Overview of houseboats, lakes, and popular backwater destinations. — relevance 2
Goa Weekend Route Builder — A fictional route-planning guide for short trips in Goa. — relevance 1
Kerala School Examination Calendar — A calendar of fictional school examination dates. — relevance 0

**Rubric applied:** 0–3 relevance; NDCG gain 2^rel−1

**QC:** intent=navigational; locale=en-IN

**Decision:** compare lexical order with ideal judged order

**Explicit evidence/rationale:** Exact navigational query for a Kerala tourism planning resource; prioritize the matching corpus page over general travel articles.

## Case 2: `S2`
**Input/evidence:** how to fix Python list index out of range

**Candidate/output:** Python IndexError: List Bounds Explained — Explains zero-based indexing, length checks, and safe iteration patterns. — relevance 3
Debugging Python Dictionary KeyError — Covers missing keys and dictionary access techniques. — relevance 1
Python Lists and Slices Tutorial — Introduces list creation, slicing, and common list operations. — relevance 2
Java Array Bounds Reference — Discusses bounds errors in Java arrays. — relevance 0

**Rubric applied:** 0–3 relevance; NDCG gain 2^rel−1

**QC:** intent=informational; locale=en-IN

**Decision:** compare lexical order with ideal judged order

**Explicit evidence/rationale:** The user seeks an explanation and debugging guidance for a common Python exception.

## Case 3: `S3`
**Input/evidence:** തിരുവനന്തപുരം ജില്ലാ കലക്ടറേറ്റ് സേവനങ്ങൾ

**Candidate/output:** തിരുവനന്തപുരം ജില്ലാ കലക്ടറേറ്റ് സേവന പോർട്ടൽ — ജില്ലാ ഓഫീസുമായി ബന്ധപ്പെട്ട സാങ്കൽപ്പിക സേവനങ്ങളും അപേക്ഷാ വിവരങ്ങളും. — relevance 3
കേരളത്തിലെ ജില്ലാ ഭരണകൂടം — കേരളത്തിലെ ജില്ലാ ഭരണസംവിധാനത്തെക്കുറിച്ചുള്ള പൊതുവിവരം. — relevance 2
കൊല്ലം ജില്ലാ കലക്ടറേറ്റ് — കൊല്ലം ജില്ലയിലെ ഒരു സാങ്കൽപ്പിക ഭരണ ഓഫീസ് രേഖ. — relevance 1
തിരുവനന്തപുരം നഗരത്തിലെ മ്യൂസിയങ്ങൾ — നഗരത്തിലെ സാംസ്കാരിക കേന്ദ്രങ്ങളുടെ പട്ടിക. — relevance 0

**Rubric applied:** 0–3 relevance; NDCG gain 2^rel−1

**QC:** intent=navigational; locale=ml-IN

**Decision:** compare lexical order with ideal judged order

**Explicit evidence/rationale:** Exact Malayalam navigational query for services associated with the Thiruvananthapuram district collectorate.
