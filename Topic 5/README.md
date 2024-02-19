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
git add .
git commit -m "Source branch"
git push
```

```bash
git status
```

```bash
git log --oneline
```

```bash
git checkout main
```


```bash
git cherry-pick <hash>
```

```bash
git cherry-pick <from hash>..<to hash>
```

```bash
git cherry-pick --continue
```