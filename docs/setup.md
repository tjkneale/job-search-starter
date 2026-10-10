# Setup

For agent-guided setup, send `$job-setup` in a chat opened in your local copy, or say “Help me set up this repo.” The [onboarding guide](onboarding.md) supports a fictional tour, gradual personal intake, a first task, and resumable progress. The steps below are the manual path.

Use a private personal copy for actual job-search work. The public starter remains reusable methods plus invented examples. GitHub's [template creation guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) describes making an independent copy with fresh history.

Run `python3 scripts/job_search.py init` from the repository root. The command creates `workspace/` from [blank workspace templates](../templates/workspace/README.md). It does not copy example data, connect accounts, or set up schedules. If `workspace/` exists, initialization stops without changing it.

Fill these first:

| Record | Minimum useful context |
| --- | --- |
| `workspace/profile/candidate.md` | Preferred name, timezone, employment history, factual title distinctions, public-use choices, and current resume path |
| `workspace/profile/evidence.md` | A few supported accomplishments, your contribution, metric definitions, sources, and what can be disclosed |
| `workspace/strategy/criteria.md` | Target roles, location/work authorization, compensation components, values preferences, and urgency |
| `workspace/resumes/master.md` or your supplied document | The exact resume baseline; retain your source document when you have one |

A new record starts with [a template](../templates/README.md). Save real outputs in the corresponding folders under `workspace/`; keep example files as references. `python3 scripts/job_search.py check` checks role structure, company-list headers, and research checkpoints. It does not verify the truth of a claim, a live posting, or activity eligibility.

Open this repository as a project in Codex to make `.agents/skills/` available. Use plain language or an explicit skill such as `$job-conversation-prep`. If your assistant does not support this skill format, ask it to follow the linked workflow directly. Available browsing, document tools, and connectors depend on your own environment.

Personal records are gitignored by default, even in a private copy. For versioned backups, use a separate private repository for `workspace/`, or deliberately change your private copy's ignore rule after confirming its visibility. Do not change the ignore rule in a copy you intend to publish. Ignoring a folder prevents new tracking; it does not remove files that were already committed.

Optional connected work is described in [integrations](integrations.md); requested recurring work is described in [automations](automations.md). Neither is needed for the offline example walkthrough.
