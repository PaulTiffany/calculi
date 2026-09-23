# Try It Somewhere New

These challenges use the same ideas in different settings. You can answer aloud, on paper, or with a partner.

For each one, give an answer **and a reason**. Then name an assumption. Open the explanation after your first attempt.

<!-- visual:diagram-learning-loop -->
<img src="assets/diagrams/learning-loop.svg" width="640" alt="Read an example, make a prediction, explain your reasoning, and change one thing. Repeat with the changed problem.">

*Try a prediction before opening an answer. Then change one thing.*
<!-- /visual:diagram-learning-loop -->

## 1. Rate and total: seats

<!-- visual:diagram-practice-chairs -->
<img src="assets/diagrams/practice-chairs.svg" width="640" alt="The practice problem starts with twelve chairs and adds four chairs per minute for three minutes. The final count is left for the reader.">

*Use the given start, rate, and time. Leave the final count for your own calculation.*
<!-- /visual:diagram-practice-chairs -->

A hall starts with 12 chairs set out. Helpers add 4 chairs per minute for 3 minutes. Nobody removes a chair.

How many chairs are added? How many are now set out? If two chairs are removed during the work, which answer changes?

<details>
<summary>Check</summary>

Twelve chairs are added, and 24 are set out at the end.

Removing two does not change how many were added. It changes the final total to 22. The net change is then ten.

This uses the distinction between input, net change, and starting amount from [lesson 1](lessons/01-classical-calculus.md).

</details>

## 2. Several inputs: a photograph

<!-- visual:diagram-practice-photo -->
<img src="assets/diagrams/practice-photo.svg" width="640" alt="A rectangular photograph is three units wide and five units tall. The reader can increase either dimension by one.">

*Change the width or the height while keeping the other fixed.*
<!-- /visual:diagram-practice-photo -->

A rectangular print is 3 units wide and 5 units tall. Its area is 15 square units.

How much area is added by increasing only its width by one? What if you increase only its height by one? Why do the answers differ?

<details>
<summary>Check</summary>

Increasing width gives $4\times5=20$, adding 5 square units.

Increasing height gives $3\times6=18$, adding 3 square units.

The change depends on which input varies and which stays fixed. See [lesson 2](lessons/02-space-and-shape.md).

</details>

## 3. Discrete steps: visitors

<!-- visual:diagram-practice-visitors -->
<img src="assets/diagrams/practice-visitors.svg" width="640" alt="Four room headcounts are ten, fourteen, thirteen, and eighteen, in that order.">

*These are snapshots. What might happen between them?*
<!-- /visual:diagram-practice-visitors -->

A room's headcount at four check-ins is 10, 14, 13, and 18.

Find the three differences and their sum. Do these counts tell you the total number of people who entered?

<details>
<summary>Check</summary>

The differences are +4, −1, and +5. Their sum is +8, which is also $18-10$.

They do not tell us the total number entering. During one interval, five could enter and one leave, giving a net gain of four. Other combinations give the same net gain. See [lesson 3](lessons/03-discrete-and-numerical.md).

</details>

## 4. Logic: shapes

Every square has four sides. This shape has four sides.

Does it follow that the shape is a square? Give an example that settles the question.

<details>
<summary>Check</summary>

<img src="assets/diagrams/practice-shapes.svg" width="640" alt="A square and a nonsquare rectangle both have four sides. The rectangle is a counterexample to reversing the rule that every square has four sides.">

No. A rectangle with unequal adjacent sides has four sides but is not a square.

One counterexample is enough to show that the reversed rule is false. See [lesson 4](lessons/04-logic-and-proof.md).

</details>

## 5. Program guarantees: game points

<!-- visual:diagram-practice-score -->
<img src="assets/diagrams/practice-score.svg" width="640" alt="An unknown starting score is reduced by three points. The required result is nonnegative. The starting condition is left for the reader.">

*Read the promise backward: what must have been true at the start?*
<!-- /visual:diagram-practice-score -->

An instruction subtracts three points from a score. You want the resulting score to be at least zero.

What is the least starting score that works? Would “the score is an integer” be enough? Suppose the code actually subtracts four: which part of the argument changes?

<details>
<summary>Check</summary>

Start with at least three points.

An integer type alone is not enough: one is an integer and would become −2.

If the code subtracts four, the required starting score becomes at least four. A proof must match the actual modeled instruction. See [lesson 5](lessons/05-computation-and-correctness.md).

</details>

## 6. Data: a playlist

| Song | Shorter than 3 minutes? | Marked favorite? |
|---|---|---|
| A | Yes | No |
| B | No | Yes |
| C | Yes | Yes |
| D | No | No |

<!-- visual:diagram-practice-playlist -->
<img src="assets/diagrams/practice-playlist.svg" width="640" alt="Song A is short but not a favorite. B is a favorite but not short. C is both. D is neither. No answer selection is marked.">

*The picture gives the records, not the selected answer.*
<!-- /visual:diagram-practice-playlist -->

Which songs meet both conditions? Which meet at least one? Does this table let you find songs shorter than 2 minutes?

<details>
<summary>Check</summary>

Both conditions: C. At least one: A, B, and C.

The table does not give enough detail for the 2-minute question. A song marked shorter than 3 minutes could last 1 minute or 2½ minutes. See [lesson 6](lessons/06-data-and-relations.md).

