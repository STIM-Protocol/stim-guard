# STIM Validation Protocol: val_bpb → Bits per Joule

**Purpose:** Empirical validation of the semantic-thermodynamic bridge (Section 3.2 of white paper)
**Framework:** Karpathy `autoresearch` + PSI Get Physics Done (GPD)
**Target:** RQ8 — Does minimizing `val_bpb` produce measurable reductions in joules per useful output bit?

---

## The Bridge (Formal Statement)

From the STIM white paper (v7.0004, Section 3.2):

```
Bits per Joule ∝ 1 / (val_bpb × energy_per_token)
```

Where:
- `val_bpb` (Validation Bits Per Byte) — semantic compression efficiency,
  measured by the `autoresearch` framework's fixed evaluation harness
- `energy_per_token` — joules consumed per token, measured via GPU power draw
- `Bits per Joule` — STIM's primary thermodynamic efficiency metric (Loop 1)

Lower `val_bpb` = better semantic compression = fewer FLOPs per meaningful bit
= fewer joules per useful output. This is the Entropy Check operating at the
semantic layer.

**GPD role:** The Get Physics Done framework provides dimensional analysis
verification that this relationship is physically consistent — that the units
resolve correctly and that the claimed thermodynamic interpretation is not a
metaphor but a formal equivalence.

---

## Experimental Procedure (autoresearch loop)

This protocol uses Karpathy's `autoresearch` autonomous research framework:
https://github.com/karpathy/autoresearch

### Prerequisites
- NVIDIA GPU with CUDA (RTX 5070 or equivalent recommended)
- `uv` package manager
- Data shards prepared: `uv run prepare.py`

### Setup
```bash
git checkout -b autoresearch/stim-val-<date>
uv run prepare.py   # prepare data shards + tokenizer
```

### The Loop
The autoresearch agent runs autonomously, modifying `train.py` to minimize
`val_bpb` within a fixed 5-minute training budget per experiment.

```bash
# Agent runs: uv run train.py > run.log 2>&1
# Agent reads: grep "^val_bpb:\|^peak_vram_mb:" run.log
```

Each experiment logs:
```
commit    val_bpb     memory_gb  status   description
a1b2c3d   0.997900    44.0       keep     baseline
b2c3d4e   0.993200    44.2       keep     [modification]
...
```

### GPD Validation Layer (STIM-specific addition)

After each `keep` experiment, run GPD dimensional analysis on the result:

```python
from gpd import verify_thermodynamic_equivalence

result = verify_thermodynamic_equivalence(
    val_bpb=0.993200,
    energy_per_token_joules=measured_gpu_draw,  # watts × seconds / tokens
    claimed_metric="bits_per_joule"
)
# GPD confirms: units resolve, thermodynamic interpretation is valid
```

This step is what connects the autoresearch empirical loop to STIM's
theoretical framework. Without GPD verification, `val_bpb` improvement
is just ML benchmarking. With GPD verification, it becomes a thermodynamic
efficiency claim grounded in physics.

---

## Measurement Protocol

To measure `energy_per_token` during training runs:

```bash
# GPU power draw during training (nvidia-smi)
nvidia-smi --query-gpu=power.draw --format=csv,noheader,nounits \
  --loop-ms=1000 > power_log.txt &
POWER_PID=$!
uv run train.py > run.log 2>&1
kill $POWER_PID

# Calculate: mean_watts × training_seconds / total_tokens_M × 1e6
```

The output adds two columns to `results.tsv`:
```
commit  val_bpb  memory_gb  status  energy_j_per_token  bits_per_joule  description
```

---

## Research Questions Addressed

| RQ | Question | Method |
|----|----------|--------|
| **RQ8** | Does minimizing `val_bpb` reduce joules per useful output bit? | autoresearch loop + power measurement + GPD verification |
| **RQ3** | What is the computational overhead of STIM pre-inference checking? | Measure latency delta with/without `stim-guard` middleware |
| **RQ7** | What are the thermodynamic bounds on the entropy check's cost? | GPD Landauer limit calculation vs. actual constraint check energy |

---

## Hardware Notes

**Current node:** `arboracle` (AMD Ryzen 7 7735U)
- Status: `autoresearch` installed, data preparable
- Blocker: No NVIDIA CUDA GPU — training experiments not meaningful at scale
- Use case: Setup verification, dry runs, code validation only

**Target node:** TUXEDO InfinityBook Max 16 (RTX 5070)
- Status: Planned
- Use case: Full overnight metabolism — ~100 experiments per 8-hour sleep cycle
- Expected baseline `val_bpb`: ~0.997 (per Karpathy's published results)

**AMD alternative:** Strix Halo build (ROCm)
- Requires `train.py` port to ROCm/HIP — feasible but adds overhead

---

## Integration with stim-guard

Once validation runs produce data, results feed back into `stim-guard`'s
Entropy Check calibration:

```python
# stim_guard/loops.py — entropy_check() threshold update
# Calibrate bits_per_joule_threshold from empirical autoresearch results
bits_per_joule_threshold = gpd.calculate_threshold(
    baseline_val_bpb=results.baseline,
    landauer_limit=gpd.landauer_limit(temp_kelvin=300),
    safety_margin=2.0   # 2x Landauer as minimum acceptable efficiency
)
```

This closes the loop: autoresearch generates empirical data → GPD verifies
thermodynamic validity → stim-guard Entropy Check threshold is calibrated
to physics, not heuristics.

---

## Citation

```
Karpathy, A. (2025). autoresearch. GitHub: karpathy/autoresearch.
Physical Superintelligence PBC. (2026). Get Physics Done (GPD).
  GitHub: psi-oss/get-physics-done. Apache 2.0.
Steward, G. (2026). STIM White Paper v7.0004. STIM-Protocol/white-paper.
```

---

*"The metabolism runs until convergence. Stasis through inferred memory."*
