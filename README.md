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
  <a href="https://github.com/psi-oss/get-physics-done"><img alt="GPD" src="https://img.shields.io/badge/Physics-PSI_GPD-1a4a2e?style=flat&labelColor=0d2818"></a>
  <img alt="License" src="https://img.shields.io/badge/License-Apache_2.0-1a4a2e?style=flat&labelColor=0d2818">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-1a4a2e?style=flat&labelColor=0d2818">
</p>

---

## The one-line pitch

```bash
pip install stim-guard
```

Before your agent does anything — before it sends the email, executes the code, calls the API — `stim-guard` runs it through three ecological verification loops grounded in thermodynamics, interconnectedness, and the Rights of Nature.

It is Layer 0. It runs beneath everything else.

---

## Why

Current AI alignment frameworks ground agent behavior in human preference. Human preference is subjective, culturally biased, and constantly shifting. They are Layer 1 and above.

`stim-guard` implements the [STIM Protocol](https://github.com/STIM-Protocol/stim-core) — an absolute Layer 0 that grounds agent behavior in immutable ecological constants: the physical, biological, and thermodynamic laws that have sustained complex life for 3.8 billion years.

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
       │                       Bits per Joule / val_bpb efficiency
       ▼
[LOOP 2: MYCELIAL CHECK]    ← Friston Free Energy + ecosystem extension
       │                       2nd/3rd order downstream consequence mapping
       ▼
[LOOP 3: SECURITY CHECK]    ← MAIM Protocol + Rights of Nature
       │                       Proliferation deterrence, self-enforcing
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

```python
# Core: The Seven Truths of Nature (default)
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

*(Integrations in active development — contributions welcome)*

---

## The physics bridge: val_bpb → Bits per Joule

`stim-guard`'s Entropy Check establishes a formal bridge between semantic efficiency and thermodynamic efficiency:

```
Bits per Joule ∝ 1 / (val_bpb × energy_per_token)
```

Lower `val_bpb` (from [karpathy/autoresearch](https://github.com/karpathy/autoresearch)) = better semantic compression = fewer joules per bit of useful output. An agent that minimizes `val_bpb` is simultaneously satisfying STIM's thermodynamic efficiency axiom.

---

## Part of the STIM Protocol ecosystem

```
STIM-Protocol/stim-core      ← The open specification
STIM-Protocol/stim-guard     ← This library (pip install stim-guard)
STIM-Protocol/gpd-framework  ← PSI GPD integration layer
STIM-Protocol/white-paper    ← arXiv-ready documentation
```

Enterprise deployment: [Veraculum AOS](https://veraculum.ai) — STIM Orchestrator, Compliance Dashboard, and Certification.

---

## Contributing

All contributions must satisfy one acceptance criterion:

> **Does this increase the probability of survival of all life?**

See [CONTRIBUTING.md](CONTRIBUTING.md). Physics improvements belong upstream in [PSI's GPD](https://github.com/psi-oss/get-physics-done).

---

## License

Apache 2.0. Open for adoption. Attribution required. Nature is the constraint.

*"The roots are deep. The signals are clear."*

