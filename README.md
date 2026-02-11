Python CI Demo 🚀
=================
=================
This repository demonstrates a CI workflow using:

- Python 3.11
- pytest for unit testing framework
- pytest-cov for test coverage 
- ruff for linting
- GitHub Actions for CI
- Branch protection rules enforcing:
    - Required status checks
    - Minimum 1 PR approval
    - Squash or rebase-only merges

This project is intentionally simple to highlight CI/CD best practices rather than application complexity.


📁 Project Structure
====================
    ZipTakeHome/
    │
    ├── src/demo/
    │   ├── __init__.py
    │   └── calculator.py
    │
    ├── tests/
    │   ├── __init__.py
    │   └── test_calculator.py
    │
    ├── .github/workflows/ci.yml
    ├── pyproject.toml
    ├── requirements-dev.txt
    └── README.md


🖥️ Local Development Setup
==========================
1️⃣ Clone the repository
    git clone https://github.com/selvaprasanna/ZipTakeHome.git 
    cd ZipTakeHome
2️⃣ Create a virtual environment
    python -m venv .venv
    source .venv/bin/activate  # Mac/Linux
    .venv\Scripts\activate     # Windows
3️⃣ Install dependencies
    pip install --upgrade pip
    pip install -r requirements-dev.txt
    pip install -e .


⚙️ CI Pipeline Overview
=======================
The GitHub Actions workflow lives in:
    .github/workflows/ci.yml

Trigger Conditions
The pipeline runs automatically:
- On every Pull Request targeting `main`
- On every push to main

CI Steps
The workflow has two jobs that performs:
1. Checkout repository
2. Setup Python 3.11
3. Install dependencies
4. Run ruff (lint) — 1st job 
5. Run pytest (unit tests) — 2nd job

If any step fails, the PR is blocked from merging.


🔒 Branch Protection Rules
==========================
The `main` branch is protected with the following requirements:
✅ Required Before Merge
- At least 1 PR approval
- All required status checks must pass (Lint Check and Unit Tests)
- Linear history required

✅ Allowed Merge Methods
- Squash merge
- Rebase merge


🔄 Pull Request Workflow
========================
1. Create a feature branch:
    git checkout -b feature/my-change
2. Make changes.
3. Run checks locally:
    ruff check .
    pytest
4. Push branch:
    git push -u origin feature/my-change
5. Open a PR.
6. Wait for CI to pass.
7. Get at least 1 approval.
8. Merge via squash or rebase.


🚨 Failure Modes
================
CI can fail for several reasons:
- Lint errors (ruff violations)
- Failing unit tests
- Dependency installation issues
- Python version mismatch
- Workflow misconfiguration
- branch protection bypasses 

If CI fails:
- Click the failed check
- Inspect logs
- Fix locally
- Push updates to PR


🔔 Notifications
================
GitHub sends notifications for:
- PR opened || Email & GitHub Notification => author
- Review requested || Email & GitHub Notification => author, reviewer
- CI check failure || Email & GitHub Notification => author, reviewer
- CI check Success || GitHub Notification => author, reviewer
- Merge completed || GitHub Notification => author, reviewer
- Main branch check failure || Email & GitHub Notification => admins, last author

Notification delivery depends on each user's GitHub settings:
- Web UI
- GitHub Mobile
- Email
- Slack Integration (additional option to implement)


Key Stakeholders
================
- Development Team (primary users of CI/CD pipeline) 
- Devops/Platform Team (maintain and optimize CI/CD Infra) 
- Tech Leads/ EMs (oversee process and make strategic decisions)
- QA Team (Define Quality Standards)
- Security Team (Ensure security compliance)