# Capability tour

The onboarding agent uses this guide in short groups. Introduce every group during a full tour, then practice the task the user chooses. The prompts below belong in chat, not a terminal. Real outputs go under `workspace/`; example links are invented demonstrations and must never become personal evidence.

## 1. Your facts and search direction

**Candidate context and positioning** keep titles, dates, accomplishments, and approved wording consistent. Supply your current resume or a few career notes; the agent helps build the profile and evidence register before polishing claims. An evidence register records what supports a claim and whether you want to use it publicly.

Example: [candidate context](../examples/profile/candidate.md), [evidence](../examples/profile/evidence.md), [positioning](../examples/profile/positioning.md).

Say: “Use my supplied resume and notes to build my candidate context and evidence register. Show missing facts and propose a career through-line.” Saves to `workspace/profile/`; public edits remain proposed until authorized.

**Compensation and consulting** are optional decision tasks. Supply your package components/preferences or a proposed paid service. The agent separates dependable recurring pay from uncertain or one-time components, and tests a consulting offer without calling interest signed income.

Examples: [compensation](../examples/strategy/compensation.md), [consulting](../examples/strategy/consulting.md). Say: “Compare these package components against my criteria and show the unknowns,” or “Help me test this consulting offer with a concrete buyer problem and validation plan.” Saves to `workspace/strategy/` using [additional tasks](additional-tasks.md).

## 2. Opportunities and companies

| Capability | Supply / chat prompt | Example and saved result |
| --- | --- | --- |
| Role research checks a posting and your fit | Posting link or description. “Use $job-role-research to assess this role against my criteria and save the next decision.” | [Role brief](../examples/opportunities/roles/cedarline-product.md); `workspace/opportunities/roles/` and tracker |
| Company diligence investigates the employer behind the role | Employer and what matters to you. “Use $job-company-diligence to investigate this employer and list the questions I should resolve.” | [Company brief](../examples/opportunities/companies/cedarline.md); `workspace/opportunities/companies/` and dated research |
| LAMP Posting checks urgency across target companies | Selected companies and target roles. “Use $job-lamp-posting to refresh these companies' official openings and preserve my other scores.” | [Posting evidence](../examples/research/postings.md); company-list Posting scores and research checkpoints |

Explain LAMP once: a company list combining candidate Advocacy and Motivation choices with Posting urgency; [the data model](data-model.md) defines the fields. A candidate interest decision is separate from the stage of actual contact or application. Live availability research needs web access; a pasted description supports analysis but cannot establish current board availability. Show [the closed role](../examples/opportunities/roles/harborlight-platform.md) to demonstrate retained history.

## 3. Networking

| Capability | Supply / chat prompt | Example and saved result |
| --- | --- | --- |
| LAMP networking finds credible potential introduction paths | Companies and known relationships. “Use $job-lamp-networking to research paths for these new or partial companies without changing my decisions.” | [Company list](../examples/opportunities/company-list.csv), [networking evidence](../examples/research/networking.md); private paths and dated checkpoints |
| Networking email drafts a brief request for insight | Recipient, actual relationship, and learning interest. “Use $job-networking-email to draft an informational-conversation request based on these facts.” | [Draft](../examples/networking/request.md); `workspace/networking/` when saving is useful |

A signed-in professional-network browser can verify your direct/mutual connections; public research cannot establish them. You can start with your own confirmed relationships without connecting an account. A potential path does not prove willingness to refer; drafting a request does not send it. Advocacy remains your choice.

## 4. Applications and interviews

| Capability | Supply / chat prompt | Example and saved result |
| --- | --- | --- |
| Application package adapts your current baseline to a role | Role, exact resume, requested answers, and output format. “Use $job-application-package with this resume and these questions; save a package for my review.” | [Manifest](../examples/resumes/applications/cedarline/package.md); `workspace/resumes/applications/<company-role>/` |
| Interview story develops a truthful episode you can reuse | Accomplishment notes and what you want it to demonstrate. “Use $job-interview-story to turn these notes into short and longer answers, with missing facts visible.” | [Story](../examples/interview/stories/pilot.md); `workspace/interview/stories/` and story bank |
| Conversation prep connects the person and mandate to your evidence | Person/company, purpose, date/duration if known. “Use $job-conversation-prep for this conversation and give me a quick review first.” | [Prep](../examples/interview/cedarline-prep.md); `workspace/interview/` and role links |

A manifest names the exact source and output files, review state, and actual submission evidence if later supplied. A package is not submitted by being written; a polished story is not rehearsed by being drafted. Word/PDF output uses available document tools; Markdown prep can start without them.

## 5. Capture, review, and activity records

| Capability | Supply / chat prompt | Example and saved result |
| --- | --- | --- |
| Conversation capture preserves learning and supported changes | Notes/transcript and actual completion/date. “Use $job-conversation-capture with these completed-conversation notes and identify follow-ups.” | [Notes](../examples/opportunities/conversations/cedarline.md); `workspace/opportunities/conversations/` plus supported canonical updates |
| Search review chooses the next useful actions | Existing pursuits and current priorities. “Use $job-search-review to give me my most useful next actions and preparation links.” | [Review](../examples/research/search-review.md); canonical decisions updated when supported |
| Personal activity records distinguish completed actions from preparation | Actual dates, actions, and minimal genuine evidence. “Help me record these personally completed search activities, keeping unknowns pending.” | [Log](../examples/profile/activity-log.md); `workspace/profile/activity-log.md` following [the activity procedure](activity-records.md) |

An invitation is not attendance and a promise is not a completed referral. Activity logging is useful without unemployment reporting. If benefits reporting matters, configure and verify your own jurisdiction's current rules separately; this starter makes no eligibility or filing determination.

## 6. Optional tools and recurring work

**Integrations** add your own browser, document tools, scoped correspondence/calendar access, or a separately implemented CRM mirror. Explain [the integration guide](integrations.md) and why the starter's CRM preview is local metadata only. There is no bundled live CRM sync adapter.

Say: “Explain what tools I need for my chosen task and help me configure only those.” Inspect actual availability; do not claim that copying this repo connected anything or ask for secrets in chat.

**Automations** can repeat a successful on-demand task at a user-chosen cadence and timezone. Show [the schedule examples](automations.md), then explain that nothing is active by default. Say: “Help me set up a recurring search review with these times and notification preferences.” Create a schedule only when the user actually requests it and the environment supports scheduling.

**Local utilities** are small terminal programs the agent can run. `demo` reads invented examples, `init` copies blank personal records without overwriting an existing workspace, `check` checks structure, and `crm-preview` prints allowlisted local metadata. They do not browse or contact anyone. Show an actual command result when tools are available; otherwise explain the relevant files.

## First-task handoff

After the overview, ask which useful task to execute or use the one already chosen. Show one actual result saved in the user's workspace, its source evidence, and the exact prompt to repeat it. Keep deferred tour topics and next steps in `workspace/setup.md` for personal onboarding. A user can skip optional topics and still begin their search.
