# Actual BANKING77 results

Official train/test: 10,003/3,080 queries; 77 published intents.
Training-only validation: 8,505 fit / 1,498 validation; alpha selected=0.1.

| Model | Official-test accuracy | Macro-F1 |
|---|---:|---:|
| Majority (training frequency) | 1.30% | 0.0003 |
| Word unigram+bigram multinomial NB | 85.88% | 0.8579 |

Correct top-1 predictions: 2645/3080. Top-3 accuracy: 95.16%.

## Duplicate/leakage audit
7 normalized texts occur in both official splits, affecting 7 test rows.
Secondary test excluding train-overlapping texts: 3073 rows, accuracy 85.84%, macro-F1 0.8575. The official split remains intact.
Duplicate extra rows: {'train': 4, 'test': 1}. Conflicting-label groups flagged: 0.
No labels or rows were silently corrected or removed. The fit/validation split groups equal normalized text to prevent within-training leakage.

## Failure evidence
435 prediction/reference disagreements; 535 cases require review because of disagreement or low uncalibrated confidence.
Weakest intents by measured F1:
- `contactless_not_working`: F1 0.545; support 40
- `card_not_working`: F1 0.660; support 40
- `top_up_failed`: F1 0.705; support 40
- `declined_card_payment`: F1 0.737; support 40
- `pending_transfer`: F1 0.743; support 40

Largest measured confusion pairs:
- `contactless_not_working` → `card_not_working`: 12 cases
- `card_payment_not_recognised` → `direct_debit_payment_not_recognised`: 6 cases
- `fiat_currency_support` → `exchange_via_app`: 6 cases
- `pending_transfer` → `transfer_timing`: 6 cases
- `failed_transfer` → `beneficiary_not_allowed`: 5 cases

The published label is a reference, not infallible gold. Incorrect predictions may reflect lexical overlap, subtle distinctions, out-of-vocabulary words or ambiguous labels. These are hypotheses for human review, not completed manual adjudications.

## Limits
- Single banking domain, English only; no evidence for Malayalam, sentiment, entity spans, safety or multilingual generalization.
- Simple lexical classifier; no transformer or production-service evaluation.
- The probabilities are uncalibrated. Coverage tables describe a sensitivity analysis, not guaranteed precision.
- A reused public test set does not demonstrate novelty or deployment readiness.
- Data collection and original annotation were done by the published dataset authors, not the portfolio owner.
- This implementation/documentation was AI-assisted. No personal human annotation score is claimed.

![Measured results](benchmark.png)

## Worked disagreement examples (not manually adjudicated)

### banking77:test:00000
> How do I locate my card?
Published: `card_arrival`; predicted: `get_physical_card`.
Uncalibrated confidence: 0.999. Human rationale and corrected-label fields remain blank.

### banking77:test:00005
> When will I get my card?
Published: `card_arrival`; predicted: `card_delivery_estimate`.
Uncalibrated confidence: 0.915. Human rationale and corrected-label fields remain blank.

### banking77:test:00011
> How long does a card delivery take?
Published: `card_arrival`; predicted: `card_delivery_estimate`.
Uncalibrated confidence: 0.999. Human rationale and corrected-label fields remain blank.

### banking77:test:00020
> I did not get my card yet, is it lost?
Published: `card_arrival`; predicted: `getting_virtual_card`.
Uncalibrated confidence: 0.686. Human rationale and corrected-label fields remain blank.

### banking77:test:00022
> How long should my new card take to arrive?
Published: `card_arrival`; predicted: `card_delivery_estimate`.
Uncalibrated confidence: 0.726. Human rationale and corrected-label fields remain blank.
