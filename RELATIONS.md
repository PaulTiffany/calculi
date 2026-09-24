# Connections Between Calculi

Two tools can be related in several ways. A shared word, symbol, or diagram does not tell us which relation holds.

This page distinguishes useful connections. It is not a single history of the field.

## Connections met in the tour

| Tools | Kind of connection | What carries across | Where to check |
|---|---|---|---|
| Differentiation and integration | Theorem | Under suitable conditions, accumulating a derivative gives endpoint change | [Lesson 1](lessons/01-classical-calculus.md); OpenStax's Fundamental Theorem |
| Differences/sums and derivatives/integrals | Discrete counterpart and approximation | Telescoping recovers endpoint change exactly; a difference divided by a step can approximate a derivative under suitable conditions | [Finite differences](tracks/change/finite-difference-calculus.md) and [numerical calculus](tracks/change/numerical-calculus.md); Stanley and Demanet |
| Differential equations and repeated updates | Discretization | Euler's method turns a rate rule into a recurrence; its accuracy and stability depend on the equation and step size | [Tank model](tracks/change/differential-equations.md); OpenStax §4.2 |
| Differential equations and Laplace transforms | Transform method | Under convergence and regularity conditions, a derivative transforms to multiplication by the new variable with an initial-value correction | [Operational calculus](tracks/operators/operational-calculus.md); MIT 18.03SC |
| Ordinary optimization and calculus of variations | Extension of the kind of input | A candidate can be a whole function or path rather than a single number | [Variations track](tracks/change/variational-calculus.md); Strang |
| Real and complex calculus | Extension of the number system with stronger differentiability requirements | Complex difference quotients must converge for arbitrary complex approaches | [Complex track](tracks/change/complex-calculus.md); MIT 18.04 |
| Tensor and exterior calculus | Specialized mathematical structure | Differential forms are alternating covariant tensors, with an exterior derivative and integration rules | [Tensor](tracks/geometry/tensor-calculus.md) and [exterior](tracks/geometry/exterior-calculus.md) tracks; Tong and Sjamaar |
| Ordinary and fractional operators | Extension under specified definitions | Orders of integration and differentiation can be noninteger; history, domains, and initial conditions matter | [Fractional track](tracks/change/fractional-calculus.md); Mainardi–Gorenflo |
| Scalar polynomials and matrix functions | Extension of the kind of input | Matrix powers use composition; a constant term multiplies the identity operator | [Functional track](tracks/operators/functional-calculus.md); Higham |
| Propositional and predicate logic | Extension of language | Predicate logic expresses claims about objects and quantifiers | [Lesson 4](lessons/04-logic-and-proof.md); Open Logic |
| Classical and linear logic | Change to structural rules and connectives | Basic linear assumptions cannot be copied or discarded freely; reusable assumptions are marked | [Linear-logic track](tracks/proof/linear-logic.md); Girard and Pfenning |
| Predicate logic and relational calculus | Application with restrictions | Logical conditions define database answers; safe queries control results | [Lesson 6](lessons/06-data-and-relations.md); *Database System Concepts*, Chapter 27 |
| Untyped and typed lambda calculi | Additional formal structure | Typing rules constrain allowed expressions; different systems impose different constraints | [Computation lesson](lessons/05-computation-and-correctness.md) and [lambda track](tracks/computation/lambda-calculus.md) |
| Lambda calculus and combinatory logic | Formal translation | Bracket abstraction replaces bound-variable declarations with combinators; the translation need not preserve size or step count | [Combinator track](tracks/computation/combinatory-logic.md); Lynn and Diller |
| Simply typed lambda calculus and System F | Extension | Type abstraction and application express reuse across type choices | [System F track](tracks/types/system-f.md); Girard, Bornholt, and Pfenning |
| Proofs and typed programs | Formal correspondence in specified systems | Propositions can correspond to types and proofs to terms | [Constructions track](tracks/types/calculus-of-constructions.md); Coquand–Huet |
| Hoare triples and weakest preconditions | Related methods of specification and verification | Backward transformation derives conditions sufficient for a triple; termination conventions must agree | [Program-logic track](tracks/proof/hoare-logic.md); Aldrich and Dijkstra |
| Program logic and separation logic | Extension | Assertions describe separate parts of memory; the frame rule preserves an untouched part under its side conditions | [Separation track](tracks/proof/separation-logic.md); Reynolds |
| Probability and stochastic calculus | Specialized development | Integration is defined for suitable random processes, with path and information assumptions | [Chance lesson](lessons/08-chance-and-cause.md) and [stochastic track](tracks/change/stochastic-calculus.md) |
| Probability and causal inference | Added causal structure | Interventions require causal assumptions beyond a joint probability description | [Chance lesson](lessons/08-chance-and-cause.md); Pearl |
| Epistemic and dynamic epistemic logic | Extension to information-changing events | Public-announcement updates restrict worlds and accessibility relations; general event models add further structure | [Epistemic track](tracks/observation/epistemic-logic.md); Baltag–Moss–Solecki |
| Recorded attributes and rough approximations | A specified mathematical construction | Equality of recorded attributes yields equivalence classes; classes wholly inside or meeting a target define lower and upper approximations | [Rough-set track](tracks/observation/rough-sets.md); Pawlak |
| Trace equivalence and strong bisimulation | Different comparison strengths | Strong bisimulation preserves matching action sequences; equal trace sets need not preserve branching behavior | [Behavior track](tracks/observation/observational-equivalence.md); Sangiorgi |
| Operators and measurement patterns | Concrete implementation | A specified two-qubit pattern implements the Hadamard operator after an outcome-dependent correction | [Measurement track](tracks/observation/measurement-calculus.md); Danos–Kashefi–Panangaden |
| Observation and intervention | Causal identification under assumptions | Back-door adjustment expresses some intervention probabilities using observational probabilities and a suitable causal graph | [Do-calculus track](tracks/observation/do-calculus.md); Pearl |