</details>

## 7. Coordination and effects: a shared kitchen

<!-- visual:diagram-practice-kitchen -->
<img src="assets/diagrams/practice-kitchen.svg" width="640" alt="One cook holds the bowl and waits for the whisk. The other holds the whisk and waits for the bowl.">

*Compare the earlier printer-and-scissors pattern. The tools have changed.*
<!-- /visual:diagram-practice-kitchen -->

One cook holds the mixing bowl and waits for the whisk. Another holds the whisk and waits for the bowl. Both refuse to release their tool first.

What blocks progress? Suggest a changed rule.

Now a timer rings. Does that event alone establish that someone removed the cake from the oven?

<details>
<summary>Check</summary>

The cooks are stuck in a circular wait. They could agree to acquire tools in the same order, or one could release a tool so the other can finish.

The timer event does not itself remove the cake. A model needs an action connecting someone hearing the timer to removing the cake. See [lesson 7](lessons/07-interaction-and-action.md).

</details>

## 8. Chance and cause: two questions

<!-- visual:diagram-token-question -->
<img src="assets/diagrams/token-question.svg" width="640" alt="One green and three yellow tokens are equally likely to be picked. The image supplies the starting contents only.">

*This is the starting bag. Decide what remains after the stated draw.*
<!-- /visual:diagram-token-question -->

A bag has one green token and three yellow tokens, each equally likely to be drawn. You draw a yellow token and keep it out. What is the chance of green next?

Separately, suppose a model says rain causes both umbrellas to open and pavements to get wet. There is no other causal link in the model. Would opening an umbrella make the pavement wet?

<details>
<summary>Check</summary>

One green and two yellow tokens remain, so the chance is 1/3.

Under the stated causal model, opening an umbrella does not cause a wet pavement. Observing open umbrellas can be evidence of rain; forcing one open does not make it rain. See [lesson 8](lessons/08-chance-and-cause.md).

</details>

## Six more trails to try

These follow the optional tracks. You can choose one without completing them all.

### 9. Describe the same movement

A movement is (4, 3) in east–north coordinates. Describe it using north–west coordinates, with the same starting point and unit. Did the movement itself change?

<details>
<summary>Check</summary>

It is **(3, −4)**: three north and four opposite west. The movement stays the same. Only its description changes. See [tensor calculus](tracks/geometry/tensor-calculus.md).

</details>

### 10. Combine boundaries

Three unit-square plots form one straight row. Trace each plot counterclockwise and cancel shared edges traversed in opposite directions. How many outside unit edges remain?

<details>
<summary>Check</summary>

**Eight.** The combined rectangle is three units long and one unit wide. Its outside has $3+1+3+1=8$ unit edges. The two shared edges each appeared twice in the original twelve traversals. See [exterior calculus](tracks/geometry/exterior-calculus.md).

</details>

### 11. Turn the movement

Start with an arrow pointing two units right. Keep the axes fixed. Multiply its complex number by i three times, making a counterclockwise quarter-turn each time. Where does it end?

<details>
<summary>Check</summary>

It points **two units down**, or $-2i$. The successive directions are up, left, then down. This changes the arrow itself. See [complex calculus](tracks/change/complex-calculus.md).

</details>

### 12. Compare histories

Use the fractional track's **toy score**, with oldest-to-newest weights 1/4, 1/2, and 1. One record has changes (2, 2, 0); another has (0, 0, 4). Starting from zero, do they end at the same value? Do they receive the same score?

<details>
<summary>Check</summary>

Both finish at **4**. Their scores differ: $2/4+2/2+0=1.5$ and $0+0+4=4$.

That is a calculation in the stated weighted model. Calling it a fractional derivative would require a different, precise definition. See [fractional calculus](tracks/change/fractional-calculus.md).

</details>

### 13. Repeat a new operator

An operator C changes the sign of both numbers in a pair. What do C² and C³ do to (2, −5)? Here powers mean repeated application.

<details>
<summary>Check</summary>

The first application gives (−2, 5). **C² returns (2, −5)**. **C³ gives (−2, 5)** again.

Two sign changes act as the identity, just as two swaps did, although one sign change and one swap are different operations. See [functional calculus](tracks/operators/functional-calculus.md).

</details>

### 14. Count uses of a resource

You have two ride vouchers. Each ride consumes one voucher. The instruction sheet can be read any number of times. Can reading it three times give you three rides under these rules?

<details>
<summary>Check</summary>

No. You can use the instructions again, but you still have only **two vouchers**. A third ride requires another voucher or a changed rule. See [linear logic](tracks/proof/linear-logic.md).

</details>

## A reusable activity for learners and teachers

Choose one problem above. Have one person change a number, object, condition, or rule. Ask the other person:

1. What stays useful from the original reasoning?
2. What must be recalculated or reconsidered?
3. What missing information could stop us answering?
4. Where else could this pattern appear?

Then swap roles. If an answer is mistaken, try a small counterexample before introducing a new technical word.

For a larger task, choose two tools and explain the assumption that connects them. [Lesson 9](lessons/09-choose-and-combine.md) shows how.

The aim is to explain why an idea applies. Speed and symbol recall are not the only signs of understanding.

*All challenges are original teaching examples. Mathematical sources are linked from the corresponding lessons.*

[Home](README.md) · [Field map](PANTHEON.md)
