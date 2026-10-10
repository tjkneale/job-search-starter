# Guided onboarding

In a Codex chat opened in your own local copy of this repo, send:

```text
$job-setup
```

Or say: “Help me set up this repo and show me how to use it.” If skill selection is unavailable, ask the assistant to follow this guide. This is a chat request; the Python commands elsewhere in the README are terminal commands that the assistant can run for you. Codex documents [repository skills and explicit invocation](https://learn.chatgpt.com/docs/build-skills).

The guide supports a fictional-data tour, personal setup, or a shortcut to a first task. You can say “skip,” “pause,” “show an example,” or “resume setup.” Personal progress is kept in `workspace/setup.md`; a tour needs no personal facts.

## Instructions for the guiding assistant

### Start with the user's purpose

Introduce the repo in one sentence: it keeps job-search context and evidence so research, networking, applications, and preparation can reuse each other's work. Briefly name the capability groups: candidate context; opportunities and companies; networking; applications and interviews; conversation outcomes and review; optional activity records, consulting, compensation, schedules, and CRM.

Use the user's already-stated goal. If needed, offer one short choice: “Would you like a tour with fictional examples, setup for your own search, or help with a task you have now?” Do not start with a long questionnaire or all the task prompts. Ask in ordinary chat, or a supported question UI, and wait for the answer when it changes the next action. Never interpret silence as a supplied personal fact. Adapt explanations to the user's familiarity; technical configuration is conditional.

### Establish the local copy

Locate this repo by its `AGENTS.md`, `scripts/job_search.py`, and templates; operate from its root rather than assuming the chat's current directory is correct. Inspect existing `workspace/` and `workspace/setup.md` before writing. A returning user resumes from actual files and recorded preferences; a blank template is not evidence of completed setup.

Explain that the public starter's examples are invented, templates provide blank structure, and personal work goes under `workspace/`. A local downloaded copy is sufficient. For GitHub ownership, recommend **Use this template → Create a new repository → Private**, then downloading or cloning that personal copy and opening its folder in Codex. If the user is viewing only the GitHub page, guide them through obtaining/opening local files before claiming to run anything. Do not create a remote, change repository visibility, or push files merely because setup was requested.

Check the existing `.gitignore`; when Git is available, verify `workspace/profile/candidate.md` is ignored with `git check-ignore`. If personal files are already tracked or ignore rules are missing, explain the actual issue and repair only the authorized local setup before adding real data. An ignore rule does not remove committed history. Do not move private files into public folders. This step does not require collecting passwords or account keys.

### Show one connected example

If the user wants to jump directly to a task, skip or defer this demonstration and reuse their available context. Otherwise, find a Python 3.10+ runtime if available, using the environment's bundled runtime discovery when supported. Run `python3 scripts/job_search.py demo` and `python3 scripts/job_search.py check --root examples`, substituting the actual available runtime. Explain the result: one fictional role is being pursued after a conversation; another closed before application; research scores and pending personal actions are separate states. Open the example role and evidence rather than treating the script's summary as the entire tour.

If Python or shell access is missing, continue by reading the Markdown examples and say which commands were not run. Basic orientation does not require installing software, credentials, or connecting accounts. If the user wants software installation, explain the specific need and use their existing authorization. Do not imply the demo verified live employers.

For tour-only mode, continue through [the capability tour](capability-tour.md), keep examples unchanged, and do not initialize or alter personal records. If the user requests practice, demonstrate only their chosen scope using the fictional evidence and label any new demonstration as fictional. For requested fictional practice, use chat or a temporary scratch folder; keep new demo outputs out of the personal workspace and published examples. A real task requires a deliberate switch to their own context.

### Build the user's context gradually

For personal setup, run `python3 scripts/job_search.py init` only if `workspace/` does not exist. Initialization is part of the requested local setup and copies blank records. If a workspace already exists, preserve it; create only missing blank scaffold files when needed, without replacing existing content. Never reset a workspace to fix a structural check.

Collect context in small conversational batches, reusing facts already supplied:

1. **Direction:** what help would be most useful now, desired role/scope, preferred name if they want it saved, and timezone when dated work requires it.
2. **Practical criteria:** location/work mode and relevant work authorization, timing, compensation preferences if needed, and any material values preferences. Unknowns can stay open; avoid requesting full addresses, account identifiers, or unrelated personal history.
3. **Resume and evidence:** use a supplied current resume or employment/accomplishment notes. Preserve the original document and record its exact path/version. Ask before treating an uncertain metric as an approved external claim. A user without a resume can begin with a few supported notes.

Save only provided facts in `workspace/profile/candidate.md`, `workspace/profile/evidence.md`, and `workspace/strategy/criteria.md`. Keep confidential corroboration separate from public-use wording. The user's criteria replace all fictional example preferences. Do not insist every blank field be completed before doing useful work.

Update `workspace/setup.md` with mode, topics actually introduced or practiced, needed tools, open facts, and next step. Mark skipped steps as skipped, not completed. Run the personal structure check after initialization or relevant edits; it does not establish that candidate intake is complete or evidence is true. Fix issues introduced by the task without deleting personal history.

### Teach the capabilities and complete a first task

Use [the tour](capability-tour.md) in a few conversational groups. For each capability explain what it helps with, what the user supplies, show its example or relevant existing record, and give the exact chat prompt and expected output location. Introduce all groups during a requested full orientation; let a user with an urgent task defer the longer tour and record what remains. Do not claim that pasting a prompt ran the task.

Ask which first task would help, unless already chosen. Good starting points are assessing a supplied posting, preparing a near-term conversation, or developing one accomplishment story. Load that focused skill/workflow and carry out the requested local research/preparation with the user's actual evidence. If required web or document tools are unavailable, offer the supported alternative, such as analyzing a supplied posting or producing a Markdown brief, and state its actual limits. Show the saved result and how it connects to the rest of the workspace.

Explain optional browsing/accounts, document/spreadsheet tools, recurring work, and CRM only to the depth the user needs. No schedule, application, outreach, or external-service write is activated by this onboarding skill. If the user expressly requests an optional integration or schedule, treat it as a separate authorized task using their own account and settings.

### Finish or resume

Summarize what actually exists, any remaining decisions or tool needs, and one next useful action. Give a repeatable task prompt and the resume request: “Use $job-setup to resume my setup.” Keep `workspace/setup.md` accurate when personal mode is active. In tour-only mode, give a brief recap and the same resume request without creating personal state. Completing setup does not require every optional integration or a full professional-history audit.
