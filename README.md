# Job Search Starter

**Start here:** create your own private copy with **Use this template**, open its local folder in Codex, and send this in chat:

```text
$job-setup
```

The agent will explain the capabilities with fictional examples, help you set up your own search, and guide you through a first useful task. You can choose a tour only, skip steps, or resume later. You can also say “Help me set up this repo and show me how to use it.” [Guided onboarding](docs/onboarding.md) explains the steps.

A personal job-search workspace for an AI assistant: research opportunities, explore networking paths, prepare applications and interviews, and carry evidence and decisions from one task into the next.

This is a standalone starter offered as a one-time handoff. There is no scheduled maintenance or support commitment, upstream synchronization, or dependency on the creator's private workspace. You own and adapt your copy. Reuse is covered by the [MIT license](LICENSE).

## Try it without accounts

Python 3.10 or later is the only dependency for the local utilities. From this directory:

```bash
python3 scripts/job_search.py demo
python3 scripts/job_search.py check --root examples
```

[The walkthrough](examples/README.md) follows a fictional candidate through a complete sample search. Every person, employer, achievement, posting, conversation, and activity in `examples/` is invented. Example URLs use the reserved `.example` domain; they are not live postings or documentary evidence. The demo reads local files and makes no network requests.

## Make it yours

1. On GitHub, choose **Use this template → Create a new repository** and select **Private** for your personal copy. You can also use a downloaded copy locally.
2. Open your local copy in Codex and send `$job-setup` in chat. The agent runs available local commands, introduces the examples, and helps collect only the context needed to begin.
3. Choose a first task, such as assessing a posting or preparing a conversation. Personal records and setup progress stay in gitignored `workspace/`; you can ask to resume setup later.
4. For later work, ask for an outcome or name a skill: “Use $job-role-research to assess this posting against my criteria.”

Prefer manual setup? Run `python3 scripts/job_search.py init` in a terminal, then follow [Setup](docs/setup.md). It creates blank records and refuses to overwrite existing work.

The skills in `.agents/skills/` route to the procedures below. Research uses available web/browser tools; document authoring uses your assistant's document tools. These tools and connected accounts are not bundled. Markdown preparation works without artifact tools. Invoking a skill does not contact anyone or create an automation.

## Capabilities

| Outcome | Entry point | Fictional demonstration |
| --- | --- | --- |
| Discover and assess roles | [Role research](docs/workflows/role-research.md) | [Role brief](examples/opportunities/roles/cedarline-product.md) |
| Explore networking paths | [LAMP networking](docs/workflows/lamp-networking.md) | [Company list](examples/opportunities/company-list.csv), [evidence](examples/research/networking.md) |
| Refresh company posting urgency | [LAMP Posting](docs/workflows/lamp-posting.md) | [Posting evidence](examples/research/postings.md) |
| Investigate an employer | [Company diligence](docs/workflows/company-diligence.md) | [Company brief](examples/opportunities/companies/cedarline.md) |
| Draft a short request for advice | [Networking email](docs/workflows/networking-email.md) | [Draft request](examples/networking/request.md) |
| Prepare a conversation or interview | [Conversation prep](docs/workflows/conversation-prep.md) | [Prep brief](examples/interview/cedarline-prep.md) |
| Tailor an application package | [Application package](docs/workflows/application-package.md) | [Manifest and answers](examples/resumes/applications/cedarline/package.md) |
| Develop evidence-backed stories | [Interview stories](docs/workflows/interview-story.md) | [Story](examples/interview/stories/pilot.md) |
| Capture completed conversations | [Conversation capture](docs/workflows/conversation-capture.md) | [Notes](examples/opportunities/conversations/cedarline.md) |
| Review the search and next actions | [Search review](docs/workflows/search-review.md) | [Review](examples/research/search-review.md) |
| Build positioning and audit public profiles | [Additional tasks](docs/additional-tasks.md) | [Positioning](examples/profile/positioning.md) |
| Compare compensation or test consulting work | [Additional tasks](docs/additional-tasks.md) | [Compensation](examples/strategy/compensation.md), [consulting](examples/strategy/consulting.md) |
| Preserve personal activity evidence | [Activity records](docs/activity-records.md) | [Activity log](examples/profile/activity-log.md) |
| Plan recurring work or a CRM mirror | [Automations](docs/automations.md), [integrations](docs/integrations.md) | [Offline CRM metadata preview](docs/integrations.md) |

[The task menu](docs/workflows.md) has copyable prompts. [The data model](docs/data-model.md) explains authority, stages, and evidence. [Sharing](docs/sharing.md) explains how to keep personal records out of the published starter.

No accounts, credentials, real records, Git history from a private search, or active schedules are included. The starter uses CSV for its small company list so the demo needs no spreadsheet library. Spreadsheet users can adapt the documented headers; no Excel editor, ATS collector, live CRM adapter, or equity simulator is bundled.
