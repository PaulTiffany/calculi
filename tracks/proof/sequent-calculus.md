# Track — Sequent Calculus: Proof as a Calculus

## Need

How can deduction itself become the object of a formal transformation system?

Gentzen's sequent calculi answer by making inferential contexts explicit.

## World

A sequent has the schematic form
\[
\Gamma\vdash\Delta,
\]
where \(\Gamma\) and \(\Delta\) are collections or sequences of formulas, depending on the system.

Intuitively, the left side records assumptions and the right side records conclusions or alternatives justified from them.

## Primitive

The key objects are:

- formulas;
- contexts;
- sequents;
- inference rules.

Logical connectives are governed by rules for how they enter or leave relevant positions in a sequent.

## Move — inference rule

A proof is a tree of rule applications.

For example, a rule may transform premises containing \(A\) and \(B\) into a conclusion containing \(A\land B\).

The characteristic motion is not numerical change but **licensed derivation**.

## Cut

One of the central structural ideas is the cut rule: roughly, if one derivation establishes an intermediate formula and another uses it, the derivations can be composed through that formula.

Gentzen's cut-elimination theorem shows, for his systems, that proofs using cuts can be transformed into cut-free proofs.

That makes **proof normalization itself** a kind of computation.

## Why this matters for the atlas

Sequent calculus makes a point that classical-calculus intuition can obscure:

> a calculus can be about valid transformation rather than quantity.

This prepares the conceptual ground for λ-reduction and process transition systems.

## Relation to natural deduction

**Historical/formal sibling relation.**

Gentzen developed both natural-deduction and sequent calculi to analyze proof.

They organize inferential structure differently.

## Relation to λ-calculus

Through Curry–Howard-style correspondences, proof normalization and program reduction can be related very deeply.

But a particular correspondence must be stated precisely; “proofs are programs” is a slogan until the types, logic, and translation are named.

## Sources

- Gerhard Gentzen, foundational papers on natural deduction and sequent calculus, 1934–35.
- Stanford Encyclopedia of Philosophy, “Natural Deduction Systems in Logic.”
- Stanford Encyclopedia of Philosophy, “Proof Theory.”
