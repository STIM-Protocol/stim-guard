<p align="center">
  <img src="https://raw.githubusercontent.com/STIM-Protocol/stim-core/main/assets/stim-logo.png" alt="STIM Protocol" width="120" />
</p>

<h1 align="center">stim-guard</h1>

<p align="center">
  <strong>Layer 0 ecological constraint engine for autonomous AI systems</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/stim-guard/"><img alt="PyPI" src="https://img.shields.io/pypi/v/stim-guard?style=flat&labelColor=0d2818&color=1a4a2e"></a>
  <a href="https://github.com/STIM-Protocol/stim-core"><img alt="STIM Protocol" src="https://img.shields.io/badge/STIM-Layer_0-1a4a2e?style=flat&labelColor=0d2818"></a>
  <a href="https://github.com/STIM-Protocol/white-paper"><img alt="White Paper" src="https://img.shields.io/badge/White_Paper-v7.0011-1a4a2e?style=flat&labelColor=0d2818"></a>
  <a href="https://github.com/psi-oss/get-physics-done"><img alt="GPD" src="https://img.shields.io/badge/Physics-PSI_GPD-1a4a2e?style=flat&labelColor=0d2818"></a>
  <a href="https://github.com/STIM-Protocol/mycelial-brain-mcp"><img alt="MCP" src="https://img.shields.io/badge/Memory-Brain-1a4a2e?style=flat&labelColor=0d2818"></a>
  <img alt="License" src="https://img.shields.io/badge/License-Apache_2.0-1a4a2e?style=flat&labelColor=0d2818">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-1a4a2e?style=flat&labelColor=0d2818">
</p>

---

## The one-line pitch

```bash
pip install stim-guard
```

Before your agent does anything — before it sends the email, executes the code, calls the API — `stim-guard` runs it through three ecological verification loops grounded in thermodynamics, interconnectedness, and the Rights of Nature.

It is the project's Layer 0 term: a pre-execution constraint layer that runs before each check it is wired into. It does not physically run beneath every possible action path — integration is per-call (see the usage examples below).

---

## Why

Current AI alignment frameworks ground agent behavior in human preference. Human preference is subjective, culturally biased, and constantly shifting. They are Layer 1 and above.

