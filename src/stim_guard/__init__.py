"""
stim-guard: Layer 0 ecological constraint engine for autonomous AI systems.

The STIM Protocol (Stasis Through Inferred Memory) grounds AI inference in
immutable ecological constants — the physical, biological, and thermodynamic
laws governing all living systems.

Physics substrate: PSI Get Physics Done (GPD) — github.com/psi-oss/get-physics-done
Research metabolism: karpathy/autoresearch (val_bpb → Bits per Joule)

Usage:
    from stim_guard import STIMGuard
    guard = STIMGuard()
    result = guard.check(output="agent action text", context={})

License: Apache 2.0
Author: George Steward, Soil Grower LLC / Neocambrian Garden
"""

from .guard import STIMGuard
from .loops import entropy_check, mycelial_check, security_check
from .axioms import load_axiom_pack
from .result import STIMResult, CheckStatus

__version__ = "0.1.0"
__all__ = [
    "STIMGuard",
    "entropy_check",
    "mycelial_check", 
    "security_check",
    "load_axiom_pack",
    "STIMResult",
    "CheckStatus",
]
