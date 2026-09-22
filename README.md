# Calculi

A pedagogy-first atlas of calculi: what each calculus takes as primitive, what it lets us do, what problem it was built to solve, and what is lost or gained when we move between them.

This repository is **not** a claim that all calculi form one historical lineage. Some are directly related by extension or encoding; some share only a structural analogy. We keep those relations separate.

## The guiding idea

A calculus becomes easier to understand when we ask:

> **What kind of world does this calculus make expressible?**

Some calculi make **change** primary. Some make **substitution**, **proof**, **communication**, **action**, **distinction**, or **observation** primary.

The word *calculus* is therefore used here in its broad mathematical sense: a disciplined system of objects, operations, and rules for transforming or reasoning about them.

## Constellations

This is a cosmology, not a single ladder.

| Constellation | Central question | Representative calculi |
|---|---|---|
| **Change and quantity** | How does something vary, accumulate, fluctuate, or optimize? | differential & integral calculus; calculus of variations; stochastic calculus; fractional calculus; tensor calculus |
| **Functions and computation** | How can computation be reduced to application, abstraction, and substitution? | combinatory logic; λ-calculus; typed λ-calculi; System F; differential λ-calculus |
| **Proof and types** | How can derivation itself be made formal? | natural deduction; sequent calculus; calculus of constructions; calculus of inductive constructions |
| **Interaction and concurrency** | How do independent processes synchronize, communicate, move, or rewrite one another? | CCS; CSP; ACP; π-calculus; join calculus; ambient calculus; stochastic π-calculus |
| **Security and distributed interaction** | How do names, channels, identities, and adversaries affect interaction? | spi calculus; applied π-calculus |
| **Reflection and higher-order process** | What changes when processes can represent, quote, or manipulate processes? | higher-order process calculi; ρ-calculus; ψ-calculi |
| **Action and evolving worlds** | How do actions change a world through time? | situation calculus; event calculus; fluent calculus |
| **Relations and data** | How can queries and relations be expressed declaratively? | relational calculus |
| **Distinction and observation** | What follows from drawing a distinction, and from limits on distinguishability? | calculus of indications; distinction graphs; Fuzzy Calculus |
| **Advanced mathematical calculi** | What happens when “calculus” is generalized to new mathematical objects? | Malliavin calculus; functional calculus; umbral calculus; calculus of fractions; Goodwillie calculus |
| **Frontier / incomplete public specification** | What new calculi are being proposed now? | Goertzel's d-calculus |

Not every item above will receive equal depth immediately. The repository will distinguish a **core learning path** from **expansion tracks**.

## Core learning path

The first pass should let a motivated reader understand why very different things are all called a *calculus*.

### I. What does "calculus" mean?

1. [What is a calculus?](lessons/00-what-is-a-calculus.md)
2. **Classical calculus** — local change and accumulation
3. **Calculus of variations** — optimizing whole paths rather than single values
4. **Stochastic calculus** — change when trajectories are noisy

### II. Computation becomes an object

5. **Combinatory logic** — computation without bound variables
6. [λ-calculus — substitution and computation](lessons/01-lambda.md)
7. **Typed λ-calculi and System F** — computation constrained by types
8. **Sequent calculus and natural deduction** — proof as formal transformation
9. **Calculus of constructions** — proofs and programs under one typed language

### III. From functions to interacting processes

10. **CCS / CSP / ACP** — early process-algebra perspectives
11. [π-calculus — communication and mobility](lessons/02-pi.md)
12. **Join calculus** — synchronization by reaction patterns
13. **Ambient calculus** — computation with movement and location
14. **spi / applied π-calculus** — cryptographic and adversarial interaction
15. [ρ-calculus — reflection and quoted processes](lessons/03-rho.md)
16. **ψ-calculi** — a parametric family of mobile process calculi

### IV. Worlds that change because actions occur

17. **Situation calculus**
18. **Event calculus**
19. **Fluent calculus**
20. **Relational calculus**

### V. Distinction becomes mathematical

