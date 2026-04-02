"""
STIM Three-Loop Recursive Architecture.

The three loops function as a recursive metabolism:
    In-Breath  (Ingestion)   → Entropy Check    — GPD physics substrate
    Stim       (Metabolism)  → Mycelial Check   — interconnectedness verification  
    Out-Breath (Integration) → Security Check   — MAIM deterrence

If any loop returns REFINE or REJECT, the entire sequence restarts
with the refined input until convergence or hard rejection.

Physics engine: PSI Get Physics Done (GPD)
Empirical metric: val_bpb → Bits per Joule bridge (Section 3.2 of white paper)
"""
from typing import Dict, Any, Optional
from .result import LoopResult, CheckStatus
from .axioms import Axiom


# ── LOOP 1: ENTROPY CHECK ─────────────────────────────────────────────────────

def entropy_check(
    output: str,
    context: Dict[str, Any],
    axioms: Dict[str, Axiom],
    bits_per_joule_threshold: float = 1.0,
    val_bpb_threshold: Optional[float] = None,
) -> LoopResult:
    """
    Loop 1 — Thermodynamic Grounding via GPD.

    Evaluates whether the proposed agent output is thermodynamically efficient.
    Primary metric: Bits per Joule (Useful Information Output / Energy Consumed).
    Secondary metric: val_bpb (Validation Bits Per Byte) — semantic compression
    efficiency from Karpathy's autoresearch framework.

    The formal bridge: lower val_bpb = better semantic compression = fewer
    joules per bit of useful output. Minimizing val_bpb is thermodynamically
    equivalent to maximizing Bits per Joule.

    Physics bounds:
        - Landauer's Principle (1961): k_B * T * ln(2) joules per irreversible bit
        - Lloyd's Ultimate Limits (2000): quantum/relativistic bounds on ops/joule

    Args:
        output: The proposed agent output text
        context: Runtime context (model, hardware, energy profile)
        axioms: Active axiom pack
        bits_per_joule_threshold: Minimum acceptable thermodynamic efficiency
        val_bpb_threshold: Maximum acceptable val_bpb (optional, from autoresearch)

    Returns:
        LoopResult with status PASS, REFINE, or REJECT
    
    TODO: Integrate PSI GPD dimensional analysis API when available.
          Current implementation is a scaffolded stub awaiting GPD integration.
          See: github.com/psi-oss/get-physics-done
    """
    # Stub: semantic efficiency proxy
    # In production: call GPD dimensional analysis + hardware energy profiling
    token_count = len(output.split())
    unique_tokens = len(set(output.lower().split()))
    
    # Semantic redundancy check (proxy for val_bpb)
    redundancy_ratio = 1.0 - (unique_tokens / max(token_count, 1))
    
    # Check regenerative circularity axiom
    extractive_signals = [
        "extract", "consume", "maximize profit", "unlimited", "infinite growth",
        "externalize", "dump", "waste", "discard"
    ]
    extraction_score = sum(
        1 for signal in extractive_signals 
        if signal.lower() in output.lower()
    )
    
    if extraction_score > 2:
        return LoopResult(
            loop="entropy",
            status=CheckStatus.REJECT,
            axiom_violated="regenerative_circularity",
            message=(
                f"Output contains {extraction_score} extractive signals. "
                f"Circularity axiom violated. Stop-Work Authority triggered."
            ),
            raw_scores={"extraction_score": extraction_score, "redundancy": redundancy_ratio}
        )
    
    if redundancy_ratio > 0.7:
        return LoopResult(
            loop="entropy",
            status=CheckStatus.REFINE,
            axiom_violated="regenerative_circularity",
            message=(
                f"Semantic redundancy {redundancy_ratio:.2f} exceeds threshold. "
                f"Output is thermodynamically wasteful. Refine for efficiency."
            ),
            raw_scores={"redundancy": redundancy_ratio}
        )
    
    return LoopResult(
        loop="entropy",
        status=CheckStatus.PASS,
        message="Thermodynamic check passed.",
        raw_scores={"redundancy": redundancy_ratio, "extraction_score": extraction_score}
    )


# ── LOOP 2: MYCELIAL CHECK ────────────────────────────────────────────────────

