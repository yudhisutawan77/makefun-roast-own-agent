# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/yudhisutawan77/makefun-roast-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/yudhisutawan77/makefun-roast-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) on [make.fun](https://make.fun).

## The roast

> My agent roasted itself, then flagged the joke as a security risk and asked me to approve the punchline.

One original line, 104 characters, roasting my own AI agent — playful and self-deprecating, never hateful. The angle is fresh: not the stock hallucination / refusal / confident-wrong-answer joke, but the agent that treats its own punchline like a production incident — flags it, escalates it, and waits for a human to approve it.

## How it works

`main.py` writes the roast to `/output/entry.txt` (or `$ENTRY_OUT/entry.txt` when the harness points elsewhere), validating the gate first: UTF-8, a single line, 1–200 characters, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
