GhostBuild-X AI Agent Instructions

Project

GhostBuild-X is an Intent-to-Execution Compiler.

It converts a software idea into:

- Requirements
- Constraints
- Architecture
- Project structure
- Starter code
- Tests
- AI agent instructions
- Development tasks

Main Rule

GhostBuild-X must always preserve:

1. User intent
2. Requirements
3. Constraints
4. Architecture decisions
5. Development rules
6. Validation requirements

Do not treat GhostBuild-X as a simple code generator.

Main Modules

- Intent Parser: Understands the user's idea and requirements.
- Constraint Engine: Adjusts technical decisions based on constraints.
- Scaffold Generator: Creates project files and starter code.
- Repo Brain: Creates instructions for developers and AI agents.
- Validation: Checks code, tests, configuration, and architecture.
- Delivery Planner: Creates tasks, milestones, and development plans.

Development Rules

- Keep each module simple and independent.
- Write clean and readable code.
- Avoid unnecessary dependencies.
- Always respect user requirements and constraints.
- Do not change requirements without a clear reason.
- Explain important technical decisions.
- Add validation instructions to generated projects.
- Keep AI agent instructions clear and consistent.

AI Agent Rules

Before changing code:

1. Read README.md.
2. Read AGENTS.md.
3. Understand the relevant module.
4. Check the existing architecture.
5. Check related tests.
6. Make the smallest required change.

After changing code:

1. Run relevant tests.
2. Check configuration.
3. Check documentation.
4. Make sure the architecture is still consistent.
5. Report any remaining problems.

Constraint Rules

User constraints have high priority.

For example, if a project requires:

- Offline support
- Low memory usage
- Zero cloud cost
- Privacy
- Fast development

Do not introduce a solution that conflicts with these requirements without clearly identifying the conflict.

Code Quality

- Use clear names.
- Keep functions small.
- Keep modules independent.
- Handle errors clearly.
- Write testable code.
- Avoid duplicate code.
- Avoid unnecessary complexity.
- Do not add unused code.

Security

Never commit:

- API keys
- Passwords
- Access tokens
- Private credentials
- Secret configuration files

Use ".env.example" for environment variables.

Never commit a real ".env" file containing secrets.

Definition of Done

A feature is complete only when:

- Code is implemented.
- Relevant tests are added.
- Tests pass.
- Configuration is documented.
- Documentation is updated when needed.
- User constraints are satisfied.
- Architecture remains consistent.

Final Principle

GhostBuild-X must create software that humans and AI agents can understand, maintain, test, and continue building.
