# Pictures and Learning Modes

The guide should work when read alone, discussed aloud, or used on paper. Readers do not need to be assigned a fixed “learning style.”

## A useful rhythm

Read a small example. Predict a result. Explain why. Then change the setting or one assumption and reason again.

A table helps us compare rows. A picture can make a setting familiar. A diagram can show what changed, what stayed the same, or which things connect.

The [practice page](PRACTICE.md) supports this rhythm without extra software.

## Follow familiar objects into new questions

Jo wears a yellow scarf. Sam carries a teal satchel. They return in the garden, library, workshop, and delivery service. Readers can recognize a setting before tackling a new question.

The books are counted in [lesson 3](lessons/03-discrete-and-numerical.md) and selected by a rule in [lesson 6](lessons/06-data-and-relations.md). The workshop introduces both [instructions](lessons/05-computation-and-correctness.md) and [coordination](lessons/07-interaction-and-action.md). The delivery lesson brings records, quantities, and actions together.

Continuity is a memory aid. It does not mean that the mathematical subjects all have the same objects or rules.

The map scene supports two deliberately different questions: [change coordinates](tracks/geometry/tensor-calculus.md) while keeping an arrow fixed, or [turn the arrow](tracks/change/complex-calculus.md) while keeping the coordinates fixed. The familiar picture gives readers a chance to notice the difference.

The observation route revisits the fair for [different views of a card](tracks/observation/epistemic-logic.md), the delivery service for [limited crate labels](tracks/observation/rough-sets.md), and the workshop for [behavioral comparison](tracks/observation/observational-equivalence.md) and [measurement-driven instructions](tracks/observation/measurement-calculus.md). [Do-calculus](tracks/observation/do-calculus.md) returns to the garden to compare observed watering with an intervention. New exact diagrams do the mathematical work; these visits reuse existing scene art.

## Give each picture a job

The [program route](PANTHEON.md#5-computation-types-and-program-guarantees) stays in the workshop while changing the question. Rule cards introduce [combinatory logic](tracks/computation/combinatory-logic.md); repeating a step introduces [System F](tracks/types/system-f.md). Credit balances and job counts support [program proofs](tracks/proof/hoare-logic.md), while addressed boxes show [memory separation](tracks/proof/separation-logic.md). Each uses its own exact diagrams with the existing workshop illustration.

The guide uses nine generated illustrations for familiar settings and a larger set of original SVG diagrams for precise examples. In the diagrams, counts, labels, arrows, and connections are part of the explanation. The scene illustrations do not supply numerical evidence.

Place a visual beside the passage it explains. Let the caption ask a useful question or point out a relationship. For a prediction exercise, show the starting information and keep the answer inside the answer reveal.

Reuse a layout when a changed setting preserves the reasoning. The printer-and-scissors waiting loop becomes the bowl-and-whisk loop in practice. Change the layout when the relationship changes.

The [asset guide](assets/README.md) contains the character reference, saved generation prompts, and instructions for rebuilding the diagrams. Updating a count or label requires no image-generation call.

## Use native formats when they help

Prefer formats that GitHub can display and the repository can preserve:

- Markdown tables for exact comparisons;
- SVG diagrams for small, precise visual examples;
- locally stored WebP illustrations for recurring people and settings;
- Mermaid for meaningful relationships or branching;
- equations accompanied by a plain-language explanation;
- collapsible answers and optional technical sections.

Keep the main lesson complete when optional sections are closed. Every essential visual needs nearby text that explains its information.

## External media

Link to an outside video, animation, or talk only when it adds something useful. Say who made it and what it helps explain.

Media must remain optional. A reader should still be able to complete the lesson if an external link disappears or video is unavailable.

Do not copy thumbnails, figures, audio, or video merely for decoration. Link to the original unless reuse is permitted and properly attributed.

## Accessibility

Keep tables and diagrams compact enough to follow on a small screen. Use short labels and check the rendered result at a narrow width. Do not use color alone to carry a distinction: the bead diagram includes letters as well as colors.

Every embedded image needs useful alternative text. Describe the information needed to follow the example, including the direction of an arrow when that matters. SVG files also carry a title and description. Essential facts remain in the lesson text.

Introduce a Greek-letter name in words before expecting a reader to pronounce it. Explain a symbol beside its first use. Put dense formal notation in an optional section, rather than requiring it to understand the example.

Original visual material is offered under the repository's CC BY 4.0 terms to the extent applicable. See [Attribution](ATTRIBUTION.md) for generation provenance and credit.

[Home](README.md) · [Contributing](CONTRIBUTING.md)
