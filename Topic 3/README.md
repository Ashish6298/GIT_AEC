# Collaboration & Remote repository

<hr />

**a. Clone a remote git repository to your local machine.**
**b. Fetch the latest changes from a remote repository and rebase your local branch on to the updated remote branch.**
**c. Write the command to merge "feature-branch" into "master" by providing a custom commit message for the merge.**

```bash
git clone <url>
```

```bash
git checkout -b feature-branch
```

Make some changes

```bash
git add .
git commit -m "Changes"
```

```bash
git fetch origin
```

```bash
git rebase origin/main
```

```bash
git push origin feature-branch
```

```bash
git merge feature-branch
```

```bash
git pull origin feature-branch  
```

```bash
git push
```