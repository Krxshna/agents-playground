# ADK Agents Playground

A collection of Google ADK sample agents demonstrating common patterns, including tool-augmented agents, function tools, LangChain integration, sequential workflows, parallel execution, and loop-based refinement.

## Getting started

### 1. Create a Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install required packages

This repository uses Google ADK and related Python tooling. Install dependencies as needed for your environment.

```bash
pip install google-generativeai langchain langchain-community requests
```

> If your project already has a specific dependency file, install from that instead.

### 3. Configure credentials

Make sure your Google ADK credentials and any provider-specific environment variables are set in your shell or `.env` files within each example folder.

Common variables may include:

- `GOOGLE_API_KEY`

## Running an example

Each folder exposes a `root_agent` object, which is the example agent ready to execute.
Use your ADK runtime or application code to load and run the sample agent.

Example usage pattern:

```python
from loop_agent.agent import root_agent

# Use your ADK runtime to execute the root_agent with the expected inputs.
# For example, pass a prompt or data payload to the agent runtime.

print(root_agent)
```

> The exact execution API depends on your ADK setup and runtime.

## How to extend

1. Copy an existing example folder.
2. Build a new `agent.py` with a `root_agent` definition.
3. Add any custom tools, new workflows, or new model instructions.
4. Update this README with your new agent example.

## Notes

- Each example is intentionally small and focused on one ADK pattern.
- `root_agent` is the primary entrypoint for each sample.
- Use `.env` files inside example folders to keep configuration local and separate.

## Contributing

Contributions are welcome. Add new agents, improve instructions, or add sample prompts and workflows.

---

Built for the ADK agents playground with a practical focus on reusable patterns, tool integration, and workflow composition.
