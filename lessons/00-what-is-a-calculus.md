# 00 — What Is a Calculus?

> A calculus is not one particular kind of mathematics. It is a disciplined world of objects, permitted moves, and rules for when those moves count.

Most people meet the word **calculus** through derivatives and integrals. That is an important calculus, but not the meaning of the word.

Mathematicians and computer scientists also speak of the λ-calculus, sequent calculi, the π-calculus, the situation calculus, the calculus of indications, stochastic calculus, functional calculus, and many others.

These systems do not all manipulate numbers. They are called calculi because they provide a **formal practice of transformation**.

This lesson gives us one comparison frame that we will reuse throughout the repository.

## 1. Five ingredients

For this atlas, we will call something a calculus when it gives us most or all of the following:

1. **Objects** — the things the calculus talks about.
2. **Primitives** — the distinctions or constructions it assumes at the beginning.
3. **Operations** — the moves we may perform.
4. **Rules** — when those moves are legitimate.
5. **Equivalence or outcome** — what counts as the same result, a completed result, or an observable result.

Different calculi emphasize different ingredients.

### Classical differential calculus

Object:
\[
f(x)
\]

Move:
\[
f \mapsto \frac{df}{dx}
\]

Question: **How does a quantity change locally?**

### λ-calculus

Object:
\[
(\lambda x.M)N
\]

Move:
\[
(\lambda x.M)N \to M[x:=N]
\]

Question: **What happens when an abstracted computation receives an argument?**

### Sequent calculus

Object:
\[
\Gamma \vdash \Delta
\]

Move: apply a proof rule producing one sequent from others.

Question: **What follows from what, by explicit inferential rules?**

### π-calculus

Object: interacting processes connected by names.

Characteristic move: communication.

Question: **How can processes communicate in a world where communication can change who can communicate next?**

### Calculus of indications

Object: marked and unmarked forms.

Characteristic move: making and simplifying distinctions.

Question: **What follows from drawing a boundary?**

Already we can see why “calculus” is broader than “taking derivatives.”

## 2. A calculus defines a world

A useful beginner's mistake is to ask:

> What does this calculus calculate?

A better question is:

> **What has to exist for its rules to make sense?**

The λ-calculus assumes expressions that may be abstracted and applied. The π-calculus assumes concurrently existing processes and names through which they communicate. Sequent calculus assumes propositions arranged into inferential contexts. Classical calculus assumes enough structure to speak coherently about variation, limits, and accumulation.

This repository calls that background the calculus's **world**.

The world is not necessarily a metaphysical claim. It is the formal environment in which the calculus operates.

## 3. One word, several meanings of “change”

The same English word can hide very different formal operations.

### Numerical change
\[
x(t) \mapsto \frac{dx}{dt}
\]

### Computational reduction
\[
(\lambda x.x)a \to a
\]

### Logical inference
\[
A,\; A\to B \vdash B
\]

### Process transition
\[
P \xrightarrow{\alpha} P'
\]

### Distinction

A previously undivided domain is marked into sides.

These operations can sometimes be related formally, but they are not interchangeable merely because all of them can be drawn as arrows.

## 4. Seven questions for every calculus

1. **Need** — what problem made this calculus useful?
2. **World** — what sort of things exist inside it?
3. **Primitive** — what does it assume before anything else?
4. **Move** — what is the characteristic operation or rewrite?
5. **Toy example** — what happens in the smallest useful case?
6. **Boundary** — what does the calculus *not* give us for free?
7. **Relations** — what is historically inherited, formally encoded, or merely analogous to another calculus?

This prevents two opposite mistakes: treating every calculus as totally unrelated, and treating every calculus as secretly the same thing.

## 5. Reduction is not differentiation

The λ-calculus has a reduction relation:
\[
(\lambda x.M)N \to_\beta M[x:=N].
\]

Classical calculus has differentiation:
\[
f \mapsto f'.
\]

Both transform expressions. But β-reduction is not a derivative.

Likewise, a π-calculus communication step is not a derivative, and a sequent-calculus inference is not a derivative.

A valid bridge between calculi requires more than visual similarity. It requires a **translation with stated preservation properties**.

Ask:

- Does the translation preserve reduction?
- Does it preserve observable behavior?
- Does it preserve equivalence?
- Does it preserve typing?
- What structure is forgotten?

## 6. Relations between calculi

Every claimed relation in this repository must use one of these labels:

- **historical influence**
- **formal encoding**
- **extension / refinement**
- **structural analogy**
- **conjectured bridge**

An arrow in a diagram is incomplete unless we know what kind of arrow it is.

## 7. Encoding is not identity

Suppose calculus \(A\) can be encoded in calculus \(B\):
\[
E:A\to B.
\]

That does **not** establish \(A=B\).

A useful translation can lose information. A faithful translation can still change representation. Two calculi can encode one another while foregrounding very different primitives.

## 8. Why begin with ordinary calculus?

Because it gives us three intuitions we will repeatedly test elsewhere:

- **Local change** — a derivative asks what is happening *here*.
- **Accumulation** — an integral asks what has built up *over a region or path*.
- **Recovery** — the Fundamental Theorem of Calculus connects local change and accumulation under appropriate conditions.

Later calculi will force us to ask whether analogues exist when the objects are proofs, programs, processes, distinctions, or observations.

Sometimes they do. Sometimes the analogy is misleading.

## 9. A first cosmology

| Calculus | World | Characteristic move |
|---|---|---|
| differential / integral | varying quantities | differentiate / integrate |
| λ | terms and functions | substitute / reduce |
| sequent | inferential contexts | apply proof rules |
| π | mobile communicating processes | communicate names |
| situation | actions and situations | update/reason over world states |
| indications | marked/unmarked forms | draw/cross distinctions |
| distinction graphs | observer-relative distinguishability | relate indistinguishable items |
| Fuzzy Calculus | bounded observational geometry | observer-relative differentiate/integrate with residue |

The point is not to choose a winner. The point is to ask what becomes visible when the primitive changes.

## 10. Checkpoint

Before continuing, you should be able to answer:

1. Why is λ-calculus legitimately called a calculus even though it has no ordinary derivative?
2. Why does a formal encoding not prove that two calculi are identical?
3. What is the difference between a primitive and an operation?
4. What does this repository mean by the “world” of a calculus?
5. Why must arrows in a lineage diagram be labeled?

## Sources

- Stanford Encyclopedia of Philosophy, “The Lambda Calculus.”
- Stanford Encyclopedia of Philosophy, “Natural Deduction Systems in Logic.”
- Robin Milner, Joachim Parrow, and David Walker, “A Calculus of Mobile Processes, I–II,” *Information and Computation* 100(1), 1992.

See [../REFERENCES.md](../REFERENCES.md) for full references.
