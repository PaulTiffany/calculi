# 04 — ρ-Calculus: Instructions That Can Be Passed Around

**Start with:** [processes, names, and messages](03-pi.md).\
**By the end:** distinguish a process, a name made from its description, and the use of that description as behavior.

## The idea

A recipe can be written on a card, handed to someone, and followed later. Holding the card and cooking the meal are different activities.

This is an analogy for **reflection**: a formal system can treat descriptions of its own processes as things it can work with.

In **ρ-calculus**, pronounced “rho calculus,” names are made by **quoting processes**. Such names can participate in communication. A **drop** operation lets a process represented by a name become behavior.

## Follow the roles

| Role in the calculus | Recipe-card analogy |
|---|---|
| A process $P$ | Instructions for doing something |
| Its quoted name $@P$ | Those instructions represented on a card |
| Communication involving that name | Passing the card |
| Dropping a received quoted process | Using the represented instructions as behavior |

The card is a teaching aid. In the formal calculus, quoting is a precise construction of a name from process syntax.

## Try it

Suppose a process sends a quoted description of another process. The receiver keeps the name for later.

Has the described process necessarily run just because its name was received? What additional use of the name would bring its behavior into play?

<details>
<summary>Check your reasoning</summary>

Receiving a name does not by itself run the process it represents. The receiver's behavior must use the name through the calculus's drop mechanism.

The useful distinction is between **having a representation** and **using it as behavior**.

</details>

## Try it somewhere else

A music player receives a stored set of playback instructions. It can keep the instructions or use them to play a tune.

Which parts resemble the card example? What would we need to specify before claiming a formal model?

<details>
<summary>Check and connect</summary>

Stored instructions resemble a representation; using them to control playback resembles bringing represented instructions into behavior.

To build a formal model, we would need to specify the processes, how their quoted names are formed, and the communication and drop rules. Merely sending an ordinary file is not enough to establish an encoding in ρ-calculus.

</details>

<details>
<summary>Optional depth — structured names and translation results</summary>

Meredith and Radestock's reflective higher-order calculus makes names from quoted processes, instead of starting with an independent stock of atomic names. This ties naming to process structure.

The language differs from ordinary π-calculus in more than one operator. Features include structured names, runtime generation of free names, and the absence of the ordinary π restriction operator.

Meredith and Radestock proposed an encoding of an asynchronous π fragment. Lybech's later analysis identifies errors in that encoding and gives a corrected encoding with stated preservation criteria. It also proves a separation in the reverse direction under its chosen criteria.

An **encoding** is a formal translation. Its claim depends on the source fragment, target language, and behavior it preserves. See [Relations](../RELATIONS.md).

</details>

## A question to carry forward

Which matters for your task: sending an address, sending a representation of a process, or bringing represented behavior into play?

Naming those roles makes this idea useful beyond a particular notation. Questions about which differences can be noticed lead to the later lessons on distinction and observation.

## Sources

The recipe and music examples are original analogies. See Meredith and Radestock, *A Reflective Higher-order Calculus* (2005), and Lybech, [*Encodability and Separation for a Reflective Higher-Order Calculus*](https://arxiv.org/abs/2209.02356) (2022), with its 2024 journal development. Full records are in [References](../REFERENCES.md#ρ-calculus-and-reflective-process-calculi).

[← π-calculus](03-pi.md) · [Home](../README.md) · [Next: calculus of indications →](05-indications.md)
