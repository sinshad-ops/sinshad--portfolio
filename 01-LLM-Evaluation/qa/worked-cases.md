# Worked Cases — LLM Pairwise Evaluation

These cases use actual repository records. Decisions are provisional or geometry-derived as stated; they are not completed human reviews.

## Case 1: `L1`
**Input/evidence:** Calculate the total cost and state the calculation.

Source context:
A community center is buying notebooks for a workshop. There are 7 packs, and each pack contains 8 notebooks. Each notebook costs $3. The supplier applies no discount, tax, delivery fee, or other charge. The organizer asks for the total cost of all notebooks, not the number of notebooks. All quantities are whole numbers, and the stated unit price applies equally to every notebook.

**Candidate/output:** A: The center will receive 56 notebooks because 7 packs × 8 notebooks equals 56. At $3 per notebook, the total is 56 × 3 = $168. Therefore, the total purchase cost is $168, excluding no additional charges because none are listed.
B: The total is $21. This multiplies the 7 packs by the $3 price and treats each pack as one priced unit. The 8 notebooks per pack affects the quantity received, but it does not affect the stated total under the supplier’s pricing.

**Rubric applied:** Pairwise accuracy, instruction following, helpfulness, clarity

**QC:** Provisional=A; AI judge=A

**Decision:** A

**Explicit evidence/rationale:** Candidate A correctly calculates 7 × 8 = 56 notebooks and 56 × $3 = $168. Candidate B gives the wrong total by multiplying packs directly by the unit price.

## Case 2: `L2`
**Input/evidence:** Determine which proposed appointment complies with the scheduling constraints.

Source context:
A clinic schedules intake calls only on Tuesdays between 9:00 a.m. and 12:00 p.m. The call must last 30 minutes, and the patient cannot attend before 10:00 a.m. or after 11:00 a.m. A proposed appointment is Tuesday at 11:00 a.m. The clinic treats an appointment ending exactly at noon as within the allowed window. No other scheduling constraints are provided, and the question asks whether this particular proposal is acceptable.

**Candidate/output:** A: The appointment is not acceptable because it starts at the latest time the patient can attend. The clinic should choose 10:30 a.m. instead so there is more flexibility before the noon cutoff.
B: The appointment is acceptable. It starts at 11:00 a.m., which is not after the patient’s 11:00 a.m. limit, and a 30-minute call ends at 11:30 a.m., within the clinic’s Tuesday 9:00 a.m. to noon window.

**Rubric applied:** Pairwise accuracy, instruction following, helpfulness, clarity

**QC:** Provisional=B; AI judge=B

**Decision:** B

**Explicit evidence/rationale:** Candidate B correctly applies both the patient's attendance limits and the clinic's operating window. Candidate A incorrectly treats starting at 11:00 a.m. as impermissible.

## Case 3: `L3`
**Input/evidence:** Extract the product names that are marked as backordered.

Source context:
The inventory note lists four products and statuses: Cedar mug — in stock; Harbor lamp — backordered; Linen throw — discontinued; Orchard tray — backordered. The note says that “backordered” means orders may be placed but shipment is delayed. Product names should be reproduced as written, without adding categories, quantities, or interpretations. The requested output is the names of all and only the products whose status exactly matches “backordered.”

**Candidate/output:** A: The backordered products are Harbor lamp and Orchard tray. The Cedar mug is in stock, while the Linen throw is discontinued, so neither belongs in the requested list.
B: The backordered products are Harbor lamp, Linen throw, and Orchard tray. The discontinued item is included because discontinued products are also unavailable for immediate shipment.

**Rubric applied:** Pairwise accuracy, instruction following, helpfulness, clarity

**QC:** Provisional=A; AI judge=A

**Decision:** A

**Explicit evidence/rationale:** Candidate A extracts exactly the two products marked backordered. Candidate B adds a product based on an unsupported interpretation rather than matching the exact status.