These relations are not all historical claims. For example, a mathematical analogy can be useful without showing that one author borrowed from another.

## More technical translation claims

An **encoding** translates one formal system into another. A serious claim must say which systems are used and which properties survive.

| Claim area | What must be specified | Source |
|---|---|---|
| Lambda computations represented by communicating processes | The lambda fragment, evaluation behavior, and target process language | Milner's [polyadic pi tutorial](https://www.lfcs.inf.ed.ac.uk/reports/91/ECS-LFCS-91-180/) |
| Pi and reflective rho calculus | The source fragment, name handling, and preservation criteria | [Rho track](tracks/interaction/rho-calculus.md); Lybech's corrected encoding and separation results |

A translation is not automatically an identity, an improvement, or proof that either language is best for teaching.

## Shared examples are not formal bridges

The tank in the [differential-equation](tracks/change/differential-equations.md) and [operational-calculus](tracks/operators/operational-calculus.md) tracks is the same specified model. Here the connection is exact: the transform calculation returns a function satisfying both the original rate equation and its initial value. The Euler calculation approximates that same function at selected times.

Our delivery service uses a query and a stock update. Their connection depends on facts such as how many crates each order needs. It is a **modeling connection**, not a theorem that all queries and updates fit together.

The card viewers, crate labels, and temperature comparisons all ask which distinctions remain available. Their rules differ: equality of recorded labels is transitive, while the temperature track's pairwise tolerance is not. This is a useful comparison of specified examples.

When contributing a connection, say whether it is a theorem, extension, application, historical influence, encoding, analogy, or proposed research bridge. Cite the specific result when the claim is formal.

[Home](README.md) · [Field map](PANTHEON.md) · [Choose and combine](lessons/09-choose-and-combine.md) · [References](REFERENCES.md)
