# Track — Calculus of Variations: Change the Whole Path

## Need

Ordinary calculus often asks what happens when a number changes.

Calculus of variations asks a different question:

> **What happens when the thing we vary is an entire function or path?**

This is the natural formal world for problems such as finding shortest paths, least-action trajectories, and extrema of functionals.

## World

Instead of a function
\[
f(x)
\]
whose output is a number, consider a **functional**
\[
J[y],
\]
whose input is itself a function \(y\).

A classical form is
\[
J[y]=\int_{a}^{b}L(x,y(x),y'(x))\,dx.
\]

The object being optimized is therefore not one point \(x\), but an entire candidate curve \(y\).

## Primitive move — variation

Perturb the candidate path:
\[
y(x)\mapsto y(x)+\varepsilon \eta(x),
\]
where \(\eta\) is an allowed variation.

Then ask how \(J[y]\) responds as \(\varepsilon\to0\).

The first variation plays a role analogous to a derivative, but now in a space of functions.

## Characteristic equation

For the classical unconstrained problem, stationary paths satisfy the Euler–Lagrange equation:
\[
\frac{\partial L}{\partial y}
-
\frac{d}{dx}
\frac{\partial L}{\partial y'}
=0.
\]

The crucial conceptual jump is:

> a derivative-like operation now acts on a functional by varying its function-valued argument.

## Toy example

The shortest path between two points in the Euclidean plane is a straight line.

One can express path length as a functional and derive the condition satisfied by an extremizing curve.

The familiar geometric answer emerges from a calculus over whole paths.

## Boundary

Calculus of variations does not by itself make probability, communication, proof, or observation primitive.

It is still an analytic calculus of change—but the object of change has moved up a level.

## Relation to classical calculus

**Extension/refinement.**

Classical derivatives are essential ingredients, but the optimization object is now a function or trajectory.

## Pedagogical bridge

This track teaches an important lesson for the entire atlas:

> changing the **type of object being transformed** can create a genuinely new calculus even when familiar derivative ideas remain inside it.

## Sources

- Encyclopedia of Mathematics, “Variational calculus.”
- I. M. Gel'fand and S. V. Fomin, *Calculus of Variations*.
