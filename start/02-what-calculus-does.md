# 02 — What Calculus Does

**Start with:** [rates and totals](01-things-change.md).\
**By the end:** explain why changing rates need more care than one multiplication.

## What if the tap slows down?

A tap fills an empty bucket. Nothing spills or drains away.

| Part of the fill | Steady rate during that part | Time | Water added |
|---|---|---|---|
| First part | 3 liters per minute | 2 minutes | 6 liters |
| Second part | 1 liter per minute | 2 minutes | 2 liters |
| Whole fill | Rate changes | 4 minutes | **8 liters** |

Multiply within each part, then add the parts. Using the final rate for all four minutes would miss the faster start.

## Where calculus enters

Real rates can change all the time. We can split the time into short pieces, estimate the water added in each piece, and add them.

Ordinary calculus makes this careful: under suitable conditions, the sums approach a definite value as the pieces get smaller. An **integral** gives that accumulated change.

We can also work the other way. Compare two nearby water amounts and divide the difference by the elapsed time. That gives an average rate. As the interval shrinks, the rate may approach a definite value. A **derivative** gives that rate at a moment.

The value an estimate approaches is called a **limit**. Smaller pieces are useful because we study what they approach, not because we divide by zero.

## Try it somewhere else

A walker travels 2 kilometers in the first hour and 4 in the second.

1. How far did the walker travel?
2. What was the average speed over both hours?
3. Do these two totals tell us the speed at every moment?

<details>
<summary>Check your reasoning</summary>

1. **6 kilometers:** add the two distances.
2. **3 kilometers per hour:** divide 6 kilometers by 2 hours.
3. **No.** The walker could have sped up, slowed down, or paused within either hour.

Average speed describes an interval. Speed at a moment needs more information.

</details>

## What must we keep track of?

An integral of the filling rate tells us how much water was **added**. To know the amount now, we also need the starting amount. Water leaving the bucket must be counted too.

> Derivatives ask about local rates. Integrals add up change. Calculus connects the two under stated conditions.

*Examples are original. The [classical lesson](../lessons/01-classical-calculus.md) gives the formulas and sources.*

[← Previous](01-things-change.md) · [Home](../README.md) · [Next: Why many calculi? →](03-why-many-calculi.md)
