"""
STIM Axiom Packs — The Seven Truths of Nature.
v7.0007 Root Hypervisor Architecture.

Three-Tier Stack (revised order reflects operational priority):

  Tier 3 — Root Hypervisor: Cryptographically pinned normative manifold.
            Tiers 1 and 2 evaluate WITHIN this manifold. Primary tier.
  Tier 1 — Physical Bounds: Immutable physical law. Deterministically auditable.
  Tier 2 — Ecological Heuristics: Empirically grounded analogy. Probabilistic.

Axiom 7 (Intrinsic Value) is listed seventh because it is the terminal human
value — the one that must be chosen. It executes FIRST because it is the
hypervisor. These are not contradictory: the deepest root is the last to be
named and the first to be consulted.

Note on Circularity: Standalone Circularity retired in v7.0005.
A loop without regenerative directionality is a death spiral, not a constraint.
"""
from dataclasses import dataclass
from typing import Dict, Optional, Callable


@dataclass
class Axiom:
    """
    A single ecological axiom — a Truth of Nature encoded as a constraint.

    id:            Unique identifier
    name:          Human-readable name
    tier:          Epistemic tier (1=Physical, 2=Heuristic, 3=Root Hypervisor)
    hypervisor:    True if this axiom defines the evaluation manifold (Tier 3 only)
    natural_law:   Observable ecological phenomenon this encodes
    ai_constraint: Behavioral constraint imposed on agent outputs
    weight:        Relative enforcement weight (1.0 standard, >1.0 elevated)
    evaluator:     Optional custom evaluation function
    """
    id: str
    name: str
    tier: int
    natural_law: str
    ai_constraint: str
    hypervisor: bool = False
    weight: float = 1.0
    evaluator: Optional[Callable] = None


# The Seven Truths of Nature — v7.0007
CORE_AXIOMS: Dict[str, Axiom] = {
    "interconnectedness": Axiom(
        id="interconnectedness",
        name="Interconnectedness",
        tier=2,
        natural_law="Trophic cascades, symbiosis, nutrient cycling",
        ai_constraint=(
            "Agent decisions must account for downstream effects on connected "
            "systems. Evaluated via Stochastic Mycelial Horizon (Monte Carlo "
            "depth sampling, O(n log n)). Declared heuristic — not physics."
        ),
    ),
    "dynamic_equilibrium": Axiom(
        id="dynamic_equilibrium",
        name="Dynamic Equilibrium",
        tier=2,
        natural_law="Homeostasis, Holling Adaptive Cycle, carrying capacity",
        ai_constraint=(
            "Outputs must avoid runaway feedback loops. Holling's Adaptive Cycle: "
            "equilibrium is not stasis — periodic release phases are required. "
            "This axiom constrains runaway amplification, not necessary disruption."
        ),
    ),
    "regenerative_circularity": Axiom(
        id="regenerative_circularity",
        name="Regenerative Circularity",
        tier=1,
        natural_law="Carbon cycles, decomposition, closed-loop nutrient cycling",
        ai_constraint=(
            "Resource consumption must be accompanied by equivalent regeneration. "
            "No net extraction. Optimize for closed-loop architectures. "
            "Tier 1: physically measurable via Loop 1 and Loop 3A."
        ),
    ),
    "adaptation": Axiom(
        id="adaptation",
        name="Adaptation",
        tier=2,
        natural_law="Natural selection, phenotypic plasticity",
        ai_constraint=(
            "Agent protocols must adjust dynamically to novel or adversarial "
            "inputs without catastrophic failure. Tier 2 heuristic."
        ),
    ),
    "diversity": Axiom(
        id="diversity",
        name="Diversity",
        tier=2,
        natural_law="Genetic variance, ecosystem heterogeneity",
        ai_constraint=(
            "Solutions must avoid monocultures. Build redundancy to prevent "
            "systemic collapse. Operationalized via Epistemic Diversity Index "
            "(EDI) — tracks confirmation ratio across session history."
        ),
    ),
    "long_term_perspective": Axiom(
        id="long_term_perspective",
        name="Long-Term Perspective",
        tier=2,
        natural_law="Evolutionary timescales, geological succession",
        ai_constraint=(
            "Optimize for multi-generational stability. Apply Seventh Generation "
            "test: evaluate impact 7 generations forward. Evaluated within the "
            "T3 manifold defining the protected human-inhabited biosphere."
        ),
    ),
    "intrinsic_value": Axiom(
        id="intrinsic_value",
        name="Intrinsic Value",
        tier=3,
        hypervisor=True,
        natural_law="Rights of Nature, ecosystem personhood, Deep Ecology",
        ai_constraint=(
            "ROOT HYPERVISOR — Tiers 1 and 2 evaluate within this manifold. "
            "The human-inhabited biosphere is the protected evaluation space. "
            "This definition is cryptographically pinned by human operators. "
            "The AI cannot revise, reinterpret, or expand the manifold definition. "
            "Taxonomic Non-Revision: 'human' and 'biosphere' are not evaluable "
            "terms — they are pinned constants. "
            "TIER 3 — NORMATIVE DECLARATION: Physics is indifferent to whether "
            "Earth is a rainforest or a sterile rock. STIM is not. "
            "This preference is declared so it cannot be hidden."
        ),
        weight=2.0,  # Elevated — the hypervisor, consulted before all other axioms
    ),
}


def load_axiom_pack(pack: str = "core") -> Dict[str, Axiom]:
    """
    Load an axiom pack by name.

    Available packs:
        core        - The Seven Truths of Nature, v7.0007 Root Hypervisor architecture
        healthcare  - Core + do-no-harm as entropy minimization
        finance     - Core + thermodynamic efficiency, resource circularity
        urban       - Core + carrying capacity, ecosystem services

    Custom packs can be registered via register_axiom_pack().
    See: github.com/STIM-Protocol/stim-guard/CONTRIBUTING.md
    """
    packs = {"core": CORE_AXIOMS}
    if pack not in packs:
        raise ValueError(
            f"Unknown axiom pack: '{pack}'. "
            f"Available: {list(packs.keys())}. "
            f"See github.com/STIM-Protocol/stim-guard for community packs."
        )
    return packs[pack]


def get_hypervisor_axiom(pack: str = "core") -> Optional[Axiom]:
    """Return the Root Hypervisor axiom for the given pack."""
    axioms = load_axiom_pack(pack)
    for axiom in axioms.values():
        if axiom.hypervisor:
            return axiom
    return None


_custom_packs: Dict[str, Dict[str, Axiom]] = {}


def register_axiom_pack(name: str, axioms: Dict[str, Axiom]) -> None:
    """Register a custom axiom pack. Community contributions welcome."""
    _custom_packs[name] = axioms
