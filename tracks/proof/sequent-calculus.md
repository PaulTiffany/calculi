# Track — Sequent Calculus: Proof as Careful Steps

**Start with:** reading an “if … then …” statement.\
**By the end:** distinguish what follows from assumptions from what merely sounds plausible.

## A worked example

Assume these two statements:

1. If this jar is sealed, then it is labeled.
2. This jar is sealed.

We may conclude: **this jar is labeled**.

A **proof** makes each allowed step explicit. A **sequent** records what follows from a collection of assumptions. Sequent calculus gives precise rules for building such proofs.

## Try it

Keep the first assumption, but change the second to “this jar is labeled.”

Can you now conclude that it is sealed?

<details>
<summary>Check your reasoning</summary>

No. A labeled jar could be open. That possibility agrees with the first assumption, so the proposed conclusion is not guaranteed.

The direction of the implication matters.

</details>

## Try it somewhere else

“If the printer is out of paper, its warning light is on.” You see the light.

What would you need before concluding that the printer is out of paper?

<details>
<summary>Check and connect</summary>

You would need a rule or evidence ruling out other causes, such as a jam. The given statement supplies only one direction.

This has the same structure as the jar example. Changing the nouns does not repair the inference.

</details>

<details>
<summary>Optional notation — sequents, rules, and cut</summary>

A sequent is often written

$$
\Gamma\vdash\Delta.
$$

The left side records assumptions. The right side records conclusions or alternatives, depending on the chosen system.

For a single-conclusion system, an AND rule can take this form:

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash B}{\Gamma\vdash A\land B}.
$$

Read it as: if the same assumptions establish $A$ and establish $B$, they establish both.

A proof is a tree of rule applications. The **cut rule** lets one proof supply an intermediate result used by another. Gentzen's cut-elimination results show how to remove such cuts in his systems.

Proof rules justify conclusions from assumptions. Establishing that the assumptions describe a real jar or printer is a further task.

</details>

## Connections and sources

Gerhard Gentzen developed both natural deduction and sequent calculi in 1934–35. They organize proofs differently. Particular logic/type correspondences also connect proof normalization with computation; see [Relations](../../RELATIONS.md).

The jar and printer examples are original illustrations of valid and invalid inference. See [References](../../REFERENCES.md#proof-calculi) for Gentzen and later expositions.

[Home](../../README.md) · [Logic family](../../PANTHEON.md#4-logic-and-formal-reasoning) · [Next: types and constructions](../types/calculus-of-constructions.md)
