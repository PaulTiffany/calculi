# Attribution and Source Provenance

This guide combines original teaching examples with mathematics from several traditions. Its grouping and reading route are editorial choices, not an accepted taxonomy of all calculi.

Original explanatory material is licensed under [CC BY 4.0](LICENSE.md). Cited sources retain their own rights.

## Core route

| Page | Main mathematical sources or role |
|---|---|
| [Welcome](START.md) | Original introduction and counter rulebook |
| [1. Rates and totals](lessons/01-classical-calculus.md) | Modern differential and integral calculus; Strang–Herman, OpenStax |
| [2. Space and shape](lessons/02-space-and-shape.md) | Multivariable and vector calculus; OpenStax, with further geometry references |
| [3. Discrete and numerical methods](lessons/03-discrete-and-numerical.md) | Differences, summation, and approximation; MIT teaching materials |
| [4. Logic and proof](lessons/04-logic-and-proof.md) | Propositional/predicate logic and proof systems; Open Logic Project |
| [5. Computation and correctness](lessons/05-computation-and-correctness.md) | Church's lambda-calculus tradition; Pfenning; Hoare-style logic and Dijkstra |
| [6. Data and relations](lessons/06-data-and-relations.md) | Relational query languages; Silberschatz, Korth, and Sudarshan |
| [7. Interaction and action](lessons/07-interaction-and-action.md) | Hoare/Milner process traditions; McCarthy/Hayes, Kowalski/Sergot, Thielscher action formalisms |
| [8. Chance and cause](lessons/08-chance-and-cause.md) | Probability, stochastic integration, and Pearl's causal calculus |
| [9. Choose and combine](lessons/09-choose-and-combine.md) | Original comparison and modeling examples |
| [Field map](PANTHEON.md), [practice](PRACTICE.md), and [connections](RELATIONS.md) | Educational synthesis; formal claims link to supporting sources |

The tank, hill, garden, counts, badge puzzles, ticket counter, data tables, poster project, bead problems, sprinkler model, and delivery service are original teaching examples. They should not be attributed to the cited authors.

## Optional tracks

| Track | Provenance and scope |
|---|---|
| [Variations](tracks/change/variational-calculus.md) | Euler–Lagrange tradition; Gel'fand–Fomin and Strang |
| [Stochastic calculus](tracks/change/stochastic-calculus.md) | Itô/Stratonovich traditions; modern stochastic integration |
| [Lambda calculus](tracks/computation/lambda-calculus.md) | Church and subsequent lambda-calculus literature |
| [Sequent calculus](tracks/proof/sequent-calculus.md) | Gentzen and proof theory |
| [Calculus of Constructions](tracks/types/calculus-of-constructions.md) | Coquand and Huet; later inductive extensions |
| [Pi calculus](tracks/interaction/pi-calculus.md) | Milner, Parrow, and Walker |
| [Rho calculus](tracks/interaction/rho-calculus.md) | Meredith and Radestock; later corrections and analysis by Lybech |
| [Action calculi](tracks/action/situation-event-fluent.md) | McCarthy/Hayes; Kowalski/Sergot; Thielscher |
| [Calculus of indications](tracks/logic/calculus-of-indications.md) | Spencer-Brown's *Laws of Form*; Kauffman's exposition |
| [Distinction graphs](tracks/observation/distinction-graphs.md) | Goertzel's 2019 research formalism |
| [Tiffany's Fuzzy Calculus](tracks/observation/tiffany-fuzzy-calculus.md) | The named framework in Tiffany's *Principia Symbolica* and related materials |

These tracks have different standing and scope: some introduce established advanced subjects; others examine particular symbolic systems or research frameworks. Their shared location under “tracks” only means that they are optional reading.

## Reconstruction and evidence

An analogy helps explain a formal idea; it does not prove a theorem about it. A tiny arithmetic example can introduce an accumulation problem without implementing the full integral calculus.

When a later source corrects an earlier formal claim, preserve that correction where the claim is taught. The rho track does this for encoding results.

The near-8th-grade target is a writing goal. It is not a claim that the material has passed a learner study. Feedback from actual new readers is valuable.

Full bibliographic records are in [References](REFERENCES.md).

## Visual material

The six Jo and Sam scene illustrations in `assets/illustrations/` were generated with OpenAI's image-generation tool on September 23, 2026, for this guide. The welcome image established the character and style reference for the five later scenes. The exact prompts are preserved in [the prompt record](assets/illustrations/prompts.json). The tool did not expose a specific model version or an itemized generation cost.

The illustrations were encoded as lossless WebP files without changing their decoded pixels. They introduce familiar settings; they are not historical photographs, sourced mathematical figures, or exact quantity diagrams.

The SVG teaching diagrams are original code-authored illustrations of the guide's examples. Their editable source is [the diagram builder](tools/build_visuals.py); their descriptions are in [the diagram manifest](assets/diagrams/manifest.json). No third-party figures were copied for this set.

Original visual material is offered under the repository's CC BY 4.0 terms to the extent applicable. Use the project credit below, identify changes, and retain the AI-generation disclosure when redistributing the scene illustrations. See [the asset guide](assets/README.md) for maintenance details.

## Reuse

A suitable credit is:

> Paul Carver Tiffany III, *Calculi: A Field Guide to Mathematical Ways of Thinking*, 2026, https://github.com/PaulTiffany/calculi, CC BY 4.0.

[Home](README.md) · [License](LICENSE.md) · [Contributing](CONTRIBUTING.md)
