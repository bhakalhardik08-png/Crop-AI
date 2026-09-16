# Security

## Reporting a vulnerability

Please do not publish secrets, credentials, or private information in an issue.

If you find a security problem in this project, contact the repository owner privately through GitHub before publicly disclosing the details.

## Repository hygiene

- API keys and credentials should never be committed.
- Local datasets and private files are excluded through `.gitignore`.
- Keras model artifacts are managed with Git LFS.
- Before pushing changes, review `git status` and the staged file list.

This project does not intentionally require API keys for its local inference workflow.
