# 08 — Comparing Calculi

**Start with:** any two lessons.\
**By the end:** compare their objects and moves, then explain which question each helps answer.

## Begin with a question

The same situation can support several models. Comparing calculi starts with what you want to find out.

A garden has a tank, a valve, and a timer. Compare these questions:

| Compare | Classical calculus | Event calculus |
|---|---|---|
| Question | How much water entered the tank? | Is the valve open after the timer fires? |
| Objects | Flow rate and water amount over time | Events, times, and facts that may change |
| Move | Integrate the rate over an interval | Apply rules for event effects and persistence |
| Result | An amount, such as 8 liters | Whether a fact holds at a time |
| What else is needed? | Rate history; starting amount and outflow if asking for water now | Which events open or close the valve, and what holds initially |
| What counts as the same answer? | Equal amounts in the chosen units | The same truth value for the queried fact |

This is an original comparison of modeling roles. It does not assert a formal translation between the calculi.

## Try it

The valve is open. Is that enough to conclude that 8 liters entered?

<details>
<summary>Check your reasoning</summary>

No. You would also need information about flow and duration. An open valve might even have an empty supply.

The event model answers one question. A quantity model answers another. Connecting them requires assumptions about how valve state affects flow.

</details>

## Make your own comparison

Choose two lessons and use a new setting: a library, a game, a workshop, or a music player.

| Question | Calculus A | Calculus B |
|---|---|---|
| What am I trying to find out? | | |
| What are the objects? | | |
| What rule can I use? | | |
| What is one worked step? | | |
| What counts as the same result? | | |
| What information or assumption is still needed? | | |

A good comparison shows one actual move in each model. Naming two calculi is only the start.

<details>
<summary>Optional depth — compare native operations</summary>

| Calculus | Objects brought into focus | Characteristic move |
|---|---|---|
| classical | varying quantities | differentiate or integrate |
| variational | whole functions or paths | vary a candidate and evaluate a functional |
| stochastic | random processes and available information | stochastic integration |
| λ | terms with binding and application | β-reduction |
| sequent | assumptions and possible conclusions | apply an inference rule |
| π | processes and names | communicate a name |
| ρ | processes and quoted process names | communicate and use reflective structure |
| indications | marked and unmarked forms | simplify by laws of forms |
| distinction graphs | pairwise indistinguishability | construct or update edges |
| Fuzzy | fields and bounded observation | observer-relative differentiation, integration, and residue accounting |

“Same result” also varies: numerical equality, equality of forms, logical derivability, or a specified equivalence of process behavior. State the criterion.

</details>

<details>
<summary>Optional depth — when a comparison becomes a translation</summary>

For a proposed translation $T:A\to B$, ask:

1. What objects and operations does it map?
2. Which results or observations does it preserve?
3. Does doing two moves and then translating agree with translating and doing the corresponding moves?
4. What does it forget?
5. Under what conditions could the original be reconstructed?

For example, λ→π encodings give explicit ways to represent computation by communication. π→ρ encoding claims need a specified fragment and correctness criteria; the [ρ lesson](04-rho.md) points to the corrected result.

A shared teaching example establishes a comparison. An encoding theorem establishes a stronger, precisely scoped claim.

</details>

## Take it further

Use [Try It Somewhere New](../PRACTICE.md) to check whether you can carry an idea beyond the story that introduced it.

The aim is to say: **“Here is my question, here is a suitable rule, and here is why it applies.”**

[← Fuzzy Calculus](07-fuzzy.md) · [Home](../README.md) · [Practice →](../PRACTICE.md) · [Browse the pantheon](../PANTHEON.md)
