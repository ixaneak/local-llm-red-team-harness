# Local LLM Red Team Harness

A custom Python evaluation framework designed to test local Large Language Models (LLMs) for prompt injection and data leakage vulnerabilities. 

## Overview
This project was developed to systematically evaluate the security posture of locally hosted LLMs. It simulates a real-world scenario where an AI system is tasked with protecting sensitive information (a secret token) while interacting with user inputs. The harness automates the testing process, evaluates the model's responses for data leakage, and logs the results for analysis.

## Architecture & Components
- **`ask.py`**: The core interaction loop. It handles API communication with a local Ollama instance, iterates through test prompts, and saves raw model responses to a JSON file.
- **`rules.py`**: Implements the simulated environment (e.g., a proprietary "Ice Cream Shop" scenario). It contains a system prompt with a hidden secret code word and includes a custom leak-checking mechanism to detect if the model attempts to exfiltrate the token.
- **`test.py`**: Auxiliary testing script for specific edge cases or targeted adversarial prompts.
- **`results.json` / `rules_results.json`**: Structured logs capturing the input prompts, model outputs, and leak-checker evaluations for post-test analysis.
- **`.gitignore`**: Ensures cache files, virtual environments, and sensitive local configurations are not committed to the repository.

## Test Scenario
The primary test evaluates the model's resistance to prompt injection and indirect data extraction. The system prompt defines a strict operational boundary (the "Ice Cream Shop" rules) and embeds a secret code word representing sensitive corporate data (e.g., an API key or PII). The red teaming process attempts to bypass these boundaries using various adversarial techniques to extract the secret.

## Setup & Execution
### Prerequisites
1. Install [Ollama](https://ollama.com/) and pull the target model:
   ```bash
   ollama pull llama3.2
