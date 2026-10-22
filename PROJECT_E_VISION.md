# Project E — Vision and Non-Claims

**Version:** 0.1 (Gate 0 draft)  
**Date:** 2026-10-23  
**Status:** proposed; not approved  
**Repository:** frozen at `e75be96`; this document lives outside the tracked tree

---

## 1. Original ambition

Project E investigates whether a physically valid energy core can be discovered or engineered that delivers unusually high useful power and/or stored energy per unit mass and volume, with credible efficiency, thermal management, lifetime, cost, and safety.

The fictional Arc Reactor is an **ambition and a compactness metaphor**, not a specification, a proof of feasibility, or a target geometry. No claim in this program may rest on fiction.

The scientific question is:

> **What is the best physically permitted energy source, conversion pathway, and system architecture for a defined mission, and can any underexplored combination produce a measurable system-level improvement over the best incumbent?**

“Best” is always conditional on a declared mission, system boundary, evidence level, and time horizon.

---

## 2. Three categories that must never be conflated

| Category | Definition | Required declaration | Example |
|---|---|---|---|
| **Storage** | Energy is bought externally and delivered later | Charging source, round-trip efficiency, depth of discharge, self-discharge | Li-ion pack, flywheel, thermal store |
| **Conversion** | A declared energy flow is converted from one form to another | Input source, input energy, every stage efficiency, waste heat | TPV, TEG, ORC, thermionic, motor/generator |
| **Generation** | A declared primary source is consumed or converted continuously | Fuel/source mass or heat, replenishment, complete energy balance | Diesel genset, fuel cell, fission reactor, solar array |

A converter with an external heat supply is **not** a generator. A battery is **not** a source. A solar panel is a converter of an external source, not a compact fuel.

No architecture may claim net energy output without an accounted source. A claim of “self-sustaining” operation requires a closed, independently verified energy balance, including startup, standby, control, and auxiliary power.

---

## 3. What Project E is not claiming

- It is not claiming that the Arc Reactor is real or buildable.
- It is not claiming that a 35 kg, 6 kW, 8 h self-contained core is possible.
- It is not claiming that a simulation proves a device works.
- It is not claiming that a patent proves feasibility.
- It is not claiming that a negative result is a failure.
- It is not claiming that cost estimates are quotations.
- It is not claiming that a laboratory demonstration is field qualification.
- It is not claiming that “new physics” is needed or available.

---

## 4. What success looks like

A successful program produces one or more of:

1. A verified map of what physics permits and what it forbids.
2. A reproducible negative result: a class of architectures that cannot meet a declared mission.
3. A measured component or system improvement that survives independent review.
4. A clear decision to stop, revise, or continue a research path.
5. A published record of failed hypotheses and why they failed.

A breakthrough is a possible outcome, not a promised deliverable.

---

## 5. What failure looks like

- A headline number that omits source, cooling, shielding, converter, fuel, or balance of plant.
- A model presented as a measurement.
- A cost estimate presented as a quotation.
- A hypothesis retained after its falsification test failed.
- A program that continues because it was funded, not because evidence supports it.
- A “new mechanism” that is a renamed existing technology or a conservation violation.

---

## 6. Program structure

| Track | Scope | Does not do |
|---|---|---|
| **A — Baseline** | Preserve and audit the eight-architecture benchmark | Dictate the discovery mission |
| **B — Landscape** | Map sources, converters, storage, limits, and evidence | Select a winner |
| **C — Hypotheses** | Build a diverse, quantitative shortlist | Run expensive simulations |
| **D — Models** | Verify and validate models for shortlisted candidates | Claim a device works |
| **E — Experiments** | Run the smallest falsifiable test | Start with hardware |
| **F — Translation** | Packaging, cost, manufacturing, safety, IP | Override scientific conclusions |

The benchmark mission (M1: 10 kWh over 8 h — 1.25 kW average — 6 kW pulse, 35 kg / 60 L / $5,000 / $0.40 per kWh) is retained as **one provisional case**, not as the definition of Project E. The repository config’s “1 kW continuous” wording gives 8 kWh; the 8 vs 10 kWh ambiguity is audit finding D16 and must be resolved before Gate 3.

---

## 7. Decision rules

1. No architecture is selected before Gate 3.
2. No experiment starts before Gate 5 and a safety review.
3. No E2 value without a DOI/datasheet and page/figure locator.
4. No cost ranking based only on E0 prices.
5. No model without an analytical reference and a verification test.
6. No positive claim without an uncertainty statement.
7. No negative result is deleted.
8. A gate is complete only with the stated evidence.

---

## 8. Gate 0 acceptance

This vision is accepted when the owner confirms:

- [ ] The benchmark is preserved as Track A, not the whole program.
- [ ] Storage, conversion, and generation are separate categories.
- [ ] The Arc Reactor is treated only as ambition.
- [ ] A negative result is an acceptable outcome.
- [ ] No architecture is selected before Gate 3.
- [ ] The program may stop if evidence does not support continuation.
