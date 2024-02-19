## Analysing and Changing Git History

a) **Given a commit ID, how would you use Git to view the details of that specific commit, including the author, date, and commit message?** 

To view details of a specific commit:

```bash
git show <commit_id>
```

Replace <commit_id> with the actual commit hash you want to inspect.

Remember to replace placeholders like <commit_id> or specific dates with the actual values you're working with in your repository

b) **Write the command to list all commits made by the author "JohnDoe" between "2023-01-01" and "2023-12-31".**

To list commits made by the author "JohnDoe" between specific dates:

```bash
git log --author="JohnDoe" --after="2023-01-01" --before="2023-12-31"
```

c) **Write the command to display the last five commits in the repository's history.**

To display the last five commits in the repository's history:

```bash
git log -n 5
```

This will show the latest 5 commits in the repository.

d) **Write the command to undo the changes introduced by the commit with the ID "abc123".**

To undo changes introduced by a specific commit (assuming "abc123" is the commit ID):

```bash
git revert abc123
```

This command creates a new commit that undoes the changes made by the specified commit.