# Module 12 — Trainer notes

## Suggested timing (90–120 minutes)

- 20 min: reconstruct the capstone evidence chain.
- 20 min: delegate-versus-human classification.
- 20 min: proportional safeguards exercise.
- 20–30 min: agree on team practices.
- 10–20 min: final presentations and course close.

## Preparation

1. Ask each group to bring its Module 11 evidence, including limitations and pending work. Do not require a merged/deployed feature if permissions or environment availability prevented it.
2. Print or distribute `capstone-assessment-checklist.md`; have participants complete it individually before group discussion.
3. Prepare one example of helpful Copilot output and one example that required correction from course artifacts or participant runs. Remove sensitive details.
4. Decide how the group will record its small practice set (course worksheet, team notes, or existing process documentation). This module does not require a repository write.

## Facilitation guidance

- Require evidence for claims. Ask to see the exact story, diff, test, CI run, review, or runtime result.
- Keep the exercise balanced: Copilot can materially help with search, drafting, tests, implementation, and log analysis, while people own product approval, security judgment, acceptance of risk, review/merge, and release authorization.
- Avoid turning the lesson into either “automate everything” or “never trust AI.” Ask what task, context, risk, and evidence make assistance appropriate.
- Distinguish a configured tool from a connected/authorized tool, and a successful tool call from a correct outcome.
- Discuss proportionality with reversibility and impact: a small documentation change does not need a deployment process; a security-sensitive change deserves targeted review and stronger evidence.
- Keep the final team practice set short. Each item should name a trigger, owner, and review signal; avoid adopting every course safeguard for every change.
- Do not add Skills, Hooks, MCP servers, CI workflows, or policy changes in the wrap-up. Identify future improvements as proposals for the team's normal change process.

## Completion evidence

Each participant completes the checklist, presents one human judgment call and one Copilot contribution, and contributes to a short team practice set that the group can trial and review.