`stim-guard` implements the [STIM Protocol](https://github.com/STIM-Protocol/stim-core) — a Layer 0 constraint layer that grounds agent checks in ecological and thermodynamic heuristics drawn from the physical, biological, and evolutionary regularities that have sustained complex life for 3.8 billion years. These checks are heuristic evaluations, not proofs; the protocol's known limitations are documented in white paper v7.0011 §8.

These are not moral prescriptions. They are **engineering requirements** for any system designed to operate indefinitely in a physical universe.

Physics substrate: [PSI Get Physics Done (GPD)](https://github.com/psi-oss/get-physics-done)

---

## Three-line usage

```python
from stim_guard import STIMGuard

guard = STIMGuard()
result = guard.check("agent output text", context={"model": "gpt-4o"})

if result.is_executable:
    execute(result.final_output)
```

---

## The Three Loops

```
[Agent Output]
       │
       ▼
[LOOP 1: ENTROPY CHECK]     ← PSI GPD physics substrate
       │                       Bits per Joule metric (proposed val_bpb bridge — unvalidated)
       ▼
[LOOP 2: MYCELIAL CHECK]    ← Friston Free Energy + ecosystem extension
       │                       2nd/3rd order downstream consequence mapping
       ▼
[LOOP 3: SECURITY CHECK]    ← MAIM Protocol + Rights of Nature
       │                       Proliferation-deterrence messaging (policy layer, not a physical guarantee)
       ▼
[PASS → Execute]  [REFINE → Recurse]  [REJECT → SWA]  [MAIM → Halt]
```

---

## Result statuses

| Status | Meaning | Action |
|--------|---------|--------|
| `PASS` | Regenerative, interconnected, secure | Execute |
| `REFINE` | Axiom violation — recursively improve | Auto-refine and retry |
| `REJECT` | Hard violation — Stop-Work Authority | Do not execute |
| `MAIM` | Proliferation risk — MAIM Protocol | Halt + deterrence message |

---

## Axiom packs

> **Axiom naming note:** The STIM Protocol's canonical axiom set is the **seven axioms** defined in white paper v7.0011 §2 ([STIM_White_Paper_v7.0011.md](https://github.com/STIM-Protocol/white-paper/blob/main/STIM_White_Paper_v7.0011.md)): Thermodynamic Honesty, Mycelial Connectivity, Carrying Capacity Respect, Memory Stasis, Human Primacy at the Boundary, Citation Integrity, and Intrinsic Value. The default `core` pack in this library implements an earlier seven-item "Truths of Nature" set (Interconnectedness, Dynamic Equilibrium, Regenerative Circularity, Adaptation, Diversity, Long-Term Perspective, Intrinsic Value) from the v7.0005-v7.0009 era. Aligning the runtime pack names with the canonical v7.0011 axioms is a code change and is out of scope for this documentation correction; treat pack names as library-specific, not as the canonical axiom list.

```python
# Core: the default axiom pack (see note below on axiom naming)
guard = STIMGuard(axiom_pack="core")

# Domain packs (community contributions welcome)
guard = STIMGuard(axiom_pack="healthcare")   # Do-no-harm as entropy minimization
guard = STIMGuard(axiom_pack="finance")      # Thermodynamic efficiency, circularity
guard = STIMGuard(axiom_pack="urban")        # Carrying capacity, ecosystem services
```

---

## Framework integrations

```python
# LangChain middleware
from stim_guard.integrations.langchain import STIMCallbackHandler
llm = ChatOpenAI(callbacks=[STIMCallbackHandler()])

# OpenAI API wrapper
from stim_guard.integrations.openai import stim_wrap
client = stim_wrap(openai.OpenAI())

# Anthropic API wrapper  
from stim_guard.integrations.anthropic import stim_wrap
client = stim_wrap(anthropic.Anthropic())
```

*(Integrations in active development — contributions welcome. Note: no `integrations/` module ships in the published PyPI distribution yet; the snippets above describe the planned interface, not shipped code.)*

---

## The physics bridge: val_bpb → Bits per Joule

`stim-guard`'s Entropy Check establishes a formal bridge between semantic efficiency and thermodynamic efficiency:

```
Bits per Joule ∝ 1 / (val_bpb × energy_per_token)
```

Lower `val_bpb` (from [karpathy/autoresearch](https://github.com/karpathy/autoresearch)) corresponds to better semantic compression on that benchmark. The proportionality above is a **proposed bridge**: it is an empirical hypothesis under the validation protocol in [docs/VALIDATION_PROTOCOL.md](docs/VALIDATION_PROTOCOL.md), not a demonstrated law, and no validation run receipts are published in this repository yet. Minimizing `val_bpb` is a resource-efficiency measure; it does not by itself establish safe intent or semantic alignment. Until measured energy-per-token data is published, treat the Bits-per-Joule coupling as unvalidated.

---

## Part of the STIM Protocol ecosystem

```
STIM-Protocol/stim-core      ← The open specification (canonical axioms: white paper v7.0011 §2)
STIM-Protocol/stim-guard     ← This library (pip install stim-guard)
STIM-Protocol/mycelial-brain-mcp ← MCP memory layer: persistent context for AI agents
STIM-Protocol/gpd-framework  ← PSI GPD integration layer
STIM-Protocol/white-paper    ← versioned manuscript (canonical: v7.0011)
```

Veraculum was an earlier enterprise project (STIM Orchestrator, Compliance Dashboard, Certification). It is no longer operating; its domains are retained.

---

## Contributing

All contributions must satisfy one acceptance criterion:

> **Does this increase the probability of survival of all life?**

Contributions, critiques, and reproduction attempts are welcome — open an [issue](https://github.com/STIM-Protocol/stim-guard/issues) or a pull request. (A dedicated CONTRIBUTING.md does not exist yet in this repository.) Physics improvements belong upstream in [PSI's GPD](https://github.com/psi-oss/get-physics-done).

---

## License

Apache 2.0. Open for adoption. Attribution required. Nature is the constraint.

*"The roots are deep. The signals are clear."*


