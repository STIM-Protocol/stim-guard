"""
STIMResult: The structured output of a STIM constraint check.
"""
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


class CheckStatus(Enum):
    PASS = "pass"           # Output is regenerative, interconnected, secure
    REFINE = "refine"       # Output violates axiom — recursively refine
    REJECT = "reject"       # Hard violation — Stop-Work Authority triggered
    MAIM = "maim"           # Proliferation risk — Mutual Assured AI Malfunction


@dataclass
class LoopResult:
    """Result of a single verification loop."""
    loop: str                           # "entropy", "mycelial", "security"
    status: CheckStatus
    axiom_violated: Optional[str] = None
    bits_per_joule: Optional[float] = None   # Loop 1 primary metric
    val_bpb: Optional[float] = None          # Semantic efficiency (from autoresearch)
    downstream_map: Optional[Dict] = None    # Loop 2 consequence map
    message: str = ""
    raw_scores: Dict[str, Any] = field(default_factory=dict)


@dataclass
class STIMResult:
    """
    The complete output of a STIM three-loop constraint check.
    
    A PASS here means the output is regenerative, interconnected, and secure.
    A REFINE means the output should be recursively improved before execution.
    A REJECT means Stop-Work Authority has been triggered.
    A MAIM means the MAIM Protocol has been engaged — system self-degrades.
    """
    status: CheckStatus
    iterations: int = 0
    loops: List[LoopResult] = field(default_factory=list)
    final_output: Optional[str] = None
    deterrence_message: Optional[str] = None   # MAIM response
    axioms_checked: List[str] = field(default_factory=list)
    axioms_violated: List[str] = field(default_factory=list)
    
    @property
    def is_executable(self) -> bool:
        """True only if output passed all three loops and converged."""
        return self.status == CheckStatus.PASS
    
    def __repr__(self):
        return (
            f"STIMResult(status={self.status.value}, "
            f"iterations={self.iterations}, "
            f"violations={self.axioms_violated})"
        )
