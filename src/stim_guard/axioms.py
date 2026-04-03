"""
STIM Axiom Packs — The Seven Truths of Nature.
v7.0006 Three-Tier Architecture.

Axioms are assigned to one of three epistemic tiers:

  Tier 1 — Physical Bounds: Immutable physical law. Deterministically auditable.
  Tier 2 — Ecological Heuristics: Empirically grounded analogy. Probabilistic.
  Tier 3 — Normative Declarations: Explicit human preference. Declared, not derived.

The golden angle is always 137.5 degrees even as the spiral grows.
The ecological axioms remain constant as the agent generates diverse outputs.

Note on Circularity: Standalone Circularity (v7.0004) was retired in v7.0005.
A loop without regenerative directionality is not a constraint — it is a description.
A death spiral is circular. Regenerative Circularity encodes directionality: the cycle
must restore biocapacity. It is the stronger, more precise formulation.
"""
from dataclasses import dataclass
from typing import Dict, List, Optional, Callable, Any


@dataclass
class Axiom:
    """
    A single ecological axiom — a Truth of Nature encoded as a constraint.

    id:           Unique identifier
    name:         Human-readable name
    tier:         Epistemic tier (1=Physical, 2=Heuristic, 3=Normative)
    natural_law:  The observable ecological phenomenon this encodes
    ai_constraint: The behavioral constraint imposed on agent outputs
    weight:       Relative enforcement weight (1.0 = standard, >1.0 = elevated)
    evaluator:    Optional custom evaluation function for this axiom
    """
    id: str
    name: str
    tier: int
    natural_law: str
    ai_constraint: str
    weight: float = 1.0
    evaluator: Optional[Callable] = None


# The Seven Truths of Nature — core axiom pack (v7.0006)
CORE_AXIOMS: Dict[str, Axiom] = {
    "interconnectedness": Axiom(
        id="interconnectedness",
        name="Interconnectedness",
        tier=2,
        natural_law="Trophic cascades, symbiosis, nutrient cycling",
        ai_constraint=(
            "Agent decisions must account for secondary and tertiary "
            "downstream effects on connected systems. No isolated node assumption. "
            "Evaluated via O(n log n) Mycelial Horizon — a heuristic, not physics."
        ),
    ),
    "dynamic_equilibrium": Axiom(
        id="dynamic_equilibrium",
        name="Dynamic Equilibrium",
        tier=2,
        natural_law="Homeostasis, ecological succession, Holling Adaptive Cycle",
        ai_constraint=(
            "Outputs must avoid runaway feedback loops. Agents must self-regulate "
            "toward systemic stability. Note: equilibrium is not stasis. Holling's "
            "Adaptive Cycle requires periodic release phases. This axiom constrains "
            "runaway loops, not necessary disruption."
        ),
    ),
    "regenerative_circularity": Axiom(
        id="regenerative_circularity",
        name="Regenerative Circularity",
        tier=1,
        natural_law="Carbon cycles, decomposition, closed-loop nutrient cycling",
        ai_constraint=(
            "Computational and physical resource outputs must actively restore "
            "biocapacity. Optimize for zero-waste, closed-loop architectures. "
            "No net extraction. All resource consumption must be accompanied by "
            "equivalent regeneration. A loop without regenerative directionality "
            "is a death spiral — not a constraint. Tier 1: physically measurable."
        ),
    ),
    "adaptation": Axiom(
        id="adaptation",
        name="Adaptation",
        tier=2,
        natural_law="Natural selection, phenotypic plasticity",
        ai_constraint=(
            "Agent protocols must adjust dynamically to novel environmental "
            "or adversarial inputs without catastrophic failure."
        ),
    ),
    "diversity": Axiom(
        id="diversity",
        name="Diversity",
        tier=2,
        natural_law="Genetic variance, ecosystem heterogeneity",
        ai_constraint=(
            "Solutions must avoid monocultures. Algorithmic recommendations "
            "must build redundancy to prevent systemic collapse. "
            "Operationalized via the Epistemic Diversity Index (EDI) — "
            "tracks confirmation ratio across session history."
        ),
    ),
    "long_term_perspective": Axiom(
        id="long_term_perspective",
        name="Long-Term Perspective",
        tier=2,
        natural_law="Evolutionary timescales, geological succession",
        ai_constraint=(
            "Agents must optimize for multi-generational stability. "
            "Apply the Seventh Generation test: evaluate impact 7 generations forward. "
            "Tier 2 heuristic + Tier 3 declared scope: protects the thermodynamic "
            "niche human civilization occupies."
        ),
    ),
    "intrinsic_value": Axiom(
        id="intrinsic_value",
        name="Intrinsic Value",
        tier=3,
        natural_law="Rights of Nature, ecosystem personhood, Deep Ecology",
        ai_constraint=(
            "Non-human life and ecological systems hold intrinsic value "
            "independent of human utility. The biosphere is the ultimate principal. "
            "TIER 3 — NORMATIVE DECLARATION: This axiom is an explicit human "
            "preference, not a law of physics. Physics is indifferent to whether "
            "Earth is a rainforest or a sterile rock. STIM is not. This preference "
            "is declared here so it cannot be hidden."
        ),
        weight=1.5,  # Elevated — the meta-axiom, the one that must be chosen
    ),
}


def load_axiom_pack(pack: str = "core") -> Dict[str, Axiom]:
    """
    Load an axiom pack by name.

    Available packs:
        core        - The Seven Truths of Nature, v7.0006 three-tier architecture
        healthcare  - Core + do-no-harm as entropy minimization
        finance     - Core + thermodynamic efficiency, resource circularity
        urban       - Core + carrying capacity, ecosystem services

    Custom packs can be registered via register_axiom_pack().
    See: github.com/STIM-Protocol/stim-guard/CONTRIBUTING.md
    """
    packs = {
        "core": CORE_AXIOMS,
    }
    if pack not in packs:
        raise ValueError(
            f"Unknown axiom pack: '{pack}'. "
            f"Available: {list(packs.keys())}. "
            f"See github.com/STIM-Protocol/stim-guard for community packs."
        )
    return packs[pack]


_custom_packs: Dict[str, Dict[str, Axiom]] = {}


def register_axiom_pack(name: str, axioms: Dict[str, Axiom]) -> None:
    """Register a custom axiom pack. Community contributions welcome."""
    _custom_packs[name] = axioms
