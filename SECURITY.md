# Security Policy

## Supported Versions

Version     Supported
1.x         :white_check_mark:
<1.0        :x:

## Reporting a Vulnerability

Please do not open a public issue for security problems.

1. Use the "Report a vulnerability" button under the Security tab of this repository, or email l00191840@atu.ie.
2. Include the affected version, steps to reproduce, and any relevant logs.
3. You can expect a reply within 5 working days.

## Security Practices in This Repo

- Dependabot alerts and security updates are enabled.
- Bandit and pip-audit run automatically in GitHub Actions.
- Secret scanning is enabled and secrets are excluded by .gitignore.
- main is protected: changes arrive through pull requests with passing checks.