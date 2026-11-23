   # Expense Tracker CLI
     ![Test Suite](https://github.com/Adaora101/expense-tracker-cli/actions/workflows/test_suite.yml/badge.svg)
   A command-line app to add, edit, delete, and summarize personal expenses.

   ## Team Members
   - Adaora Obialo(Developer, Product Owner)

   ## Contact / Work Hours
   - Email: l00191840@atu.ie
   - Work hours: Mon–Fri, 9:00 AM – 5:00 PM

   ## Definition of Ready
   An issue is ready to be worked on when:
   - It has a clear user-story title
   - It has a priority and a size
   - It is assigned to an iteration and milestone
   - Acceptance criteria are written
   - It has no unresolved blockers

   ## Branching Strategy
   This project uses GitHub Flow:
   - main always holds working code and is never committed to directly.
   - Each issue gets its own branch (e.g. feature/5-edit-expense).
   - Work is merged into main through a pull request after the automated checks pass.
   - Branches are kept after merging so the full history is visible(This was not applied to     first few branches).

   ## CI/CD Pipeline Design
   The pipeline is split into separate workflows on purpose:
   - Single Test runs one test file and one individual test, so a developer can quickly check a single feature.
   - Test Suite runs every test with a coverage minimum of 80%.
   - Build & Package builds the installable package.

  