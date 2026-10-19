# Findings and decision implications

The visual dataset contains 120 unique rendered PNGs and 240 synthetic answer records. The actual RGB-pixel baseline correctly answers 54/60 eligible questions (90.0%), with 50.0% coverage and 60 abstentions.

The baseline reads image pixels for counts, color frequency and bar height. Ground truth is generated from rendering geometry; scene metadata is not used to predict answers. Abstentions cover spatial/absence/UI tasks unsupported by this baseline. Performance on simple colored components says nothing about photographs, real charts, OCR or a vision-language model. Six color-order failures in the eligible subset expose limitations of the leftmost tie heuristic on multi-row layouts.

## Next validation step
Blind human review of the source evidence, followed by adjudication and a new unseen benchmark.
