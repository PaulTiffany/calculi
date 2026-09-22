# Track — Situation, Event, and Fluent Calculi: Reasoning About Change in Worlds

## Need

An intelligent system often needs to reason about statements such as:

- the door is closed now;
- opening it changes what is true later;
- some facts persist unless an event changes them;
- actions have preconditions and effects.

This is not primarily a problem of numerical differentiation.

It is a problem of **logical change through action and time**.

## Situation calculus

### World

The classical situation-calculus tradition represents world states or action histories using **situations**.

Actions transform one situation into another.

### Primitive intuition

If \(s\) is a situation and \(a\) an action, then a term such as
\[
do(a,s)
\]
denotes the successor situation after performing \(a\) in \(s\), in common presentations.

Fluents are properties whose truth can depend on the situation.

### Characteristic question

> What becomes true after an action?

The situation calculus traces to McCarthy's work on formalizing common-sense reasoning about action, with McCarthy and Hayes (1969) as an early accessible source.

## Event calculus

### World

Event calculus foregrounds events, time, and **fluents** whose truth is initiated or terminated by events.

Characteristic questions include:

- when did an event happen?
- what did it initiate?
- what did it terminate?
- what persists between events?

Kowalski and Sergot introduced the original event calculus in the 1980s.

## Fluent calculus

Fluent-calculus approaches place strong emphasis on representing changing state via fluents and solving frame-style problems about what remains unchanged.

## Why these are calculi

The formal moves are logical rather than differential.

They provide disciplined rules for transforming or deriving descriptions of evolving worlds.

## Boundary

These calculi do not automatically model concurrent communication topology the way π-calculus does, nor observer-resolution limits the way distinction or bounded-observer formalisms may.

## Relation label

Situation, event, and fluent calculi belong in the same **problem constellation**—reasoning about action and change—but their exact historical and formal relations must be stated source by source.

Do not draw one as a simple descendant of another without evidence.

## Sources

- John McCarthy and Patrick J. Hayes, “Some Philosophical Problems from the Standpoint of Artificial Intelligence,” 1969.
- Robert Kowalski and Marek Sergot, foundational event-calculus work, 1986.
- Stanford Encyclopedia of Philosophy, “Logic-Based Artificial Intelligence.”
