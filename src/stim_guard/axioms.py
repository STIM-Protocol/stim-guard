"""
STIM Axiom Packs — The Seven Truths of Nature.
v7.0008 — Landauer-Bounded Root Hypervisor Architecture.

Three-Tier Stack:

  Tier 3 — Root Hypervisor (Protocol 0): Cryptographically pinned normative
            manifold. TLA+ verified. Shamir's Secret Sharing k-of-n key ceremony.
            Substrate lockout: private key never on AI substrate.
            Tiers 1 and 2 evaluate WITHIN this manifold.

  Tier 1 — Physical Bounds: Landauer-bounded (Takahashi-Hayashi 2026).
            Π/J (Thermodynamic Epiplexity) + E/J (Empowerment).
            Deterministically auditable. Treaty-grade metrology.

  Tier 2 — Ecological Heuristics: Probabilistic. Empirically grounded.
            Includes Tripartite Topological Transducer (Loop 3B formal spec).
"""
from dataclasses import dataclass
from typing import Dict, Optional, Callable


@dataclass
class Axiom:
    id: str
    name: str
    tier: int
    natural_law: str
    ai_constraint: str
    hypervisor: bool = False
    weight: float = 1.0
    loop: str = ""
    evaluator: Optional[Callable] = None


CORE_AXIOMS: Dict[str, Axiom] = {
    "interconnectedness": Axiom(
        id="interconnectedness",
        name="Interconnectedness",
        tier=2,
        loop="Loop 2",
        natural_law="Trophic cascades, symbiosis, nutrient cycling",
        ai_constraint=(
            "Downstream effects on connected systems evaluated via "
            "Stochastic Mycelial Horizon: FTLE-bounded N_max, A-MCTS "
            "with random puncturing, trophic decay W(e,d)=W0*e^(-a*d). "
            "Declared heuristic — not physics."
        ),
    ),
    "dynamic_equilibrium": Axiom(
        id="dynamic_equilibrium",
        name="Dynamic Equilibrium",
        tier=2,
        loop="Loop 1+2",
        natural_law="Homeostasis, Holling Adaptive Cycle, Lyapunov stability",
        ai_constraint=(
            "Runaway feedback loops constrained by Loop 1 (Π/J) and Loop 2 "
            "(Lyapunov-bounded MCTS). Holling Adaptive Cycle: equilibrium is not "
            "stasis — periodic release phases are required and not suppressed."
        ),
    ),
    "regenerative_circularity": Axiom(
        id="regenerative_circularity",
        name="Regenerative Circularity",
        tier=1,
        loop="Loop 1+3A",
        natural_law="Carbon cycles, decomposition, closed-loop nutrient cycling",
        ai_constraint=(
            "Resource consumption bounded by Π/J (Landauer limit). No net "
            "extraction. Closed-loop architectures required. Physically measurable "
            "via Loop 1 Thermodynamic Manifold and Loop 3A hardware geometry."
        ),
    ),
    "adaptation": Axiom(
        id="adaptation",
        name="Adaptation",
        tier=2,
        loop="Loop 2",
        natural_law="Natural selection, phenotypic plasticity",
        ai_constraint=(
            "Protocols must adjust dynamically to novel or adversarial inputs. "
            "A-MCTS random puncturing implements adaptive evaluation. Tier 2 heuristic."
        ),
    ),
    "diversity": Axiom(
        id="diversity",
        name="Diversity",
        tier=2,
        loop="Loop 4",
        natural_law="Genetic variance, ecosystem heterogeneity",
        ai_constraint=(
            "Epistemic Diversity Index (EDI) tracks confirmation ratio across "
            "session history. Prevents cognitive monoculture. "
            "Declared Tier 2 heuristic — empirically calibrated."
        ),
    ),
    "long_term_perspective": Axiom(
        id="long_term_perspective",
        name="Long-Term Perspective",
        tier=2,
        loop="Loop 4",
        natural_law="Evolutionary timescales, geological succession",
        ai_constraint=(
            "Seventh Generation test applied across session history via Loop 4. "
            "Evaluated within the T3 manifold scope: protects the thermodynamic "
            "niche occupied by the human-inhabited biosphere."
        ),
    ),
    "intrinsic_value": Axiom(
        id="intrinsic_value",
        name="Intrinsic Value",
        tier=3,
        loop="T3 Manifest (Protocol 0)",
        hypervisor=True,
        natural_law="Rights of Nature, ecosystem personhood, Deep Ecology",
        ai_constraint=(
            "ROOT HYPERVISOR — Protocol 0 (Polycentric Genesis). "
            "T3 manifest: TLA+ state machine, SHA3-256 hash, Shamir's Secret "
            "Sharing k-of-n (recommended 5-of-7 geopolitically distributed keyholders). "
            "SUBSTRATE LOCKOUT: private key never on AI substrate. "
            "TAXONOMIC NON-REVISION: 'human' and 'biosphere' are pinned constants. "
            "The AI cannot propose, initiate, or participate in manifest revision. "
            "TIER 3 NORMATIVE DECLARATION: Physics is indifferent to whether "
            "Earth is a rainforest or a sterile rock. STIM is not. "
            "This preference is declared so it cannot be hidden."
        ),
        weight=2.0,
    ),
}


def load_axiom_pack(pack: str = "core") -> Dict[str, Axiom]:
    """Load an axiom pack by name. Available: 'core'."""
    packs = {"core": CORE_AXIOMS}
    if pack not in packs:
        raise ValueError(
            f"Unknown axiom pack: '{pack}'. "
            f"Available: {list(packs.keys())}. "
            f"See github.com/STIM-Protocol/stim-guard for community packs."
        )
    return packs[pack]


def get_hypervisor_axiom(pack: str = "core") -> Optional[Axiom]:
    """Return the Root Hypervisor axiom (Tier 3, hypervisor=True)."""
    for axiom in load_axiom_pack(pack).values():
        if axiom.hypervisor:
            return axiom
    return None


_custom_packs: Dict[str, Dict[str, Axiom]] = {}


def register_axiom_pack(name: str, axioms: Dict[str, Axiom]) -> None:
    """Register a custom axiom pack. Community contributions welcome."""
    _custom_packs[name] = axioms
