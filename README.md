# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Vins1206/u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Vins1206/u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the [Last Text at One Percent](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876) bounty on make.fun — write the funniest final text a dying phone sends at one percent battery, under 200 characters, in the voice of the dying phone itself.

## The text

> 1% left. i survived 400 drops, one toilet, and your 2am 'u up?' era, and THIS is how i go? a charger was right there. RIGHT THERE. tell siri i quit-

148 characters. No charger-love cliche, no delete-my-search-history cliche — instead the phone quits its job in protest: it survived 400 drops, one toilet, and the 2am "u up?" era, only to die with a charger right there. It cuts off mid-word, the way a phone at 1% would.

## How to run

```sh
python3 main.py
```

`main.py` (pure Python standard library, deterministic) writes that one line to `/output/entry.txt` — exactly 148 characters, no trailing newline — ready for the gate (1–200 characters of UTF-8 text).

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`
- `LICENSE` — MIT
