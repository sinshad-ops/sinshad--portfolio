# Worked Cases — Synthetic Visual Evaluation

These cases use actual repository records. Decisions are provisional or geometry-derived as stated; they are not completed human reviews.

## Case 1: `scene-001`
**Input/evidence:** How many circles are visible?

**Candidate/output:** 3

**Rubric applied:** Question type: count; exact answer

**QC:** Image exists and contains non-background pixels

**Decision:** gold=3

**Explicit evidence/rationale:** Rendering metadata contains 3 non-overlapping circle components.

## Case 2: `scene-002`
**Input/evidence:** Which named color appears most often? If tied, use the leftmost object's color.

**Candidate/output:** amber

**Rubric applied:** Question type: dominant_color; exact answer

**QC:** Image exists and contains non-background pixels

**Decision:** gold=amber

**Explicit evidence/rationale:** Object color counts are {'amber': 2, 'red': 1, 'green': 1}; deterministic leftmost tie rule applies.

## Case 3: `scene-003`
**Input/evidence:** Is the first blue shape left of the final purple shape?

**Candidate/output:** no

**Rubric applied:** Question type: left_right; exact answer

**QC:** Image exists and contains non-background pixels

**Decision:** gold=no

**Explicit evidence/rationale:** x coordinates are 50 and 43.
