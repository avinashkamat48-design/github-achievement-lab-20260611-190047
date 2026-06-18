# Pull Request Planning

Before opening a pull request, write down:

- The smallest behavior or docs gap being changed
- The files expected to change
- The command that verifies the change
- What is intentionally out of scope

## Split When

- A docs change and code change can be reviewed independently
- A refactor is not required for the bug fix
- Tests reveal a second unrelated behavior

## Keep Together When

- The test only makes sense with the implementation
- The README update documents the exact new behavior
- The files form one reviewable story
