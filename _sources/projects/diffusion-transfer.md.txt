---
html_theme.sidebar_secondary.remove: true
---

# Guided Transfer for Diffusion LLMs

:::::{div} terminal-window
:::{div} terminal-titlebar
:::
::::{div} terminal-body

`$ cat projects/diffusion-transfer.md`

:::{div} terminal-output

**Guided Transfer for Diffusion LLMs**

![Transfer performance across data regimes](../_static/projects/gtl.png)

Discrete diffusion models are a different way to do language generation — instead of autoregressive left-to-right, they denoise all tokens in parallel. Cool in theory. In practice, you pretrain one on a big corpus and then need it to work on your specific domain. Fine-tuning is expensive and you probably don't have enough domain data.

This project solves the transfer problem without touching the pretrained denoiser. The trick is classifier-guided sampling: train a lightweight guide network on your small target dataset and steer the diffusion process at inference time. The hard part was making this efficient — naive ratio-based guidance is exponential in vocab size. A scheduling trick brings it down to linear.

The result: 7% of parameters trained, works across data regimes, and dominates fine-tuning when target data is scarce. That's the regime that matters in practice — you rarely have millions of domain-specific examples.

:::

`$ cat /etc/motd`

:::{div} terminal-output
*// ...built with Claude Code. based on data, but verify.*
:::

`$ cd ~`

:::{div} terminal-output
[learn more](https://arxiv.org/abs/2512.10877) · [back to home](../index)
:::

::::
:::::
