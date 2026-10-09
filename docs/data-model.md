# Records and evidence

The same structure is used under `workspace/` for personal work and under `examples/` for invented demonstrations. The root instructions and workflows stay generic.

| Record | Authority |
| --- | --- |
| `profile/candidate.md` and `profile/evidence.md` | Candidate facts, approved wording, evidence, and disclosure choices |
| `strategy/criteria.md` | Candidate's search gates and preferences |
| `opportunities/roles/*.md` | Canonical role identity, decision, pipeline stage, availability, and next action |
| `opportunities/company-list.csv` | Company list, candidate Advocacy/Motivation choices, potential paths, Posting score |
| `research/company-status.json` | Separate networking and Posting research checkpoints, dates, and evidence references |
| `opportunities/companies/`, `research/` | Diligence, sources, observations, and unresolved questions |
| `interview/` and `resumes/applications/` | Preparation, story versions, application manifests, exact outputs |
| `profile/activity-log.md` | Actual personal activities and completion evidence; eligibility is a separate question |

## Role metadata

Keep metadata bullets before the first `##` heading; use the [role template](../templates/role-brief.md). Required fields are `Company`, `Role`, `Decision`, `Pipeline`, and `Verification status`. Use a stable employer/requisition identity to avoid duplicates. Optional fields include official URL, requisition, location, posted compensation, last verified date, next action, and `CRM board lock`.

`Decision` is `Pursue`, `Watch`, or `Exclude`. It expresses candidate interest or an explicit criteria-based exclusion. An untriaged lead starts `Watch / Research`. Availability is `Active`, `Closed`, `Unverified`, or `Fictional` for examples only.

| Pipeline | Meaning |
| --- | --- |
| Research, Networking planning, Preparing | Work before external contact |
| Reached out, Connected, Informational interview | Actual contact occurred; application not yet submitted |
| Applied | Application submission confirmed |
| Interviewing | Interview scheduled or formal employer interview process underway |
| Offer | Formal offer received and under consideration |
| Won't apply | Candidate declined or the unapplied opening is unavailable |
| Closed Lost | A submitted application was rejected |
| Accepted | Offer accepted |

Interest can remain `Pursue` after rejection while stage becomes `Closed Lost`. A closed unapplied posting uses `Won't apply`, with prior notes retained. Preparation or an employer's announced general recruiting process never proves attendance, submission, or selection.

## Company list

LAMP is a company prioritization convention: List, Advocacy, Motivation, Posting. The documentation here describes this starter's use, inspired by *The 2-Hour Job Search*, rather than reproducing the book.

The CSV headers are `List`, `Advocacy`, `Networking path 1`, `Networking path 2`, `Motivation`, `Posting`. Add consecutively numbered path columns between Advocacy and Motivation as needed. Discover columns by their names; preserve existing entries and row order. CSV links are plain text. Moving to an Excel workbook requires preserving native links, formulas, and formatting with appropriate spreadsheet tools; these scripts read CSV only.

Advocacy is blank, `Yes`, or `No` and belongs to the candidate. Motivation is blank or 1–3 with 3 highest, also candidate controlled. Posting is blank or 1–3: 3 for a relevant live official opening, 2 for other live openings without a target confirmed, 1 for a verified empty official board. An inaccessible board leaves Posting unresolved, not 1.

`company-status.json` uses normalized company names as keys (casefolded, whitespace collapsed). Each entry has separate `networking` and `posting` checkpoints. Allowed statuses are `untracked`, `partial`, `researched`, `no_paths_found`, `existing_contacts_only`, or `deferred`. A checkpoint with research needs an observation date and a relative evidence path under the same data root. Scores and occupied cells do not prove completion. The [fictional registry](../examples/research/company-status.json) illustrates the format.
