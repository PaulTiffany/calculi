# Connections Between Calculi

Two tools can be related in several ways. A shared word, symbol, or diagram does not tell us which relation holds.

This page distinguishes useful connections. It is not a single history of the field.

## Connections met in the tour

| Tools | Kind of connection | What carries across | Where to check |
|---|---|---|---|
| Differentiation and integration | Theorem | Under suitable conditions, accumulating a derivative gives endpoint change | [Lesson 1](lessons/01-classical-calculus.md); OpenStax's Fundamental Theorem |
| Differences/sums and derivatives/integrals | Discrete counterpart and approximation | Both relate changes and totals; finite steps and local limits have different rules | [Lesson 3](lessons/03-discrete-and-numerical.md), including the cancellation identity |
| Ordinary optimization and calculus of variations | Extension of the kind of input | A candidate can be a whole function or path rather than a single number | [Variations track](tracks/change/variational-calculus.md); Strang |
| Propositional and predicate logic | Extension of language | Predicate logic expresses claims about objects and quantifiers | [Lesson 4](lessons/04-logic-and-proof.md); Open Logic |
| Predicate logic and relational calculus | Application with restrictions | Logical conditions define database answers; safe queries control results | [Lesson 6](lessons/06-data-and-relations.md); *Database System Concepts*, Chapter 27 |
| Untyped and typed lambda calculi | Additional formal structure | Typing rules constrain allowed expressions; different systems impose different constraints | [Computation lesson](lessons/05-computation-and-correctness.md) and [lambda track](tracks/computation/lambda-calculus.md) |
| Proofs and typed programs | Formal correspondence in specified systems | Propositions can correspond to types and proofs to terms | [Constructions track](tracks/types/calculus-of-constructions.md); Coquand–Huet |
| Program logic and separation logic | Extension | Assertions can describe separate parts of memory and support local reasoning | [Reynolds's paper](https://www.cs.cmu.edu/~jcr/seplogic.pdf) |
| Probability and stochastic calculus | Specialized development | Integration is defined for suitable random processes, with path and information assumptions | [Chance lesson](lessons/08-chance-and-cause.md) and [stochastic track](tracks/change/stochastic-calculus.md) |
| Probability and causal inference | Added causal structure | Interventions require causal assumptions beyond a joint probability description | [Chance lesson](lessons/08-chance-and-cause.md); Pearl |

These relations are not all historical claims. For example, a mathematical analogy can be useful without showing that one author borrowed from another.

## More technical translation claims

An **encoding** translates one formal system into another. A serious claim must say which systems are used and which properties survive.

| Claim area | What must be specified | Source |
|---|---|---|
| Lambda computations represented by communicating processes | The lambda fragment, evaluation behavior, and target process language | Milner's [polyadic pi tutorial](https://www.lfcs.inf.ed.ac.uk/reports/91/ECS-LFCS-91-180/) |
| Pi and reflective rho calculus | The source fragment, name handling, and preservation criteria | [Rho track](tracks/interaction/rho-calculus.md); Lybech's corrected encoding and separation results |

A translation is not automatically an identity, an improvement, or proof that either language is best for teaching.

## Shared examples are not formal bridges

Our delivery service uses a query and a stock update. Their connection depends on facts such as how many crates each order needs. It is a **modeling connection**, not a theorem that all queries and updates fit together.

Likewise, an example about lost information can motivate both a graph model and an observation framework. A shared example does not establish equivalence or historical descent.

When contributing a connection, say whether it is a theorem, extension, application, historical influence, encoding, analogy, or proposed research bridge. Cite the specific result when the claim is formal.

[Home](README.md) · [Field map](PANTHEON.md) · [Choose and combine](lessons/09-choose-and-combine.md) · [References](REFERENCES.md)
