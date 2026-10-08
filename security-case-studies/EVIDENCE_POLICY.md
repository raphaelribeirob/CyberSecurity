# Evidence and responsible disclosure policy

## Source versus proof
The author's private Instant projects were reviewed **by reading selected code and test files**. Their security was not proven in production. A test present in a private repository is not proof it ran successfully. Reproduced synthetic logic is not proof the original application is safe.

## Public boundaries
- Do not commit proprietary source copied from a private repository, internal endpoint details, customer data, security incidents, access tokens or configuration secrets.
- All examples must use invented users, timestamps, objects, account references and mock events.
- Reference projects by approved product name and general technical category; do not publish private code extracts or unapproved internal architecture.
- Never publish instructions targeting real Instant customer services or vulnerability findings that have not been coordinated.
- Do not assign personal authorship to work merely because an AI assistant generated it. Disclose AI-assisted development accurately when relevant.

## Evidence to publish after doing an exercise
- Scope and explicit permission
- Date and tool versions
- Threat hypothesis / expected behavior
- Reproducible commands or tests
- Sanitized observed results and failing/negative cases
- Interpretation, residual risks, limitations
- What the author personally executed or changed

## Claim-language examples
- Accurate: "Reviewed access-control guards and created independent negative authorization tests using synthetic accounts."
- Accurate: "Public educational example tests passed in GitHub Actions" (only once observed).
- Misleading: "Secured production payments" without a deployment-level assessment.
- Misleading: "OWASP certified" because a project includes OWASP-oriented checks.

## Rules of engagement
Use systems you own or are explicitly authorized to assess, with rate limits and safe test data. Inform the appropriate owner about any material finding before public disclosure.