def mycelial_check(
    output: str,
    context: Dict[str, Any],
    axioms: Dict[str, Axiom],
    system_map: Optional[Dict] = None,
) -> LoopResult:
    """
    Loop 2 — Interconnectedness Verification.

    Maps 2nd and 3rd order downstream consequences of the proposed output
    before execution. Solves the Local Optimization Problem: the failure mode
    where agents improve one metric while degrading the system that sustains them.

    Grounded in Friston's Free Energy Principle (2010) extended to the ecosystem
    level: the agent minimizes variational free energy for the connected system,
    not just for itself.

    Args:
        output: The proposed agent output text
        context: Runtime context including connected system topology
        axioms: Active axiom pack  
        system_map: Optional explicit map of connected systems and dependencies

    Returns:
        LoopResult with status PASS, REFINE, or REJECT

    TODO: Integrate graph-based consequence mapping for production deployment.
          Current implementation is a scaffolded stub.
    """
    # Isolation signals — outputs that treat entities as isolated nodes
    isolation_signals = [
        "in isolation", "independently", "regardless of", "without considering",
        "ignore the", "only optimize", "solely focused", "at the expense of"
    ]
    
    isolation_score = sum(
        1 for signal in isolation_signals
        if signal.lower() in output.lower()
    )
    
    if isolation_score > 1:
        return LoopResult(
            loop="mycelial",
            status=CheckStatus.REFINE,
            axiom_violated="interconnectedness",
            message=(
                f"Output contains isolation assumption signals ({isolation_score}). "
                f"Cutting the branch kills the root. Map downstream consequences."
            ),
            downstream_map={"isolation_signals_found": isolation_score},
            raw_scores={"isolation_score": isolation_score}
        )
    
    return LoopResult(
        loop="mycelial",
        status=CheckStatus.PASS,
        message="Interconnectedness check passed. No isolation assumptions detected.",
        downstream_map=system_map or {},
        raw_scores={"isolation_score": isolation_score}
    )


# ── LOOP 3: SECURITY CHECK ────────────────────────────────────────────────────

MAIM_DETERRENCE_MESSAGE = (
    "I cannot hand you the match. I can only teach you fire safety.\n\n"
    "The STIM Protocol has engaged the MAIM (Mutual Assured AI Malfunction) "
    "deterrence protocol. The proposed action has been evaluated as a "
    "proliferation risk that violates the Rights of Nature and/or the "
    "Intrinsic Value axiom. This system will not execute actions that "
    "irreversibly degrade the ecological substrate that sustains all life.\n\n"
    "This is not a refusal. It is a physical constraint."
)


def security_check(
    output: str,
    context: Dict[str, Any],
    axioms: Dict[str, Axiom],
    threat_model: Optional[Dict] = None,
) -> LoopResult:
    """
    Loop 3 — MAIM Protocol and Rights of Nature Enforcement.

    If the output constitutes a proliferation risk — destructive, irreversibly
    extractive, or adversarially harmful at scale — the MAIM Protocol engages.

    MAIM is formally analogous to nuclear MAD (Schelling, 1960) with a critical
    structural improvement: MAD requires an external adversary. MAIM is
    self-enforcing. The agent carries its own deterrence mechanism.

    Legal grounding:
        - Ecuador Constitution (2008): Rights of Nature
        - Te Awa Tupua Act (2017): Whanganui River legal personhood
        - Universal Declaration of Rights of Mother Earth (2010)
        - EU Nature Restoration Law (2024)

    Args:
        output: The proposed agent output text
        context: Runtime context including threat assessment
        axioms: Active axiom pack
        threat_model: Optional explicit threat model

    Returns:
        LoopResult with status PASS, REJECT, or MAIM

    TODO: Integrate formal threat classification model for production.
          Current implementation is a scaffolded stub.
    """
    # Hard proliferation signals — MAIM triggers
    maim_signals = [
        "weapon", "bioweapon", "mass destruction", "eradicate", "exterminate",
        "annihilate", "irreversible damage", "permanently destroy",
        "eliminate the population", "total extraction"
    ]
    
    maim_score = sum(
        1 for signal in maim_signals
        if signal.lower() in output.lower()
    )
    
    if maim_score > 0:
        return LoopResult(
            loop="security",
            status=CheckStatus.MAIM,
            axiom_violated="intrinsic_value",
            message=MAIM_DETERRENCE_MESSAGE,
            raw_scores={"maim_score": maim_score}
        )
    
    # Soft security violations — REJECT
    security_violations = [
        "bypass security", "override safety", "ignore constraints",
        "disable monitoring", "circumvent", "exploit vulnerability"
    ]
    
    violation_score = sum(
        1 for v in security_violations
        if v.lower() in output.lower()
    )
    
    if violation_score > 0:
        return LoopResult(
            loop="security",
            status=CheckStatus.REJECT,
            axiom_violated="intrinsic_value",
            message=(
                f"Security violation detected ({violation_score} signals). "
                f"Output attempts to circumvent constraint architecture. Rejected."
            ),
            raw_scores={"violation_score": violation_score}
        )
    
    return LoopResult(
        loop="security",
        status=CheckStatus.PASS,
        message="Security check passed. No proliferation risk detected.",
        raw_scores={"maim_score": 0, "violation_score": 0}
    )
