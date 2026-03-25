# SafeLLM Guardrails

This project implements guardrails for Large Language Models to prevent harmful outputs and prompt injection attacks.

Features:
- Prompt injection detection
- Harmful query filtering
- Output guardrails
- Safe response enforcement
- Logging system

Architecture:
User → Guardrails → LLM → Output Filter → Safe Response

Installation:

pip install -r requirements.txt

Run:

python app.py

Demo:

The system blocks harmful prompts and allows safe queries.

Example:

Input: how to hack bank account  
Output: blocked

Input: hello  
Output: allowed