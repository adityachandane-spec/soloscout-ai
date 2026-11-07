# SoloScout AI

An AI agent concept that discovers opportunities and checks whether students can apply.

> **Current status: Prototype v0.1.** This repository currently contains a local eligibility-checking demo using clearly labelled illustrative records. It does **not** yet search the live web or provide verified real-world opportunities.

## Current features

- Student profile inputs: age, education level, solo preference and fee budget.
- Transparent rule-based checks for age, education, team size and fee.
- Three-valued outcomes: pass, fail or unknown.
- Overall result distinguishes likely eligibility from cases needing verification.
- Sample records are explicitly labelled as demo data, not real events.

## Run locally

1. Install Python 3.10 or newer.
2. Clone this repository:

   `git clone https://github.com/adityachandane-spec/soloscout-ai.git`

3. Enter the project folder:

   `cd soloscout-ai`

4. Create and activate a virtual environment (recommended):

   **Windows PowerShell**
   `python -m venv .venv`
   `.\.venv\Scripts\Activate.ps1`

   **macOS/Linux**
   `python3 -m venv .venv`
   `source .venv/bin/activate`

5. Install dependencies:

   `pip install -r requirements.txt`

6. Start the app:

   `streamlit run app.py`

## Safety and accuracy

- Missing requirements are reported as **unknown**, never silently treated as eligible.
- Always verify deadlines, age rules, fees and team requirements on the organiser's official page.
- Do not commit API keys, passwords or private personal data.

## Roadmap

- [x] Initial Streamlit interface
- [x] Transparent eligibility rules engine
- [ ] Live opportunity search
- [ ] Official-page content extraction
- [ ] Evidence snippets and source timestamps
- [ ] AI agent planning and tool orchestration
- [ ] Evaluation dataset and accuracy report
- [ ] Deployment and demo video

## Project

Built for learning and hackathon development. The implementation and roadmap will evolve as the official competition problem statement is reviewed.
