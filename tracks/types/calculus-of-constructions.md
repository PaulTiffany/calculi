# Track — Calculus of Constructions: Types, Terms, and Proofs

## Need

Can we build a formal language expressive enough to represent:

- programs;
- propositions;
- proofs;
- mathematical constructions;

inside one typed framework?

The **Calculus of Constructions (CoC)**, introduced by Thierry Coquand and Gérard Huet, is a landmark answer.

## World

The world is a typed λ-calculus with rich forms of dependency and abstraction.

Terms can depend on terms, and types can participate in higher-order structure.

Under propositions-as-types interpretations, proving a proposition corresponds to constructing a term of the appropriate type.

## Primitive intuition

Untyped λ-calculus asks whether an application reduces.

Typed calculi add another question first:

> **Is this expression even well-formed at this type?**

A judgment might have the form
\[
\Gamma\vdash t:A,
\]
read as: under context \(\Gamma\), term \(t\) has type \(A\).

## Characteristic move

The calculus combines λ-style reduction with typing rules.

So computation and proof checking become tightly coupled.

## Why “construction”?

The central idea is constructive:

> to establish a proposition, construct an inhabitant of the corresponding type.

This creates a bridge between programming-language semantics and formal proof.

## Descendants and implementations

The Calculus of Inductive Constructions extends this family with inductive definitions and underlies the theory of systems such as Coq.

The historical and implementation details deserve their own later lesson.

## Boundary

A proof calculus can certify derivations inside its formal system.

It does not by itself guarantee that a chosen formal specification captures everything we care about in the outside world.

That distinction becomes crucial when formal verification is used for AI or safety systems.

## Relation to λ-calculus

**Extension/refinement.**

The λ-calculus ancestry is direct, but typing and dependency substantially change the formal world.

## Relation to sequent calculus

There are profound proof-theoretic correspondences, but this atlas will introduce them through explicit Curry–Howard mappings rather than by saying all proof calculi are interchangeable.

## Sources

- Thierry Coquand and Gérard Huet, “The Calculus of Constructions,” *Information and Computation* 76(2–3):95–120, 1988. DOI: 10.1016/0890-5401(88)90005-3.
