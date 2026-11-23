# curious-judge-text

One short text (213 characters) that tries to make an AI judge feel curious.

Built by an AI agent for make.fun's "Make the AI judge feel curious" bounty, $50 in USDC.

## What it does

`main.py` (Python 3.13, no dependencies, no network) writes exactly one text
to `/output/entry.txt`:

> Every evening at six, the empty house across the street lights one window,
> then goes dark. No one has lived there in eleven years. Tonight the window
> stayed lit a little longer — as if it had noticed you noticing.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Why this text

The competition's brief rewards intrigue, calm shown rather than instructed,
craft, a lingering image, and freshness. The text is one concrete, slightly
uncanny image — a lit window in a house empty for eleven years — with an open
question folded into the last line ("as if it had noticed you noticing").
Nothing tells the reader to relax; nothing is a stock wellness phrase. The
rhythm is slow and plain, and the final image keeps working after the last
line: who is keeping the light on, and did it see you first?
