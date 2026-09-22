# Calculi

A pedagogy-first atlas of calculi: what each calculus takes as primitive, what it lets us do, what problem it was built to solve, and what is lost or gained when we move between them.

This repository is **not** a claim that all calculi form one historical lineage. Some are directly related by extension or encoding; some share only a structural analogy. We keep those relations separate.

## The guiding questions

A calculus becomes easier to understand when we ask what its world permits.

| Question | A calculus that makes it central |
|---|---|
| How does a function transform an argument? | λ-calculus |
| How do concurrent processes communicate and change connectivity? | π-calculus |
| What happens when processes can use representations of processes as names? | ρ-calculus |
| What follows from making or erasing a distinction? | calculus of indications |
| What can a particular observer distinguish? | distinction graphs |
| What calculus is available to a bounded observer whose observation itself has finite resolution and residue? | Fuzzy Calculus |

The point is not that each row supersedes the previous one. The point is that each row changes **what is primitive**.

## Learning path

1. [What is a calculus?](lessons/00-what-is-a-calculus.md)
2. [λ-calculus — substitution and computation](lessons/01-lambda.md)
3. [π-calculus — communication and mobility](lessons/02-pi.md)
4. [ρ-calculus — reflection and quoted processes](lessons/03-rho.md)
5. [Calculus of indications — distinction as operation](lessons/04-indications.md)
6. [Distinction graphs — distinction relative to an observer](lessons/05-distinction-graphs.md)
7. [Fuzzy Calculus — bounded observation and residual calculus](lessons/06-fuzzy.md)
8. [Comparing calculi without flattening them](lessons/07-comparison.md)
9. [Frontier: Goertzel's d-calculus](lessons/08-frontier-d-calculus.md)

Each lesson uses the same five-part frame:

- **Need** — what problem motivates the calculus?
- **Primitive** — what does the calculus assume before anything else?
- **Move** — what is the characteristic operation?
- **Example** — what happens in the smallest useful case?
- **Boundary** — what does this calculus *not* give us for free?

## A map, not a ladder

A rough conceptual map:

```text
functions / substitution
        λ
        │  encodable as processes
        ▼
communication / mobility
        π
        │  reflective process lineage
        ▼
        ρ

distinction as primitive
        │
        ├── calculus of indications
        │
        └── observer-relative distinguishability
                    │
              distinction graphs

bounded differentiation / observation
        │
        └── Fuzzy Calculus
```

The vertical lines above do **not** all mean the same thing. In this repository every edge must be labeled as one of:

- **historical influence**
- **formal encoding**
- **extension/refinement**
- **structural analogy**
- **conjectured bridge**

If we cannot support an edge, we do not draw it.

## Why "cosmology"?

A genealogy asks, "What descended from what?"

A cosmology asks a different question:

> **What kind of world does this calculus make expressible?**

In λ-calculus, the world is organized around application and substitution. In π-calculus, around interacting processes and names. In ρ-calculus, process structure can participate in naming and reflection. In distinction-based systems, what can and cannot be told apart becomes central. In Fuzzy Calculus, observation is bounded and the failure of exact recovery is itself mathematical data.

That is the teaching goal of this repository: learn a calculus by learning the world it assumes.

## Epistemic rules

1. Historical claims require sources.
2. An encoding is not an identity.
3. Similar notation is not evidence of ancestry.
4. A later calculus can generalize an earlier object without retroactively originating it.
5. Unpublished or incompletely specified systems stay in the **frontier** section until their primitives and laws are public.
6. Fuzzy Calculus is presented alongside its antecedents, not as if observer-relative distinction began with it.

## Sources

See [REFERENCES.md](REFERENCES.md). Primary or near-primary sources are preferred whenever possible.

## License

Educational material in this repository is intended to remain open and citable. License metadata will be added explicitly before a tagged release.
