# 02 — λ-Calculus: Instructions with Inputs

**Start with:** the idea of an instruction with an input. No derivatives are needed.\
**By the end:** carry out a small substitution and recognize the same rule with different inputs.

## The idea

Imagine an instruction that says:

> Take two inputs. Return the first.

Give it **tea**, then **cake**. It returns **tea**. Give it **red**, then **blue**. It returns **red**.

The objects changed; the instruction stayed the same. This is an analogy for an operation we can write precisely in **λ-calculus**, pronounced “lambda calculus.”

## Three useful words

- **Abstraction:** make an instruction with an input slot.
- **Application:** give an input to that instruction.
- **Substitution:** put the input where its slot is used.

In λ-calculus, expressions are called **terms**. A term can be a variable, an application, or an abstraction. Instructions can themselves be inputs.

## See one move at a time

Here $a$ and $b$ are distinct variable names standing for inputs.

| Expression | Read it as |
|---|---|
| $\lambda x.\lambda y.x$ | Take an input called $x$, then one called $y$; return $x$ |
| $(\lambda x.\lambda y.x)\,a$ | Fill the first slot with $a$ |
| $\lambda y.a$ | The remaining instruction takes an input and returns $a$ |
| $(\lambda y.a)\,b$ | Fill the remaining slot with $b$ |
| $a$ | The result |

The symbol **λ** introduces an input slot. The dot starts the body of the instruction. This substitution step is called **β-reduction**, pronounced “beta reduction.”

## Try it

Change the instruction to “take two inputs; return the second.” In notation, use $\lambda x.\lambda y.y$.

Give it $p$, then $q$. What remains after each step?

<details>
<summary>Check your reasoning</summary>

First, $(\lambda x.\lambda y.y)\,p$ becomes $\lambda y.y$. The first input is unused.

Then $(\lambda y.y)\,q$ becomes $q$. The second input is returned.

Compare this with the table: the location of the used slot determines the result.

</details>

## Try it somewhere else

A label maker uses the instruction “take a heading, then a note; return the heading.” You change the note but keep the heading. Does the result change? What if you swap the order of the inputs?

<details>
<summary>Check and connect</summary>

Changing the unused note leaves the result unchanged. Swapping the inputs makes the note arrive in the first slot, so it is returned instead.

This is the same first-input rule in a new setting. The label maker is a teaching analogy; the formal calculation concerns terms and substitution.

</details>

<details>
<summary>Optional notation — binding, safe substitution, and loops</summary>

The general rule is

$$
(\lambda x.M)N\to_\beta M[x:=N].
$$

Here $M[x:=N]$ means replace the **free** occurrences of $x$ in $M$ by $N$. An occurrence is **bound** when it belongs to an enclosing input declaration for that variable.

Substitution must preserve these relationships. In $(\lambda x.\lambda y.x)y$, the incoming $y$ must remain free. First rename the inner slot to a fresh name $z$:

$$
(\lambda x.\lambda z.x)y\to_\beta\lambda z.y.
$$

Renaming a bound slot consistently is **α-conversion**. Producing $\lambda y.y$ instead would change the meaning.

A **normal form** has no β-reduction left to perform. Not every term reaches one. For example,

$$
\Omega=(\lambda x.xx)(\lambda x.xx)\to_\beta\Omega.
$$

This term repeats its own reduction.

</details>

## What this model brings into focus

The native move is applying and rewriting terms. [Typed calculi](../tracks/types/calculus-of-constructions.md) add rules about which terms fit together. [Process calculi](03-pi.md) put communication at the center.

There are formal encodings of λ-computation in communicating processes; [Relations](../RELATIONS.md) records that connection.

## Sources and optional viewing

Alonzo Church originated λ-calculus. The everyday examples here are original analogies. For the rules, see Frank Pfenning's [“The λ-Calculus,” CMU lecture notes](https://www.cs.cmu.edu/~fp/courses/15814-f25/lectures/01-lambda.pdf), especially §§2–5, and [References](../REFERENCES.md#λ-calculus).

**Watch:** Computerphile / Graham Hutton, [“Lambda Calculus”](https://www.youtube.com/watch?v=eis11j_iGMs), for another explanation of inputs and substitution.

[← Classical calculus](01-classical-calculus.md) · [Home](../README.md) · [Next: π-calculus →](03-pi.md)
