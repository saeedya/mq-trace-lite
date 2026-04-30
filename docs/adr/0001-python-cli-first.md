# ADR 0001 — Python CLI-First Architecture

## Status

Accepted

---

## Context

MQ Trace Lite is an early-stage tool designed to help engineers inspect and debug IBM MQ messages during incidents.

The primary user is a DevOps or backend engineer who needs a fast, simple, and scriptable tool.

---

## Decision

We choose:

- Python as the primary language
- CLI-first approach for the MVP

---

## Rationale

### Why Python

- Fast development speed
- Strong ecosystem for scripting and automation
- Fits DevOps workflows
- Lower friction for iteration and experimentation

---

### Why CLI-first

- Faster to build than UI
- Better suited for incident scenarios
- Easy to integrate into scripts and pipelines
- No need for browser/UI complexity in MVP

---

## Consequences

### Positive

- Rapid MVP delivery
- Lower development overhead
- Easier debugging and testing

### Negative

- Less user-friendly than UI
- Not suitable for non-technical users
- May require redesign if evolving into a full platform

---

## Future Considerations

- Add API layer (FastAPI)
- Add UI if needed
- Possibly re-evaluate language (e.g., Java) for enterprise scaling