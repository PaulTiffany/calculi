# 01 — Classical Calculus: Local Change and Accumulation

**Start with:** [rates, totals, and limits](../start/02-what-calculus-does.md).\
**By the end:** explain a rate, add up change, and say why the starting amount matters.

## The idea

A **function** is a rule that assigns an output to an input. For a filling tank, the input could be time and the output the amount of water.

Classical calculus studies how such quantities vary. Its two main moves are:

- **differentiate:** find the local rate of change;
- **integrate:** add up change across an interval.

## A worked example

A tank starts with **5 liters**. Water enters steadily at **2 liters per minute** for 3 minutes. None leaves.

| What do we want? | Reasoning | Answer |
|---|---|---|
| Rate of change | Each minute adds 2 liters | 2 liters per minute |
| Water added | 2 liters per minute × 3 minutes | 6 liters |
| Water now | Starting amount + water added | **11 liters** |

The integral of the rate gives the **6 liters added**. The starting amount is needed to get 11.

For a rate that varies, we add contributions from smaller pieces, as in the [beginner example](../start/02-what-calculus-does.md). Limits let us make this precise.

## Try it somewhere else

A box holds 7 meters of ribbon. A machine feeds in ribbon at 3 meters per minute for 2 minutes.

1. How much ribbon is added? How much is in the box?
2. A second box starts empty and receives ribbon at the same rate. Does knowing the rate tell you which box you have?

<details>
<summary>Check your reasoning</summary>

1. **6 meters are added; 13 meters are in the first box.**
2. **No.** Both amounts grow at the same rate. The second box ends with 6 meters.

A rate records change. It does not record the starting amount. The water and ribbon examples share this structure even though their units differ.

</details>

## The connection

The **Fundamental Theorem of Calculus** connects differentiation and integration. With suitable assumptions, adding up a quantity's rate of change gives its final value minus its starting value.

<details>
<summary>Optional notation — derivative, integral, and the theorem</summary>

Let $f(x)=x^2$, where $x^2$ means $x$ multiplied by itself. The derivative is defined by

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h},
$$

when that limit exists. The fraction is the change in output divided by a nonzero change in input.

Here it simplifies to $2x+h$, so the limit is $f'(x)=2x$. At $x=3$, the local rate is 6.

Integrating this derivative from 0 to 3 gives

$$
\int_0^3 2x\,dx=9.
$$

If we use $F(x)=5+x^2$ instead, its derivative is still $2x$. The integral gives $F(3)-F(0)=14-5=9$, not 14.

A standard form of the theorem says: if $f$ is continuous on $[a,b]$ and $F(x)=\int_a^x f(t)\,dt$, then $F'(x)=f(x)$ in the interior. If $F'=f$ on the interval, then

$$
\int_a^b f(x)\,dx=F(b)-F(a).
$$

The assumptions specify where these rules apply.

</details>

<details>
<summary>Further connection — surfaces and boundaries</summary>

For a suitable oriented manifold $M$ and differential form $\omega$, Stokes' theorem relates an integral over a region to one over its boundary:

$$
\int_M d\omega=\int_{\partial M}\omega.
$$

Differential forms describe quantities that can be integrated over curves, surfaces, and higher-dimensional regions. Explore [geometry and fields](../PANTHEON.md#2-geometry-and-fields) when you want this wider setting.

</details>

## Where to go next

For change across space, explore [vector calculus](../PANTHEON.md#2-geometry-and-fields). For choosing a whole path, try [variations](../tracks/change/variational-calculus.md). For random paths, try [stochastic calculus](../tracks/change/stochastic-calculus.md).

Each adds structure and assumptions to the questions we can ask.

## Sources and optional viewing

The examples are original. For the standard theorem, see Gilbert Strang and Edwin “Jed” Herman, [*Calculus Volume 1*, §5.3, OpenStax](https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus). Further sources are in [References](../REFERENCES.md#classical-calculus-and-analysis).

**Watch:** 3Blue1Brown's [“The essence of calculus”](https://www.youtube.com/watch?v=WUvTyaaNkzM) offers geometric pictures of rates and areas. The lesson above is complete without the video.

[← Foundation](../start/03-why-many-calculi.md) · [Home](../README.md) · [Next: λ-calculus →](02-lambda.md)
