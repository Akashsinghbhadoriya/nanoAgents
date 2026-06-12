# nanoAgents

A minimal implementation of AI agent systems from first principles.

Inspired by Andrej Karpathy's nanoGPT, this project focuses on understanding the fundamental building blocks behind modern agent architectures rather than relying on high-level frameworks.

The repository starts with simple tool calling and gradually evolves into memory systems, planning, reasoning loops, evaluation frameworks, and eventually multi-agent simulations.

## Philosophy

Modern agent frameworks hide a significant amount of complexity behind abstractions.

The goal of nanoAgents is to expose these abstractions and rebuild them step-by-step.

Each component should be:

* Small
* Readable
* Educational
* Incrementally extensible

## Learning Roadmap

### Phase 1: Tool Use

* Tool Interface
* Tool Registry
* Structured Tool Calls
* LLM-Based Tool Selection

### Phase 2: Reasoning

* Observations
* ReAct Loop
* Multi-Step Execution

### Phase 3: Memory

* Conversation Memory
* Long-Term Memory
* Memory Retrieval

### Phase 4: Planning

* Goal Decomposition
* Task Generation
* Execution Planning

### Phase 5: Evaluation

* Task Success Metrics
* Tool Accuracy
* Agent Benchmarks

### Phase 6: Multi-Agent Systems

* Agent Communication
* Collaboration
* Delegation

### Phase 7: Agent Civilizations

* Citizens as Agents
* Goals and Motivations
* Resource Management
* Social Structures
* Emergent Behaviors

## Current Architecture

```text
User
 ↓
Agent
 ↓
Selector
 ↓
ToolCall
 ↓
ToolRegistry
 ↓
Tool
```

## Project Structure

```text
nanoAgents/

├── agent/
├── tools/
├── llm/
├── memory/
├── planning/
├── evaluation/
├── tests/
└── main.py
```

## Long-Term Vision

The final goal is to create a civilization simulator where every citizen is an autonomous agent composed of the primitives developed throughout this repository.

Rather than building the simulator directly, we first learn and implement each primitive independently, then combine them into increasingly complex systems.

Learn primitives first.
Build systems second.
Understand abstractions always.

```
```
