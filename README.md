# Japanese Higher Order Numbers

## What?
This is a Python script for converting large numbers into Japanese higher order numbers (命数法).

## Why?

In Japanese, the word you append to a large number changes for every 10^4 increase/decrease.

This differs from English, where the appended word changes for every 10^3 increase/decrease. Examples:
- 9  million  is 9000万  (kyu-sen-man)
- 90 million  is 9億     (kyu-oku)
- 9  trillion is 9兆     (kyu-chou)

Describing large numbers in Japanese can be difficult if you are used to the appended number-word changing every 3 decimal places like in English: million, billion, trillion. The script accepts a raw number and converts it to the Japanese 10^4 system, appending the correct higher-order numeric kanji.

## What else?

Supports appended Japanese words for numbers as large as 9999 x 10^64.

When the base number is less than 10, format to shows one decimal-place for a little more precision:
- Example: num_to_jp(12000) results in 1.2万

Rounding:
- num_to_jp(995000) results in 99万
- num_to_jp(995001) results in 100万

Optionally append any string via the second argument:
- Example: num_to_jp(1000000,"円") results in: 100万円

## Reference:
https://ja.wikipedia.org/wiki/%E5%91%BD%E6%95%B0%E6%B3%95
