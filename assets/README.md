# The guide's visual kit

The pictures help readers recognize a setting, see a rule, and carry an idea into a new example. Every core lesson and optional track has a visual beside the relevant explanation.

## Familiar helpers and objects

- **Jo:** taller teal helper with a yellow scarf.
- **Sam:** round terracotta helper with a teal shoulder satchel.
- **Shared palette:** dark blue outlines, teal, terracotta, warm yellow, and light backgrounds.
- **Shared objects:** water, garden borders, books, cards, tools, coins, and crates.

Keep scenes uncluttered and understandable at a small size. Use familiar expressions and simple shapes without making the people seem foolish or helpless. The characters connect the visits; each mathematical subject still gets its own explanation.

## The nine scene illustrations

| File | Teaching role |
|---|---|
| [welcome.webp](illustrations/welcome.webp) | Meet Jo and Sam at the community fair; character and style reference |
| [garden.webp](illustrations/garden.webp) | Ask about water amounts and garden space |
| [library.webp](illustrations/library.webp) | Count books, then select books using a different question |
| [workshop.webp](illustrations/workshop.webp) | Discuss instructions, tools, and coordination |
| [chance.webp](illustrations/chance.webp) | Introduce uncertain outcomes |
| [delivery.webp](illustrations/delivery.webp) | Combine records, quantities, and actions |
| [maps.webp](illustrations/maps.webp) | Compare changing coordinates with turning an arrow |
| [materials.webp](illustrations/materials.webp) | Ask how earlier changes can affect a material |
| [sound.webp](illustrations/sound.webp) | Explore an operator that acts on two channel values |

These are 1536 × 1024 lossless WebP assets, about 9.9 MB in total. Lesson embeds usually display them at 400 pixels wide. They contain no mathematical labels or quantities that must be counted.

The first set used six image-generation calls: one reference scene followed by five scenes made with that reference. A later expansion used three more calls with the same reference. Reusing these assets across pages keeps the number of generation calls down. No price or cheaper-model claim is implied; this interface exposed neither a model selector nor itemized costs.

The [prompt record](illustrations/prompts.json) stores each request and its reference, where used. To add a scene, supply `welcome.webp` as the visual reference and describe only the new setting and activity. Keep letters, formulas, counted objects, and exact relationships out of the illustration. Review the result before embedding it. Generation is not deterministic, so keeping a prompt does not guarantee identical pixels.

## Rebuild exact diagrams locally

The SVGs in `diagrams/` show exact counts, input choices, dependencies, or before-and-after states. They are standalone vector files with accessible titles and descriptions. [The manifest](diagrams/manifest.json) records their names, dimensions, and descriptions.

From the repository root, run:

```sh
python3 tools/build_visuals.py
```

This uses only Python's standard library. It makes no network requests and no image-generation calls. Edit the relevant drawing function in [build_visuals.py](../tools/build_visuals.py), run the command, and commit both the source and the resulting SVG files. Edit titles and descriptions when the teaching meaning changes.

Open changed SVGs in a browser or vector viewer. Check counts, direction, labels, overlaps, and readability at a narrow width. Keep a diagram focused on one relationship. Do not force a complicated formalism into a tiny picture.

## Embed beside the explanation

Use a relative image path from the Markdown page and a width of up to 640 pixels for a diagram or 400 pixels for a scene. GitHub constrains images to the available page width. Include useful alternative text and a short caption.

Keep the essential facts in the prose too. Labels and shapes must support color distinctions. For practice, a diagram may show the starting data; put a diagram that explains the answer inside the corresponding answer reveal.

The same books appear in counting and querying lessons. The same waiting-loop layout appears with workshop tools and kitchen tools. These repetitions give the reader something stable while the question or setting changes.

The observation and causal tracks reuse the fair, delivery, workshop, and garden scenes. Their new diagrams show separate views of a card, rough-set groups and boundaries, branching behavior, quantum command dependencies, and causal adjustment. This expansion adds no generated raster assets.

## Provenance and reuse

The data and interaction expansion adds ten SVGs: request joins, a mismatched-witness example, field slots, request coverage, preparation orders, a blocked and repaired handshake, two ambient-movement diagrams, decryption, and replay. It reuses the library, workshop, and delivery illustrations. Precise nesting and event order come from the diagrams and their text descriptions.

The change tracks reuse the garden scene. Nine diagrams show growing tile squares, difference tables, sampled rates, trapezoidal totals, a missed pulse, tank balance, Euler steps, a transform route, and a shrinking gap. The same tank model connects the differential-equation and operational-calculus tracks. All nine diagrams rebuild locally without image-generation calls.

The program tracks reuse the workshop scene. Their diagrams show combinator reductions, matching and mismatched types, forward execution and backward conditions, a loop invariant, and separate versus aliased memory cells. The nine additional SVGs need no new image-generation calls.

The scene illustrations were AI-generated for the guide. The SVG diagrams were authored as code for its teaching examples. See [Attribution](../ATTRIBUTION.md) for the generation record, project credit, and applicable [CC BY 4.0 terms](../LICENSE.md).

[Home](../README.md) · [Pictures and learning modes](../MEDIA.md) · [Contributing](../CONTRIBUTING.md)
