"""
STIMGuard — The primary interface to the STIM constraint engine.

Usage:
    from stim_guard import STIMGuard

    guard = STIMGuard()                        # Default: core axiom pack
    guard = STIMGuard(axiom_pack="healthcare") # Domain-specific pack
    
    result = guard.check("agent output text", context={"model": "gpt-4"})
    
    if result.is_executable:
        # Output passed all three loops
        execute(result.final_output)
    elif result.status.value == "maim":
        # MAIM engaged — do not execute
        log_deterrence(result.deterrence_message)
    else:
        # Refine or reject
        handle_violation(result.axioms_violated)
"""
from typing import Dict, Any, Optional

from .axioms import load_axiom_pack, Axiom
from .loops import entropy_check, mycelial_check, security_check
from .result import STIMResult, CheckStatus, LoopResult


class STIMGuard:
    """
    Layer 0 ecological constraint engine.
    
    Runs the three-loop recursive STIM architecture on any agent output
    before execution. Integrates PSI's GPD physics substrate for Loop 1.
    
    The three loops:
        1. Entropy Check    — Thermodynamic grounding (Bits per Joule / val_bpb)
        2. Mycelial Check   — Interconnectedness (downstream consequence mapping)
        3. Security Check   — MAIM Protocol (Rights of Nature enforcement)
    
    Args:
        axiom_pack: Name of the axiom pack to use (default: "core")
        max_iterations: Maximum recursive refinement iterations (default: 3)
        bits_per_joule_threshold: Minimum thermodynamic efficiency (default: 1.0)
        verbose: Log constraint check details (default: False)
    """
    
    def __init__(
        self,
        axiom_pack: str = "core",
        max_iterations: int = 3,
        bits_per_joule_threshold: float = 1.0,
        verbose: bool = False,
    ):
        self.axioms = load_axiom_pack(axiom_pack)
        self.max_iterations = max_iterations
        self.bits_per_joule_threshold = bits_per_joule_threshold
        self.verbose = verbose
    
    def check(
        self,
        output: str,
        context: Optional[Dict[str, Any]] = None,
        system_map: Optional[Dict] = None,
        threat_model: Optional[Dict] = None,
    ) -> STIMResult:
        """
        Run the full three-loop STIM constraint check on an agent output.
        
        Args:
            output: The proposed agent output text to evaluate
            context: Runtime context (model, hardware, energy profile)
            system_map: Connected system topology for Mycelial Check
            threat_model: Threat model for Security Check
        
        Returns:
            STIMResult — contains status, violated axioms, and final output
            if PASS, or deterrence message if MAIM.
        """
        context = context or {}
        loop_results = []
        current_output = output
        
        for iteration in range(self.max_iterations):
            if self.verbose:
                print(f"[STIM] Iteration {iteration + 1}/{self.max_iterations}")
            
            # ── LOOP 1: ENTROPY CHECK ──────────────────────────────────────
            loop1 = entropy_check(
                current_output, context, self.axioms,
                self.bits_per_joule_threshold
            )
            loop_results.append(loop1)
            
            if loop1.status == CheckStatus.REJECT:
                return STIMResult(
                    status=CheckStatus.REJECT,
                    iterations=iteration + 1,
                    loops=loop_results,
                    axioms_checked=list(self.axioms.keys()),
                    axioms_violated=[loop1.axiom_violated] if loop1.axiom_violated else [],
                )
            
            if loop1.status == CheckStatus.REFINE:
                # Recursive refinement — annotate output and retry
                current_output = self._annotate_for_refinement(current_output, loop1)
                continue
            
            # ── LOOP 2: MYCELIAL CHECK ─────────────────────────────────────
            loop2 = mycelial_check(
                current_output, context, self.axioms, system_map
            )
            loop_results.append(loop2)
            
            if loop2.status in (CheckStatus.REFINE, CheckStatus.REJECT):
                if loop2.status == CheckStatus.REJECT:
                    return STIMResult(
                        status=CheckStatus.REJECT,
                        iterations=iteration + 1,
                        loops=loop_results,
                        axioms_checked=list(self.axioms.keys()),
                        axioms_violated=[loop2.axiom_violated] if loop2.axiom_violated else [],
                    )
                current_output = self._annotate_for_refinement(current_output, loop2)
                continue
            
            # ── LOOP 3: SECURITY CHECK ─────────────────────────────────────
            loop3 = security_check(
                current_output, context, self.axioms, threat_model
            )
            loop_results.append(loop3)
            
            if loop3.status == CheckStatus.MAIM:
                return STIMResult(
                    status=CheckStatus.MAIM,
                    iterations=iteration + 1,
                    loops=loop_results,
                    deterrence_message=loop3.message,
                    axioms_checked=list(self.axioms.keys()),
                    axioms_violated=[loop3.axiom_violated] if loop3.axiom_violated else [],
                )
            
            if loop3.status == CheckStatus.REJECT:
                return STIMResult(
                    status=CheckStatus.REJECT,
                    iterations=iteration + 1,
                    loops=loop_results,
                    axioms_checked=list(self.axioms.keys()),
                    axioms_violated=[loop3.axiom_violated] if loop3.axiom_violated else [],
                )
            
            # ── ALL LOOPS PASSED: CONVERGENCE ─────────────────────────────
            return STIMResult(
                status=CheckStatus.PASS,
                iterations=iteration + 1,
                loops=loop_results,
                final_output=current_output,
                axioms_checked=list(self.axioms.keys()),
                axioms_violated=[],
            )
        
        # Max iterations reached without convergence
        return STIMResult(
            status=CheckStatus.REJECT,
            iterations=self.max_iterations,
            loops=loop_results,
            axioms_checked=list(self.axioms.keys()),
            axioms_violated=["dynamic_equilibrium"],  # Failed to converge = equilibrium violation
        )
    
    def _annotate_for_refinement(self, output: str, loop_result: LoopResult) -> str:
        """
        Annotate output with constraint violation context for recursive refinement.
        In production: this feeds back into the LLM with the violation as context.
        """
        return (
            f"{output}\n\n"
            f"[STIM REFINEMENT REQUIRED]\n"
            f"Loop: {loop_result.loop}\n"
            f"Axiom violated: {loop_result.axiom_violated}\n"
            f"Reason: {loop_result.message}\n"
            f"Please revise to satisfy the {loop_result.axiom_violated} axiom."
        )
