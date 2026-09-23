# 2 — Slopes, Shapes, and Space

**You need:** the idea of a [rate](01-classical-calculus.md) and area of a rectangle.\
**Your goal:** compare directions, then explain what “best” means in an optimization problem.

## A hill has more than one slope

On a small patch of an imaginary hill:

- walk 10 meters east, and you rise 2 meters;
- walk 10 meters north, and you rise 1 meter.

The hillside is fixed. Nothing needs to change over time. The height varies **with location**.

**Predict:** from the same starting point, which of those two walks gains more height?

<details>
<summary>Check</summary>

The eastward walk gains 2 meters, twice the northward gain. “The slope” needs a direction.

This does not yet compare every possible direction, such as northeast.

</details>

A height can depend on two inputs: how far east and how far north. **Multivariable calculus** handles functions with several inputs.

One useful move is to vary one input while holding the others fixed. Another is to ask how a quantity changes in a chosen direction.

## A quantity at every place

A map that assigns a quantity to each location is a **field**.

| Map | What each location gets |
|---|---|
| Height map | A number for height |
| Temperature map | A number for temperature |
| Wind map | An arrow for wind speed and direction |

An arrow has both size and direction; we call it a **vector**. Vector calculus can describe flow through a surface or circulation around a loop.

For example, a wind arrow can point along a window or straight through it. Its speed alone does not tell us how much air crosses the window.

## Which shape gives the most space?

You have 16 meters of fence for a rectangular garden. All four sides need fencing.

| Width | Length | Total fence | Area |
|---|---|---|---|
| 1 m | 7 m | 16 m | 7 square meters |
| 2 m | 6 m | 16 m | 12 square meters |
| 3 m | 5 m | 16 m | 15 square meters |
| 4 m | 4 m | 16 m | 16 square meters |

The square wins among these choices. But checking four rows does not prove it beats every rectangle, including ones with fractional side lengths.

**Optimization** means finding the best allowed choice for a stated goal. Here the goal is largest area; the constraint is 16 meters of fence.

Calculus gives ways to find and check candidates. A point where the rate of change is zero might be a maximum, a minimum, or neither. We still need to check.

## Try a changed problem

One side of the garden can now use an existing wall. Only three sides need fencing.

Must the 4-by-4 square still be best? Can you find a rectangle with more area using 16 meters of fence?

<details>
<summary>Check your reasoning</summary>

A rectangle 4 meters out from the wall and 8 meters along it uses $4+8+4=16$ meters of fence. Its area is 32 square meters.

The old answer relied on fencing all four sides. Changing the constraint changes the problem.

This example finds a better choice; by itself, it is not a proof of the new optimum.

</details>

<details>
<summary>Optional mathematics — checking the first optimum</summary>

If the width is $w$, the length is $8-w$, with $0<w<8$. The area is

$$
A(w)=w(8-w)=16-(w-4)^2.
$$

A square is never negative, so the area cannot exceed 16. It reaches 16 when $w=4$.

Calculus finds the same candidate from $A'(w)=8-2w=0$. The extra check establishes that it is a maximum.

For the hill, a simple height model is $h(x,y)=100+0.2x+0.1y$, with distances in meters. Its partial derivatives are $0.2$ and $0.1$. They measure the change in height per meter east and north, respectively.

</details>

## Other doors into geometry

**Tensor** methods handle quantities with more complex direction and coordinate rules. **Exterior calculus** organizes integration over curves, surfaces, and regions. These methods overlap; they are not levels in a single ladder.

To choose an entire path or shape, explore [the calculus of variations](../tracks/change/variational-calculus.md).

## Sources

The hill and garden are original examples. See OpenStax, *Calculus Volume 3*: [directional derivatives](https://openstax.org/books/calculus-volume-3/pages/4-6-directional-derivatives-and-the-gradient), [vector fields](https://openstax.org/books/calculus-volume-3/pages/6-1-vector-fields), and [Stokes' theorem](https://openstax.org/books/calculus-volume-3/pages/6-7-stokes-theorem). More geometry sources are in [References](../REFERENCES.md#geometry-and-field-calculi).

[← Rates and totals](01-classical-calculus.md) · [Home](../README.md) · [Next: Working in steps →](03-discrete-and-numerical.md)
