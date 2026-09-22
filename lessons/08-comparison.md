# 08 — Comparing Calculi Without Flattening Them

A cosmology becomes dangerous when every formalism is forced into one story.

This lesson gives us a disciplined comparison method.

## 1. Compare primitives first

Ask what must exist before any rule can run.

| Calculus | Primitive emphasis |
|---|---|
| classical | varying quantities / local structure |
| λ | variables, abstraction, application |
| sequent | formulas in inferential contexts |
| π | processes and names |
| ρ | reflective process/name structure |
| indications | distinction / mark |
| distinction graphs | observer-indexed indistinguishability |
| Fuzzy | bounded observer interface and observer-relative differential structure |

Two systems that use similar arrows may still begin from different primitives.

## 2. Compare characteristic moves

| Calculus | Move |
|---|---|
| classical | differentiate / integrate |
| λ | β-reduce |
| sequent | infer by a rule |
| π | communicate / transition |
| ρ | communicate with reflective naming structure |
| indications | mark / simplify forms |
| distinction graph | construct/update indistinguishability relations |
| Fuzzy | differentiate/integrate through bounded observation and track residue |

## 3. Compare observables

A calculus needs some account of when two formal objects count as equivalent.

Examples include:

- same numerical value;
- α/β/η relations;
- logical derivability;
- bisimulation;
- same marked/unmarked form;
- same distinction structure;
- same observer-visible projection.

When moving between calculi, ask which equivalence is preserved.

## 4. Compare loss

Every translation deserves a loss ledger.

Suppose
\[
T:A\to B.
\]

Ask:

1. Is \(T\) injective?
2. Is it surjective?
3. Does it preserve reduction?
4. Does it preserve observations?
5. Does it preserve composition?
6. Can \(A\) be reconstructed?
7. What structure disappears?

This turns “these look similar” into a research program.

## 5. Example: λ and π

There are encodings of λ-style computation into π-calculus.

So a valid statement is:

> specified λ-computations can be represented by communicating π-processes under an explicit translation.

An invalid leap is:

> therefore λ-calculus and π-calculus are the same calculus.

The encoding tells us something deep precisely because their primitive pictures differ.

## 6. Example: π and ρ

ρ is π-like and reflective.

But the encoding history is subtle: later work found errors in an earlier encoding and repaired the result under carefully stated criteria.

Lesson:

> **Never teach the slogan where the theorem has conditions.**

## 7. Example: distinction graphs and Fuzzy Calculus

Potential relation:
\[
\text{bounded observer projection}
\longrightarrow
\text{induced indistinguishability relation}.
\]

If formally established, that would be a bridge from an observational geometry to a distinction graph.

But the reverse direction may lose:

- kernel shape;
- resolution scale;
- differential structure;
- curvature;
- path information;
- residue.

That would make the graph a quotient or shadow of richer structure.

At present this is a comparison program, not a theorem of this repository.

## 8. Five labels

Use only:

- **historical influence**
- **formal encoding**
- **extension/refinement**
- **structural analogy**
- **conjectured bridge**

If a statement does not fit one of these, rewrite it until it does.

## Exercise — classify the arrow

Classify each statement before researching whether it is true:

1. “π developed from the process-algebra tradition including CCS.”
2. “λ-computation can be encoded using π-processes.”
3. “ρ is basically π plus reflection.”
4. “Distinction graphs and Fuzzy Calculus both foreground observer-relative structure.”
5. “A bounded observer projection induces the exact graph structure of Goertzel 2019.”

Suggested categories:

- (1) historical influence / extension;
- (2) formal encoding;
- (3) oversimplified; needs replacement;
- (4) structural analogy;
- (5) conjectured bridge until proved.
