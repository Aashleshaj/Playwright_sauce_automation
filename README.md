Playwright Sauce Demo Automation

Description

This repository contains an end-to-end automation framework for the SauceDemo e-commerce web application (https://www.saucedemo.com). The tests are written in Python using Pytest and Playwright, and they validate core user workflows such as login, inventory interaction, cart actions, and checkout validations.
The project demonstrates a scalable test architecture using the Page Object Model (POM) and includes reporting and configuration support.

Project Features

End-to-end UI automation tests for SauceDemo

Page Object Model (POM) design pattern

Pytest test runner

Playwright for browser automation

Structured test suite (login, products, cart)

HTML test reporting

Test fixtures and browser setup configuration

```
Project Structure
Playwright_sauce_automation/
├── pages/                # Page objects
├── tests/                # Test cases
├── reports/              # HTML and test reports
├── conftest.py           # Pytest fixtures (browser setup)
├── pytest.ini            # Pytest configuration
├── .gitignore            # Ignored files for Git
└── README.md             # Project documentation
```

Command to run
pytest .\tests\login_sauce.py

To save report in report folder while running file
pytest --html=reports/report.html .\tests\login_sauce.py

Installing Playwright-MCP in VScode
- **Install node JS** Download in your system([[Download NODE JS](https://nodejs.org/en/download)])
- **To add the Playwright server:** 
```
npx @google/gemini-cli mcp add playwright npx -y @playwright/mcp@latest
```
- Add API key of Gemini in Agent to able to gemini models instead of claude (paid model)
- Use below command to get All 3 agents in your folder(Planner, Generator, Healer)
```
npx playwright init-agents --loop=vscode
```

[Reference document for playwright MCP](https://www.shapemyinterview.com/resources/playwright-mcp-ai-agents-guide)

Follow below steps to run planner agent<br>
* Open Copilot chat<br>
* Select Gemini 3.1 Flash Lite model
* Select playwright-test-planner.agent.md in chat and provide below prompt<br>
@playwright-test-planner

Execute a static, low-interaction test planning cycle for [INSERT YOUR URL]. To avoid API rate limits, you must strictly follow these constraints:

1. **Single Observation:** Call `planner_setup_page` and review the initial `browser_snapshot` exactly once.
2. **NO Interactive Exploration:** Do NOT use `browser_click`, `browser_type`, or navigate away from the initial URL. Infer the entire user journey—from product selection all the way through the final checkout flow—directly from the static DOM snapshot.
3. **Comprehensive Coverage:** Design 10 to 12 detailed test scenarios. Ensure you cover happy paths (e.g., successful checkout), boundary conditions, and negative validations (e.g., leaving mandatory checkout payment fields blank).
4. **Immediate Export:** Once all scenarios are planned, use your bash tool to save the results directly to `data/manual_test_cases.xlsx`. Use the exact columns: `Test ID`, `Title`, `Description`, `Steps`, `Expected Outcome`, and `Priority`. Stop all operations immediately after the file is saved.

Follow below steps to run generator agent<br>
* Open Copilot chat<br>
* Select Gemini 3.1 Flash Lite model<br>
* Select playwright-test-generator.agent.md in chat and provide below prompt<br>
* 
@playwright-test-generator

Process ONLY the first 3 test cases (TC-001 to TC-003) from `data/manual_test_cases.xlsx`:

1. **Read & Audit:** Parse TC-001 through TC-003 from `data/manual_test_cases.xlsx`. Scan `pages/` and `tests/` to check if they already exist.
2. **Deduplicate:** Skip any of these 3 cases if already implemented.
3. **Automate in POM:** Extend Page Objects in `pages/` as needed, then write automated scripts in `tests/`.
4. **Stop:** Do not proceed to TC-004. Stop once TC-001 through TC-003 are processed.

Passing 3 testcase to automate at a time so limit will not get exhausted and model able to perform well.