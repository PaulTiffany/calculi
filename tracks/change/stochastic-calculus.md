# Track — Stochastic Calculus: Change Along Noisy Paths

## Need

Classical calculus behaves beautifully for sufficiently regular trajectories.

But many important processes are random and extremely irregular.

Brownian motion, for example, is continuous but almost surely nowhere classically differentiable.

So how can we integrate and reason about change along such paths?

That is the domain of **stochastic calculus**.

## World

A basic world contains:

- a probability space;
- a filtration representing information available through time;
- stochastic processes;
- random paths such as Brownian motion.

The information structure matters: an integrand may be required to depend only on information available up to the current time.

## Primitive move — stochastic integration

A central object is an integral such as
\[
\int_0^t H_s\,dX_s,
\]
where \(X\) is a stochastic process or semimartingale and \(H\) is a suitable predictable process.

This is not generally an ordinary Riemann or Riemann–Stieltjes integral.

The definition is built to survive the roughness of stochastic trajectories.

## Why ordinary rules change

For Itô calculus, the familiar chain rule acquires an additional second-order term.

Schematically, for an Itô process \(X_t\),
\[
df(X_t)
=
f'(X_t)\,dX_t
+
\frac12 f''(X_t)\,(dX_t)^2,
\]
with the stochastic bookkeeping giving the quadratic-variation contribution.

The deeper point is not the mnemonic notation.

It is:

> the geometry of the path changes the valid calculus rules.

## Boundary

Stochastic calculus makes uncertainty and filtration mathematically explicit, but it does not automatically make the observer an ontological primitive or explain what distinctions an observer can make.

Probability-relative and observer-relative are not synonyms.

## Relation to classical calculus

**Extension/refinement.**

Stochastic calculus recovers ordinary-looking operations in a new path regime, but alters the rules to account for stochastic variation.

## Why this belongs near Fuzzy Calculus

Only as a **structural comparison**:

- stochastic calculus changes calculus because paths are rough/random;
- Fuzzy Calculus changes calculus because access is observer-bounded.

The reasons for the correction terms differ.

That is exactly the sort of distinction this atlas is built to preserve.

## Sources

- Encyclopedia of Mathematics, “Stochastic integral.”
- Karatzas and Shreve, *Brownian Motion and Stochastic Calculus*.
