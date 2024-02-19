## Creating and Merging Branches

<hr />

**a. Create a new branch named "feature-branch". Switch to the "master" branch. Merge the "feature-branch" into "master".**


```bash
git branch feature-branch
```

```bash
git checkout feature-branch
```

```bash
git add .
```

```bash
git commit -m "<message>"
```

```bash
git push origin feature-branch:main
```

<hr />

**b. Write the command to stash your changes switch branches and then apply the stashed changes.**


```bash
git checkout new-branch
```

```bash
git stash
```