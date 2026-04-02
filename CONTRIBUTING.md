# Contributing to PeachBot Edge

Thank you for your interest in contributing to **PeachBot Edge** — a deterministic, edge-native intelligence system designed for scientific and biological computation.

---

## Philosophy

PeachBot Edge is **not a typical software project**. Contributions must strictly follow these principles:

* **Deterministic Execution**
  No randomness, no probabilistic outputs, no hallucination-prone systems.

* **Privacy-First Design**
  No raw data leakage. All federation must be metadata-only (FILA compliant).

* **Edge-Native Operation**
  Core execution must not depend on cloud infrastructure.

* **Modular Architecture**
  Components must remain decoupled and extensible.

* **Config-Driven Behavior**
  No hardcoded thresholds, weights, or tuning parameters.

---

## Contribution Types

We welcome high-quality contributions in the following areas:

### Core Extensions

* New modules via `peachbot-core`
* Domain-specific execution logic (MedAI, Eco, AgriAI, Bio)

### Intelligence Systems

* Memory models (decay, reinforcement, prioritization)
* Signal classification improvements
* Context-aware execution logic

### Edge Optimization

* CPU/memory-aware optimizations
* Lightweight execution strategies
* Hardware-aware enhancements

### Testing & Validation

* Unit tests
* Integration tests
* Edge-case validation

### Documentation & Research

* Architecture documentation
* Technical write-ups
* Paper contributions / benchmarks

---

## Not Accepted

The following will be rejected:

* LLM-based or generative AI integrations
* Cloud-dependent execution logic
* Hardcoded parameters or thresholds
* Breaking deterministic guarantees
* Tight coupling between modules
* Any violation of privacy constraints

---

## Development Setup

```bash
git clone https://github.com/<your-org>/peachbot-edge.git
cd peachbot-edge

python -m venv .venv
source .venv/Scripts/activate   # Windows

pip install -r requirements.txt
```

---

## Testing

All contributions must pass:

```bash
pytest -v
```

### Requirements:

* No failing tests
* No skipped critical tests
* New features must include tests

---

## Code Guidelines

### General

* Use **type hints**
* Follow **clean modular design**
* Avoid global mutable state
* Keep functions small and composable

### Configuration

* All tunable parameters MUST go into:

  ```text
  configs/config.yaml
  ```
* No magic numbers in code

### Logging

* Use structured logging:

  ```python
  logger.info("[NODE] start | module=medai")
  ```

### Determinism

* No randomness unless explicitly controlled
* Same input → same output (strict requirement)

---

## Pull Request Process

1. **Fork the repository**
2. Create a new branch:

   ```bash
   git checkout -b feature/<your-feature-name>
   ```
3. Make your changes
4. Add/update tests
5. Run full test suite:

   ```bash
   pytest -v
   ```
6. Submit a Pull Request with:

### PR Must Include:

* Clear description
* Technical rationale
* Impact analysis
* Test coverage

---

## Architectural Constraints

Contributions must respect system layers:

```text
Runtime → Signal → Context → Execution → Memory → Federation
```

Do NOT:

* bypass layers
* inject shortcuts
* break flow integrity

---

## Security & Privacy

* No external API calls in core runtime
* No data exfiltration
* No logging of sensitive payloads
* FILA must remain metadata-only

---

## Citation Requirement

If your contribution is used in research:

* You must cite PeachBot Edge (see `CITATION.cff`)
* Contributions may be acknowledged in future publications

---

## License

By contributing, you agree that:

> Your contributions will be licensed under the **Apache License 2.0**

---

## Recognition

Contributors will be:

* Credited in repository history
* Acknowledged in documentation
* Referenced in research outputs (where applicable)

---

## Final Note

PeachBot Edge is **deep-tech infrastructure**, not an experimental playground.

Every contribution should move the system toward:

* higher reliability
* stronger determinism
* better edge performance
* scientifically grounded intelligence

---
