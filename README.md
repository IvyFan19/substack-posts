# My Substack Workflow

## How it works

1. Write raw ideas in `drafts/`
2. Run `/publish <filename>` in Claude Code
3. Claude polishes it and appends the result to the same draft file
4. Review, edit, tweak until you're happy
5. Tell Claude to publish — it saves to `published/`, updates the index, and posts to Substack

## Folder structure

```
drafts/          Raw ideas and notes
published/       Final articles + index.md
publish.py       Script that posts to Substack
.substack-config.json   Your Substack credentials
.claude/commands/       Claude Code slash commands
```

## Quick reference

| What you want to do | How |
|---|---|
| Write a new idea | Create a file in `drafts/` |
| Polish and publish | `/publish <filename>` in Claude Code |
| See all published articles | Open `published/index.md` |
| Publish manually (skip Claude) | `python3 publish.py published/article.md` |

## Notes

- The cookie in `.substack-config.json` expires periodically. If publishing fails, grab a fresh `substack.sid` from your browser.
- Original drafts are never deleted.
- Everything is in English.
