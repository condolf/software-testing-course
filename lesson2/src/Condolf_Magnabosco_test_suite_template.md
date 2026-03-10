# TEST_SUITE_TEMPLATE.md — Manual Test Suite (PlanningPoker)

> **Fill this file during the lab.**  
> Do not modify the implementation code.

## Group Info

- **Date:** 2026-03-06  
- **Members:**
  - Davide Condolf
  - Federico Magnabosco

---

## Program Under Test (PUT)

- **Repository / Folder:**  
- **File:** `planning_poker.py`  
- **Method:** `identify_extremes(estimates)`

### Short description (in your own words)

Write 2–3 lines about what the method is supposed to do.

This method is supposed to read all the votes and selects the name of the 2 developers that voted 
the highest and lowest estimates in the set.
---

## Assumptions / Preconditions

List any assumptions you are making about inputs or environment (if none, write “None”).

- None 

---

## Test Suite

Fill the table below. Add more rows if needed.

> **Inputs format suggestion:** represent estimates as a list of pairs, e.g.  
> `[("Alice", 5), ("Bob", 3), ("Charlie", 8)]`

| ID   | Description        | Preconditions                                    | Inputs                            Expected Output       | Observed Output | Outcome (Pass/Fail) | Notes |-
|------|------------        |--------------                                    |--------                          |-----------------      |----------------|---------------------|------ |
| TC01 | Wrong Data Types   | String for names, Non negative int for estimates | [(1, 'Alice'), (2, 'Bob')]       | Datatype Error        | AttributeError |  Pass               |       |
| TC02 | All None estimates | String for names, Non negative int for estimates | [('Alice', None), ('Bob', None)] | ['Bob','Bob']         | AttributeError |  Fail               |       |
| TC03 | Negative estimates | String for names, Non negative int for estimates | [('Alice', -1), ('Bob', 4)]      | NegativeEstimateError | AttributeError |  Pass               |       |


---

## Notes on Oracles (Expected Output)

Explain briefly how you decided the expected outputs (your “oracle”):

With some "common sense" constraints like the non negativity of the estimates, 
so we can reasonably expect what the intended output is meant to be.
 

---

## Reflection (short)

Answer briefly (5–10 lines total):

1. What guided your choice of test cases?
2. How confident are you in the method after running (or reasoning about) your test suite?
3. What would you test next if you had more time?
#
1. We wanted to find the most common edge cases that usually end up in errors, 
  like negative values, not intended values (None) ecc.
  TC01 instead checks how the system reacts if the inputs are swapped (Name <-> Estimate)
2. We think that with some input processing to check the data types this function can behave correctly.
3. Some test cases to see how the program reacts to omonyms, since by the static analisys it doesn't seem to check for already existing names.
  
