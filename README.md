# PeachBot Edge

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/peachbotAI/peachbot-edge/releases)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Tests](https://img.shields.io/badge/pytest-passing-brightgreen.svg)](https://github.com/peachbotAI/peachbot-edge/actions)
[![Architecture](https://img.shields.io/badge/architecture-Edge__Native-orange.svg)](#)
[![Execution](https://img.shields.io/badge/execution-Deterministic-purple.svg)](#)

### Edge-Native Execution Layer for Deterministic Biological Intelligence

---

## Overview

**PeachBot Edge** is the execution layer of the PeachBot ecosystem — a **deterministic, edge-native intelligence engine** designed for biological, clinical, and scientific systems.

It enables **on-device computation**, **stateful reasoning**, and **federated coordination**, without reliance on cloud infrastructure or large language models.

> ⚠️ This is **not** a diagnostic system and does **not** provide medical decisions.
> It is a **scientific alerting and computation infrastructure**.

---

## Documentation

For deep dives into system mechanics, underlying theory, and deployment constraints, refer to the official documentation:

* [System Architecture](docs/architecture.md) — Detailed breakdown of the execution pipeline and constraints.
* [Scientific Foundations](docs/scientific_foundations.md) — The biological and computational theory driving the system (SBC, Graph Theory, FILA).
* [Disclaimers](docs/disclaimers.md) — Crucial legal, medical, and operational boundaries.

---
## 🚀 Quick Start
```bash
python -m src.main
```
## Core Principles

* **Edge-First** — All core computation runs locally
* **Deterministic Execution** — No stochastic outputs, no hallucinations
* **Privacy-Preserving** — No raw data leaves the device
* **Modular Architecture** — Clean separation of execution, memory, and communication
* **Biologically-Inspired Computation (SBC)** — Feedback-driven, adaptive processing

---

## Meta-Execution Pipeline

*Note: While data traverses the system via a directed execution graph, the engine processes each node using the following deterministic pipeline:*

```text
Input Signal
     ↓
Signal Classification
     ↓
Context Construction
     ↓
Hardware-Aware Adaptation
     ↓
Safe Execution Sandbox
     ↓
Core Module Execution (peachbot-core)
     ↓
Memory Update (State + Priority + Decay)
     ↓
Federation (FILA - Metadata Exchange)
     ↓
Adaptive Graph Routing
```

---

## Key Components

### 🔹 Runtime Engine
* Adaptive graph execution
* Conditional branching
* Deterministic processing pipeline

### 🔹 SBC Engine (Synthetic Biological Computation)
* Feedback loops
* Memory-driven behavior
* State-aware execution

### 🔹 Memory Intelligence Layer
* Weighted memory (priority-based)
* Reinforcement & decay
* Selective retention

### 🔹 Signal & Context Layer
* Signal classification (normal / anomaly / critical)
* Context-aware execution

### 🔹 Safety Layer
* Fault isolation
* Timeout handling
* Deterministic fallback

### 🔹 Hardware Awareness Layer
* CPU & memory profiling
* Adaptive execution modes:
  * `performance`
  * `balanced`
  * `safe`

### 🔹 FILA (Federated Intelligence Layer Adapter)
* Metadata-only communication
* No raw data transfer
* Distributed awareness across nodes

---

## Project Structure

```bash
src/
  runtime/
    graph/          # Execution graph + executor
    state/          # Memory + intelligence
    signal/         # Signal classification + context
    safety/         # Execution guards + fallback
    hardware/       # Device profiling + adaptation

  communication/
    fila/           # Federated metadata layer

  core_bridge/      # Interface to peachbot-core
  monitoring/       # Logging system
  contracts/        # Data contracts

configs/
  config.yaml       # All tunable parameters

tests/              # Full system validation
docs/               # Full Documentation
```

---

## Prerequisites

* **Python 3.10+**
* Linux / macOS (Windows supported via WSL2)
* Minimum 1GB RAM (for `balanced` execution mode)

---

## Installation

### 1. Clone Repository
```bash
git clone [https://github.com/peachbotAI/peachbot-edge.git](https://github.com/peachbotAI/peachbot-edge.git)
cd peachbot-edge
```

### 2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Run the System

```bash
python -m src.main
```

You will see:
* Boot banner
* System configuration
* Execution logs
* Adaptive graph execution

---

## Quick Start: Triggering an Execution

Once the system is running, you can simulate an incoming biological or environmental signal by dispatching a payload to the runtime:

```python
# example_dispatch.py
from src.runtime.graph.executor import GraphExecutor
from src.contracts.payload import SignalPayload

executor = GraphExecutor()

# Construct a test signal
signal = SignalPayload(
    source="medai_sensor_01",
    data={"heart_rate": 120, "spo2": 94},
    priority=1.5
)

# Dispatch and observe deterministic routing
result = executor.dispatch(signal)
print(f"Final State: {result.state}")
```

---

## Run Tests

```bash
pytest -v
```

Expected:
```
ALL TESTS PASSED
```

---

## Configuration

All behavioral tuning is externalized. No hardcoded tuning parameters exist in the runtime logic.

📁 `configs/config.yaml`

Example:
```yaml
runtime:
  timeout: 2

memory:
  decay:
    weak: 0.9
    strong: 0.95
  threshold:
    removal: 0.3

priority:
  base: 1.0
  weights:
    anomaly: 2.0
    memory_seen: 1.0
    complexity: 0.5
```

---

## Integration with `peachbot-core`

PeachBot Edge executes modules defined in **peachbot-core**:

```python
core_executor.execute(module_name="medai", data=payload)
```

* Modular plug-in system
* No tight coupling
* Supports multi-domain intelligence:
  * MedAI
  * Eco
  * AgriAI
  * Bio

---

## What Makes PeachBot Edge Unique

* Not an API wrapper
* Not an LLM-based system
* Not a diagnostic engine

It is:
> **Edge-native deterministic intelligence infrastructure for scientific systems**

---

## Roadmap (High-Level)

* Hardware-level scheduling optimization
* Real federated node communication via FILA
* Domain-specific intelligence modules
* Self-evolving execution graphs

---

## Citation

If you use PeachBot Edge in research or production, please cite:

```bibtex
@software{peachbot_edge_2026,
  author = {Swapin Vidya},
  title = {PeachBot Edge: Edge-Native Deterministic Intelligence Engine},
  year = {2026},
  version = {0.1.0},
  url = {[https://github.com/peachbotAI/peachbot-edge](https://github.com/peachbotAI/peachbot-edge)}
}
```

---

## License

This project is licensed under the **Apache License, Version 2.0**.

You are free to:
* Use the software commercially
* Modify and distribute it
* Integrate it into proprietary systems

Under the following conditions:
* Include a copy of the license (`LICENSE`)
* Provide proper attribution
* State any significant changes made

For full terms, see the `LICENSE` file.

---

## Contributions

Contributions are welcome and must follow the guidelines defined in `CONTRIBUTING.md`.

By contributing, you agree that:
* Your contributions will be licensed under **Apache License 2.0**
* You adhere to system principles:
  * Deterministic execution
  * Privacy-preserving design
  * Config-driven behavior (no hardcoding)

Before submitting a PR, ensure all tests pass:
```bash
pytest -v
```

---

## Disclaimer

PeachBot Edge is **not a medical device, diagnostic tool, or clinical decision system**. 

All outputs should be interpreted as computational signals, system-level alerts, or research insights. Use in real-world environments is the responsibility of the deploying entity. See `docs/disclaimers.md` for full details.