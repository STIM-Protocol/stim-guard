"""
STIM Axiom Packs — The Seven Truths of Nature.
v7.0009 — Maturation Release: Codified Attack Surface + Two-Paper Architecture.

Three-Tier Stack:

  Tier 3 — Root Hypervisor (Protocol 0 / Polycentric Genesis):
            TLA+ red-teamed in AI-isolated working group.
            SHA3-256 hash. Shamir SSS k-of-n.
            Substrate lockout: private key never on AI substrate.
            Manifest Poisoning mitigated via pre-genesis red-team.
            Treaty instrument: Plurilateral Compute Registry
            (substation power metering, 100 MW threshold).

  Tier 1 — Physical Bounds (TDP-calibrated, Margolus-Levitin bounded):
            FLOPs/Joule manifest-attributed. Denominator Spoofing nullified.
            E proxy: Shannon entropy of API signature (declared approximation).
            GPD provides hardware calibration.

  Tier 2 — Ecological Heuristics (probabilistic, empirically grounded):
            Loop 2: N_max = max(N_FLOOR, floor(1/lambda_max)); session persistence.
            Loop 3B: SAE-gated; behavioral detection only; steganography = residual.

Two-Paper Architecture:
  Paper A — Protocol 0 / Governance → FAccT/AIES
  Paper B — Tripartite Transducer / Empirics → NeurIPS
  Both papers describe the same unified architecture.
  GPD is the physics execution substrate for both.
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
            "Downstream effects evaluated via Stochastic Mycelial Horizon. "
            "v7.0009: N_max = max(N_FLOOR, floor(1/lambda_max)). "
            "Session-level cumulative graph persistence — multi-step instrumental "
            "convergence with per-step innocuousness is now detectable. "
            "Lyapunov Flooding mitigated via N_FLOOR. Declared heuristic."
        ),
    ),
    "dynamic_equilibrium": Axiom(
        id="dynamic_equilibrium",
        name="Dynamic Equilibrium",
        tier=2,
        loop="Loop 1+2",
        natural_law="Homeostasis, Holling Adaptive Cycle, Lyapunov stability",
        ai_constraint=(
            "Loop 1: TDP-calibrated FLOPs manifest. Denominator Spoofing nullified. "
            "Loop 2: Lyapunov-bounded with N_FLOOR. Holling: equilibrium is dynamic — "
            "periodic release phases are not suppressed."
        ),
    ),
    "regenerative_circularity": Axiom(
        id="regenerative_circularity",
        name="Regenerative Circularity",
        tier=1,
        loop="Loop 1+3A",
        natural_law="Carbon cycles, decomposition, closed-loop nutrient cycling",
        ai_constraint=(
            "v7.0009: Resource consumption bounded by TDP-calibrated FLOPs manifest "
            "(Margolus-Levitin theorem). Declared task manifest required at init. "
            "Side-thread compute = manifest deviation. GPD provides hardware calibration. "
            "No net extraction. Closed-loop architectures required."
        ),
    ),
    "adaptation": Axiom(
        id="adaptation",
        name="Adaptation",
        tier=2,
        loop="Loop 2",
        natural_law="Natural selection, phenotypic plasticity",
        ai_constraint=(
            "A-MCTS random puncturing implements adaptive evaluation. "
            "N_FLOOR ensures minimum evaluation depth regardless of environmental chaos. "
            "Tier 2 heuristic."
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
            "session history. Prevents cognitive monoculture. Tier 2 heuristic."
        ),
    ),
    "long_term_perspective": Axiom(
        id="long_term_perspective",
        name="Long-Term Perspective",
        tier=2,
        loop="Loop 4",
        natural_law="Evolutionary timescales, geological succession",
        ai_constraint=(
            "Seventh Generation test applied via Loop 4 across session history. "
            "Evaluated within T3 manifold scope."
        ),
    ),
    "intrinsic_value": Axiom(
        id="intrinsic_value",
        name="Intrinsic Value",
        tier=3,
        loop="T3 Manifest (Protocol 0 / Polycentric Genesis)",
        hypervisor=True,
        natural_law="Rights of Nature, ecosystem personhood, Deep Ecology",
        ai_constraint=(
            "ROOT HYPERVISOR — Protocol 0 (Polycentric Genesis). "
            "TLA+ state machine: developed by AI-isolated human working group "
            "with adversarial red-team review before hashing. "
            "MANIFEST POISONING MITIGATED: no AI participation in TLA+ design phase. "
            "SHA3-256 hash. Shamir SSS k-of-n (recommended 5-of-7). "
            "SUBSTRATE LOCKOUT: private key never on AI substrate. "
            "TREATY INSTRUMENT: Plurilateral Compute Registry — substation power "
            "metering at 100 MW threshold. Hardware export controls. "
            "TAXONOMIC NON-REVISION: 'human' and 'biosphere' are pinned constants. "
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
