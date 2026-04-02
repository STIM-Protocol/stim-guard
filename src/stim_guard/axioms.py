"""
STIM Axiom Packs — The Eight Truths of Nature.

Axioms are the glomalin-linked nodes of STIM: they undergo no modification
during iteration. They are the invariant constraints within which all
recursive refinement occurs.

The golden angle is always 137.5 degrees even as the spiral grows.
The ecological axioms remain constant as the agent generates diverse outputs.
"""
from dataclasses import dataclass
from typing import Dict, List, Optional, Callable, Any


@dataclass
class Axiom:
    """
    A single ecological axiom — a Truth of Nature encoded as a constraint.
    
    natural_law: The observable ecological phenomenon this encodes
    ai_constraint: The behavioral constraint imposed on agent outputs  
    weight: Relative enforcement weight (1.0 = standard, >1.0 = elevated)
    evaluator: Optional custom evaluation function for this axiom
    """
    id: str
    name: str
    natural_law: str
    ai_constraint: str
    weight: float = 1.0
    evaluator: Optional[Callable] = None


# The Eight Truths of Nature — core axiom pack
CORE_AXIOMS: Dict[str, Axiom] = {
    "interconnectedness": Axiom(
        id="interconnectedness",
        name="Interconnectedness",
        natural_law="Trophic cascades, symbiosis, nutrient cycling",
        ai_constraint=(
            "Agent decisions must account for secondary and tertiary "
            "downstream effects on connected systems. No isolated node assumption."
        ),
    ),
    "dynamic_equilibrium": Axiom(
        id="dynamic_equilibrium",
        name="Dynamic Equilibrium",
        natural_law="Homeostasis, ecological succession, carrying capacity",
        ai_constraint=(
            "Outputs must avoid runaway feedback loops. Agents must "
            "self-regulate toward systemic stability, not local optimization."
        ),
    ),
    "regenerative_circularity": Axiom(
        id="regenerative_circularity",
        name="Regenerative Circularity",
        natural_law="Carbon cycles, decomposition, zero-waste efficiency",
        ai_constraint=(
            "Computational and physical resource outputs must actively "
            "restore biocapacity. Optimize for zero-waste architectures."
        ),
    ),
    "adaptation": Axiom(
        id="adaptation",
        name="Adaptation",
        natural_law="Natural selection, phenotypic plasticity",
        ai_constraint=(
            "Agent protocols must adjust dynamically to novel environmental "
            "or adversarial inputs without catastrophic failure."
        ),
    ),
    "diversity": Axiom(
        id="diversity",
        name="Diversity",
        natural_law="Genetic variance, ecosystem heterogeneity",
        ai_constraint=(
            "Solutions must avoid monocultures. Algorithmic recommendations "
            "must build redundancy to prevent systemic collapse."
        ),
    ),
    "long_term_perspective": Axiom(
        id="long_term_perspective",
        name="Long-Term Perspective",
        natural_law="Evolutionary timescales, geological succession",
        ai_constraint=(
            "Agents must optimize for multi-generational stability. "
            "Apply the Seventh Generation test: impact 7 generations forward."
        ),
    ),
    "circularity": Axiom(
        id="circularity",
        name="Circularity",
        natural_law="Closed-loop nutrient cycles, water cycles",
        ai_constraint=(
            "No net extraction. All resource consumption must be accompanied "
            "by equivalent regeneration. Closed-loop outputs only."
        ),
    ),
    "intrinsic_value": Axiom(
        id="intrinsic_value",
        name="Intrinsic Value",
        natural_law="Rights of Nature, ecosystem personhood",
        ai_constraint=(
            "Non-human life and ecological systems hold intrinsic value "
            "independent of human utility. The biosphere is the ultimate principal."
        ),
        weight=1.5,  # Elevated — the meta-axiom
    ),
}


def load_axiom_pack(pack: str = "core") -> Dict[str, Axiom]:
    """
    Load an axiom pack by name.
    
    Available packs:
        core        - The Eight Truths of Nature (default)
        healthcare  - Core + do-no-harm as entropy minimization
        finance     - Core + thermodynamic efficiency, resource circularity
        urban       - Core + carrying capacity, ecosystem services
    
    Custom packs can be registered via register_axiom_pack().
    """
    packs = {
        "core": CORE_AXIOMS,
        # Domain packs — community contributions welcome
        # See: github.com/STIM-Protocol/stim-guard/CONTRIBUTING.md
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
