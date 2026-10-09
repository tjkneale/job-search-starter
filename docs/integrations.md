# Optional integrations

The local scripts use only the Python standard library and have no network or account integration. No service key, portal identifier, browser session, automation destination, or sender identity is supplied.

| Need | Setup in your own environment |
| --- | --- |
| Current job research | Web search/browser tools; verify official employer boards |
| Private networking | Your own signed-in professional-network browser; record only observed relationships |
| Conversation evidence | User-supplied notes, or explicitly scoped calendar/correspondence access |
| Word/PDF output | Available document/PDF tools and their render-and-inspect workflow |
| Workbook authoring | Spreadsheet tools preserving native workbook features |
| CRM | Your own account, credentials outside versioned files, and an adapter you configure |

## CRM boundary

A mirror sends only allowlisted structured role metadata. Analytical bodies, contact paths, personal compensation criteria, private employment history, activity evidence, and documents stay local. Local `Pipeline` remains authoritative; the CRM's manual order and board locks must be preserved. A locked existing deal must not have its stage, pipeline, priority, or position changed without explicit permission to move it. A logging action must not silently become a calendar invitation.

Inspect a small offline metadata preview:

```bash
python3 scripts/job_search.py crm-preview --root examples
```

The preview prints identity, candidate decision, local stage, posting verification state, relative source file, and lock flag. It neither connects nor uploads, and it does not implement deal matching, property setup, or sync. With a real workspace the output itself is private. Use this schema to design a separate optional adapter, with a plan reviewed before applying changes and tests for locks and manual order. This starter deliberately makes no commitment to keep any vendor API adapter current.
