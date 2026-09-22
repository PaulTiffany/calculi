# 08 — Comparing Calculi

The purpose of the pyramid is not to reveal one secret master calculus. It is to make comparison easier.

## Compare the world first

| Calculus | Native world |
|---|---|
| classical | varying quantities |
| variational | paths and functionals |
| stochastic | random processes and filtrations |
| λ | terms, abstraction, application |
| sequent | formulas in inferential contexts |
| π | processes and names |
| ρ | reflective process/name structure |
| indications | marked and unmarked forms |
| distinction graphs | observer-relative distinguishability |
| Fuzzy | bounded observational geometry |

## Compare the move

| Calculus | Characteristic move |
|---|---|
| classical | differentiate / integrate |
| variational | vary a path or function |
| stochastic | integrate along stochastic processes |
| λ | β-reduce |
| sequent | infer by a rule |
| π | communicate / transition |
| ρ | communicate with reflective naming structure |
| indications | mark / simplify forms |
| distinction graph | construct or update indistinguishability |
| Fuzzy | observer-relative differentiate / integrate and track residue |

## Compare what counts as “the same”

Different calculi use different notions of sameness: numerical equality, normal form, α/β/η equivalence, logical derivability, bisimulation, graph equivalence, or observer-visible equivalence.

This is often where apparently similar calculi sharply diverge.

## Compare translations

Suppose

\[
T:A\to B.
\]

Ask:

1. What does \(T\) preserve?
2. What does it forget?
3. Does it preserve composition?
4. Does it preserve observable behavior?
5. Can the original object be reconstructed?

A translation is interesting precisely because two calculi need not be identical.

## Three useful examples

### λ and π

λ-computation can be represented using communicating processes under explicit encodings.

That does not erase the difference between **application** and **interaction** as native primitives.

### π and ρ

ρ-calculus is closely related to π-calculus but adds reflective structure.

The encoding history itself is instructive: exact formal claims matter more than slogans like “π plus reflection.”

### Classical and stochastic calculus

Both speak of change and integration, but stochastic path structure alters the valid rules.

The same familiar word—“integral”—can therefore name operations living in significantly different formal worlds.

## Exercise — climb the pyramid

Pick any two calculi in the repository and fill in:

| Question | Calculus A | Calculus B |
|---|---|---|
| What exists? | | |
| What differences matter? | | |
| What can happen? | | |
| How do moves compose? | | |
| What counts as the same result? | | |
| What is not native? | | |

If the comparison is still interesting after filling this out, it is probably worth formalizing.

## Final lesson

A calculus is not just notation.

It is a choice about what exists, what may change, what may compose, what may be observed, and what may count as equivalent.

The pyramid is a way to see those choices.
