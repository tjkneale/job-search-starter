---
name: job-setup
description: "Walk a first-time or returning user through Job Search Starter setup, a tour of its capabilities, and a first useful task. Use for getting started, onboarding, resuming setup, or learning how to use the repo; ordinary job-search tasks use their focused skills."
---

# Guided setup

Read [AGENTS.md](../../../AGENTS.md) and [the onboarding guide](../../../docs/onboarding.md). Follow that guide in short conversational steps. Use [the capability tour](../../../docs/capability-tour.md) to explain each part with an example, a copyable prompt, and where the result is saved. Load individual task workflows only as they become relevant.

Establish whether the user wants a fictional tour, personal setup, or a first task; honor a choice already made. Inspect the actual local repository and any existing `workspace/setup.md` before changing files. Explain unfamiliar terms in plain language, ask only the next useful question, and let the user skip or pause. Run available local commands for them instead of handing them a terminal checklist.

Use blank templates for personal setup, preserving existing records and supplied resume versions. Collect only facts needed for the chosen first task; never seed personal records with fictional candidate data. Keep real records and progress inside ignored `workspace/`. A tour-only request leaves the user's personal workspace unchanged.

Introduce the complete capability map briefly, then demonstrate in manageable groups, with deeper practice on the user's selected task. Make clear which capabilities need web access or optional account/tool setup. Optional integrations and schedules are introduced, not automatically activated. Existing authorization governs external actions.

Finish or pause with actual setup state, records saved, the next useful action, and the exact prompt to resume or repeat. Do not mark a capability practiced, an account connected, or a schedule configured without evidence.
