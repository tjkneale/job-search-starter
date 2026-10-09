# One-time sharing

Publish the generic starter with fresh history. It contains only methods, blank templates, code, and invented fixtures. Do not initialize publication from a private repository's `.git` directory, remotes, branches, tags, or old objects.

Before publishing, review every included file and the Git author identity. Confirm that only the intended starter content is present, no real records or credentials are staged, and `workspace/`, `.env`, downloads, and private evidence are ignored. Newly added binary documents need separate metadata and content review. A filename or ignore rule alone does not establish privacy.

Create a new GitHub repository from this clean directory, then enable **Template repository** in Settings as described in [GitHub's template guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository). Public visibility and the MIT license should be part of the publisher's final review. Do not push the private working repository.

A recipient uses **Use this template** to generate a private personal repository with independent history, or downloads the starter for local use. They add their own context and optional accounts. They can make all later changes in their copy. There is no automated update channel, expected upstream contribution, or maintenance promise.

If a recipient wants to share their own adapted starter later, export only generic methods and newly invented fixtures into another clean directory. Removing personal files from the latest version of an already public history is not an adequate export procedure.
