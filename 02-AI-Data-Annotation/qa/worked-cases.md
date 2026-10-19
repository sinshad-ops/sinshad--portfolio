# Worked Cases — Multi-task AI Data Annotation

These cases use actual repository records. Decisions are provisional or geometry-derived as stated; they are not completed human reviews.

## Case 1: `A1`
**Input/evidence:** I was charged twice for the same monthly plan, and the second charge appeared after I had already canceled. Please review the duplicate payment and return the extra amount. I appreciate the quick service normally, but this billing issue is making me uneasy.

**Candidate/output:** topic=billing; sentiment=mixed; urgency=medium

**Rubric applied:** Exact categorical labels plus exact entity spans

**QC:** No structural warning

**Decision:** accept reference for provisional benchmark

**Explicit evidence/rationale:** AI-authored provisional annotation: the dominant request concerns a duplicate charge and possible billing correction.

## Case 2: `A2`
**Input/evidence:** I cannot sign in after changing my password yesterday. The reset link says it has expired immediately, even when I request a fresh one. Could someone check whether my account is locked? I need access before my next scheduled shipment, but it is not an emergency.

**Candidate/output:** topic=account; sentiment=negative; urgency=medium

**Rubric applied:** Exact categorical labels plus exact entity spans

**QC:** No structural warning

**Decision:** accept reference for provisional benchmark

**Explicit evidence/rationale:** AI-authored provisional annotation: the primary actionable need is restoring account access rather than changing a shipment.

## Case 3: `A3`
**Input/evidence:** The tracking page has shown “label created” since Monday, and the package still has not moved. This was supposed to arrive for a class project. Can you confirm whether it is actually with the carrier or arrange another delivery option?

**Candidate/output:** topic=delivery; sentiment=negative; urgency=high

**Rubric applied:** Exact categorical labels plus exact entity spans

**QC:** No structural warning

**Decision:** accept reference for provisional benchmark

**Explicit evidence/rationale:** AI-authored provisional annotation: the dominant issue is a stalled shipment and the requested resolution concerns delivery status or replacement.
