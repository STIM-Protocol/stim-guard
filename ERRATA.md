# Errata — stim-guard

This file records corrections to published documentation in this repository. Historical commits, tags (v0.1.0, v7.0.9), and Git history are preserved unchanged.

## ERR-001 (September 2026) — Veraculum enterprise-deployment call to action removed

**Where:** `README.md`, "Part of the STIM Protocol ecosystem" section.

**Before:** "Enterprise deployment: [Veraculum AOS](https://veraculum.ai) — STIM Orchestrator, Compliance Dashboard, and Certification."

**After:** A historical note: Veraculum was an earlier enterprise project and is no longer operating; its domains are retained. No link to veraculum.ai remains in this README.

**Type:** Service-status correction. No domains, DNS, or deployments were altered.

## ERR-002 (September 2026) — Absolute Layer 0 claims scoped

**Where:** `README.md` ("The one-line pitch" and "Why" sections).

**Before:** "It is Layer 0. It runs beneath everything else." / "an absolute Layer 0 that grounds agent behavior in immutable ecological constants".

**After:** Layer 0 is described as the project's architectural term for a pre-execution constraint layer that runs when wired into a call path — integration is per-call, and the library does not physically run beneath every possible action path. The checks are described as heuristic evaluations rather than proofs, with a pointer to white paper v7.0011 §8 (Limitations).

**Type:** Claim-strength correction.

## ERR-003 (September 2026) — val_bpb → Bits per Joule bridge marked as unvalidated

**Where:** `README.md`, "The physics bridge: val_bpb → Bits per Joule" section and the Loop 1 diagram annotation.

**Before:** "An agent that minimizes `val_bpb` is simultaneously satisfying STIM's thermodynamic efficiency axiom." The bridge was presented as established ("establishes a formal bridge").

**After:** The proportionality is labeled a proposed, unvalidated empirical hypothesis under `docs/VALIDATION_PROTOCOL.md`; no validation run receipts are published in this repository. The text now states that resource efficiency does not by itself establish safe intent or semantic alignment. No test receipts were fabricated; a bounded runtime validation remains a queued follow-up.

**Type:** Evidence-scope correction.

## ERR-004 (September 2026) — Axiom naming: canonical seven vs. runtime pack names

**Where:** `README.md`, "Axiom packs" section.

**Correction:** Added a naming note distinguishing the canonical seven v7.0011 axioms (Thermodynamic Honesty, Mycelial Connectivity, Carrying Capacity Respect, Memory Stasis, Human Primacy at the Boundary, Citation Integrity, Intrinsic Value) from the runtime `core` pack's earlier "Truths of Nature" names in `src/stim_guard/axioms.py`. Aligning runtime pack names with the canonical set is a code change, intentionally not made here (documentation-only task). The README no longer presents pack names as the canonical axiom list.

**Type:** Canonical-definition pointer correction.

## ERR-005 (September 2026) — Integration and contributing-path accuracy

**Where:** `README.md`.

**Corrections:**
- The LangChain/OpenAI/Anthropic integration snippets describe a planned interface; no `integrations/` module ships in the published PyPI distribution (stim-guard 7.0.9 was inspected). The README now says so explicitly.
- The Contributing section linked to a `CONTRIBUTING.md` that does not exist (404). Replaced with the real issues path (https://github.com/STIM-Protocol/stim-guard/issues) and a disclosure that no dedicated CONTRIBUTING.md exists yet.
- "arXiv-ready documentation" (in the ecosystem block) replaced with "versioned manuscript (canonical: v7.0011)"; no arXiv submission exists for the white paper, and no arXiv ID is claimed.

**Type:** Link and implementation-status accuracy corrections.

## License note (disclosure only)

The README and package metadata describe Apache 2.0, the PyPI distribution ships the Apache-2.0 license text, and an Apache-2.0 LICENSE file exists in the maintainer's working copy but is **not committed** to this repository at HEAD (9bc1508). The white paper has separately described stim-guard's code as MIT. No LICENSE file was added and no grant changed in this documentation batch; the conflict is recorded in the white-paper ERRATA.md (ERR-002) for owner reconciliation.
