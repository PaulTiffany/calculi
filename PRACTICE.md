# Try It Somewhere New

**Start with:** the [three beginner pages](start/01-things-change.md), then whichever linked lessons you want to practice.

Pick a challenge. Say, sketch, or write an answer **before** opening the explanation. Each challenge changes the setting so you can check whether the idea travels.

## 1. From water to deliveries

A packer finishes 4 parcels per minute for 3 minutes, then 2 per minute for 5 minutes. There were already 6 finished parcels.

How many are ready now? Why can't you multiply the final rate by all 8 minutes?

<details>
<summary>Check: rates and totals</summary>

The packer adds $4\times3+2\times5=22$ parcels. Including the starting 6 gives **28**.

The final rate does not describe the first three minutes. Split the time wherever the stated rate changes.

This is the same accumulation pattern as [filling a tank](lessons/01-classical-calculus.md).

</details>

## 2. From instructions to a playlist

An instruction takes two songs and returns the second. It receives Song A, then Song B. What does it return?

Now rename them Song X and Song Y, keeping the order. What stayed the same?

<details>
<summary>Check: use the rule, not the labels</summary>

It returns **Song B**, then **Song Y**. The second-input rule stayed the same.

In the [λ lesson](lessons/02-lambda.md), that pattern is $\lambda x.\lambda y.y$. The song names are labels in this analogy; playing the music would require more rules.

</details>

## 3. From jars to a library

Assume: every reserved book has a label. This book has a label.

Must it be reserved? Explain with a possible counterexample.

<details>
<summary>Check: which direction does the rule go?</summary>

No. Some unreserved books could have labels too.

The assumption lets us go from **reserved to labeled**. It does not give the reverse direction. See [proof as careful steps](tracks/proof/sequent-calculus.md).

</details>

## 4. From a help desk to a game

A player tells a teammate, “There is another chat room.” In a second version, the player sends a usable invitation to that room.

Which version changes the teammate's available connections? What assumption makes your answer work?

<details>
<summary>Check: information that enables a next move</summary>

The usable invitation can provide a new connection, assuming it grants access to join. Merely saying another room exists does not provide the route.

This resembles [π-calculus name passing](lessons/03-pi.md). A full game model would also specify access rules.

</details>

## 5. From a garden to a recorded journey

A device records only the total distance of a trip. Two trips both record 10 kilometers.

Must their speeds have been the same throughout? Name an extra observation that would help distinguish them.

<details>
<summary>Check: same record, different possibilities</summary>

No. One could be steady and the other include stops and bursts of motion. Distances recorded at intermediate times would help.

Equal totals leave differences unresolved. This connects [rates and totals](start/02-what-calculus-does.md) with the recovery question in [Fuzzy Calculus](lessons/07-fuzzy.md).

This is a comparison of questions, not an identification of their formal operators.

</details>

## Build one of your own

Choose an activity you know. Fill in:

> I want to know _____. My objects are _____.\
> The rule I can use is _____. Here is one step: _____.\
> This works if _____. It still leaves _____ unanswered.

Change the objects or the setting and try again. Which part of the reasoning survives? Which assumption must change?

## For a learner or teacher

Use a short session: explain one example, let the learner try a similar one, then change the setting. Ask for a reason before revealing the answer. Paper and conversation are enough.

| If the learner can… | Try next |
|---|---|
| Retell the example but cannot do a new one | Change just one input and work through it together |
| Do a similar problem with a reason | Change the setting and ask what stays the same |
| Transfer the rule and name an assumption | Find a case where the rule would not apply |

Return later to one challenge without rereading its lesson. Success means explaining the move and its conditions, not remembering a calculus's name.

*All challenges are original teaching examples. Reuse or adapt with the [repository credit](ATTRIBUTION.md#reuse) and [CC BY 4.0 license](LICENSE.md).*

[Home](README.md) · [Compare two calculi](lessons/08-comparison.md) · [Browse the pantheon](PANTHEON.md)
