**Agents Do Things, Skills Teach Things**

---

I kept mixing up Agents and Skills in Claude Code. They both looked like prompts to me — you write some instructions, Claude does what you say. It took a while before I figured out they're actually doing very different things.

## What an Agent Actually Is

Here's the cleanest definition I've found:

**Agent = Custom System Prompt + Fresh Context Window + Tool Access**

That's it. An Agent is a pre-configured instance of Claude with:
1. A system prompt that defines its behavior and expertise
2. A brand new context window (no memory from your previous conversations)
3. Access to whichever tools you grant it

The critical insight: **Every time you invoke an Agent, it starts with a clean slate.**

This is a feature, not a bug. If you're building an Agent that reviews code for security issues, you don't want it contaminated by memories of your last chat about fixing bugs. You want a focused, specialized instance that does one thing well.

Think of an Agent like spinning up a specialist consultant. You brief them once (via the system prompt), they look at the specific problem (via the fresh context), they use their tools, and they deliver. Next time you call them, they don't remember the last engagement.

## What a Skill Actually Is

Skills are different. Completely different.

**Skills = Best Practice Documentation that Claude Auto-Reads**

A Skill isn't an instance of Claude. It's a reference document that Claude can pull from when it needs domain-specific knowledge.

The best analogy I've heard compares it to software documentation:

- **Skills** = Official API documentation (React docs, MDN Web Docs, Python stdlib reference)
- **Agent** = Senior developer who's internalized the docs + understands your specific codebase
- **Claude (base)** = Junior developer who looks up the docs when they need help

Let's say you're working with React. You could create a Skill that contains:
- useState hook best practices
- Common pitfalls with useEffect
- Your team's component architecture patterns

When Claude encounters a React question, it automatically reads the Skill and applies that knowledge to your specific situation. It's not a separate instance — it's augmented context for the main Claude instance you're talking to.

## Why This Distinction Matters

Once I understood this, I stopped making two specific mistakes:

**Mistake 1: Trying to make Agents remember things**

I kept wondering why my Agent wasn't learning from previous interactions. Now I know: it's not supposed to. If you need persistent memory, you either need to re-pass context each time or you're actually looking for a Skill, not an Agent.

**Mistake 2: Treating Skills like task-runners**

I tried to create a "Skill" that would automatically run tests. That's not what Skills do. Skills provide knowledge. Agents provide behavior. If you want something to actively do things, you want an Agent with appropriate tool access.


## What This Means for How You Build

When I sit down to extend Claude Code now, I ask myself:

1. **Am I trying to teach Claude something?** → Skill
2. **Am I trying to create a specialized behavior?** → Agent

Or more practically:

- "I want Claude to know our API patterns" → Skill
- "I want a focused instance that only reviews API code" → Agent

The tools aren't interchangeable. They solve different problems.

And once you get that, both become way more useful.

