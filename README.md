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