21. [Calculus of indications — distinction as operation](lessons/04-indications.md)
22. [Distinction graphs — distinction relative to an observer](lessons/05-distinction-graphs.md)
23. [Fuzzy Calculus — bounded observation and residual calculus](lessons/06-fuzzy.md)
24. [Comparing calculi without flattening them](lessons/07-comparison.md)
25. [Frontier: Goertzel's d-calculus](lessons/08-frontier-d-calculus.md)

## Expansion tracks

Once the core path is stable, separate tracks can deepen particular meanings of *calculus*.

### Change beyond Newton and Leibniz

- tensor calculus
- fractional calculus
- stochastic differential calculus
- Malliavin calculus
- functional calculus

### Computation and type theory

- simply typed λ-calculus
- linear λ-calculus
- differential λ-calculus
- System F
- calculus of constructions
- calculus of inductive constructions

### Process calculi

- CCS
- CSP
- ACP
- π-calculus
- higher-order π-calculus
- join calculus
- ambient calculus
- stochastic π-calculus
- spi calculus
- applied π-calculus
- ρ-calculus
- ψ-calculi

### Logic of action and time

- situation calculus
- event calculus
- fluent calculus

### Structural and categorical uses of "calculus"

- calculus of fractions
- Goodwillie calculus
- umbral calculus

## One teaching frame for every lesson

Every lesson should answer the same seven questions:

1. **Need** — what problem made this calculus useful?
2. **World** — what sort of things exist inside it?
3. **Primitive** — what does it assume before anything else?
4. **Move** — what is the characteristic operation or rewrite?
5. **Toy example** — what happens in the smallest useful case?
6. **Boundary** — what does the calculus *not* give us for free?
7. **Relations** — what is historically inherited, formally encoded, or merely analogous to another calculus?

This lets a reader compare Newtonian differentiation, β-reduction, π-calculus communication, sequent rules, and observer-relative distinction without pretending they are the same operation.

## A map, not a ladder

A rough map:

```text
CHANGE / ACCUMULATION
classical calculus
   ├── variations
   ├── stochastic
   ├── fractional
   └── tensor / functional / Malliavin ...

FORMAL TRANSFORMATION
combinatory logic
   └── λ-calculus
        ├── typed λ / System F
        ├── differential λ
        └── proofs-as-programs
             ├── natural deduction / sequents
             └── Calculus of Constructions / CIC

INTERACTION
CCS / CSP / ACP
   └── π-calculus
        ├── join / ambient
        ├── spi / applied π
        ├── stochastic π
        ├── higher-order process calculi
        ├── ρ-calculus
        └── ψ-calculi

ACTION / WORLD CHANGE
situation calculus
   ├── event calculus
   └── fluent calculus

DISTINCTION / OBSERVATION
calculus of indications
   └── observer-relative distinction
        ├── distinction graphs
        └── bounded differentiation / observation
             └── Fuzzy Calculus

FRONTIER
Goertzel d-calculus — comparison deferred until public primitives and laws are available
```

The lines above do **not** all mean the same thing. In this repository every edge must be labeled as one of:

- **historical influence**
- **formal encoding**
- **extension/refinement**
- **structural analogy**
- **conjectured bridge**

If we cannot support an edge, we do not draw it.

## Why "cosmology"?

A genealogy asks:

> What descended from what?

A cosmology asks:

> **What kind of world must exist for this calculus to make sense?**

In classical calculus, quantities vary continuously enough for local change and accumulation to be related. In λ-calculus, the world is organized around abstraction, application, and substitution. In π-calculus, around interacting processes and names. In ρ-calculus, process structure can participate in naming and reflection. In distinction-based systems, what can and cannot be told apart becomes central. In Fuzzy Calculus, observation is bounded and failure of exact recovery is itself mathematical data.

The teaching goal is to learn each calculus by learning the world it assumes.

## Epistemic rules

1. Historical claims require sources.
2. An encoding is not an identity.
3. Similar notation is not evidence of ancestry.
4. A structural analogy is not a historical influence.
5. A later calculus can generalize an earlier object without retroactively originating it.
6. Unpublished or incompletely specified systems stay in the **frontier** section until their primitives and laws are public.
7. Fuzzy Calculus is presented alongside its antecedents, not as if observer-relative distinction began with it.
8. Where scholars disagree about lineage or interpretation, the disagreement stays visible.

## Sources

See [REFERENCES.md](REFERENCES.md). Primary or near-primary sources are preferred whenever possible.

## License

Educational material in this repository is intended to remain open and citable. License metadata will be added explicitly before a tagged release.
