# Get latest release tag

This action query GitHub API releases endpoint and get the latest release tag using a regex

## Inputs

| Input        | Required | Description                              |
|--------------|----------|------------------------------------------|
| github_token | yes      | GitHub token                             |
| regex        | yes      | regex pattern to match only certain tags |

## Outputs

| Output | Description                       |
|--------|-----------------------------------|
| tag    | Tag value extracted from releases |

## Usage

```yaml
- name: Update deployment container image
  uses: resuelve/latest-release-tag-action@master
    with:
      github_token: ${{ secrets.GITHUB_TOKEN }}
      regex: "some regex"
```

Enjoy 🎉
