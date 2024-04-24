# SNU Logic Design 2023

This repository provides some reference codes & tests for the final ldlab project.

## Testing for Final Project
Check [test](./test).


## Installing ISE 14.7 on a Silicon Mac
Check [this](./docs/ise_on_mac.md) for detailed instructions. It won't be that hard to follow.

## Installing Vivado on a Silicon Mac
Since the Xilinx ISE is a deprecated solution succeeded by Xilinx Vivado, you might prefer installing it (and I also advise you to do so). If so, there are several tools available for easy use. See [link](https://github.com/ichi4096/vivado-on-silicon-mac) for steps.

I tried it, and it works well. But there are some precautions

1. Use Vivado 2022.2 or earlier (not 2023)
2. If you're using macOS 14 (Sonoma), disable the use of Rosetta2 in Docker, while installing. You may enable it after installation, as it yields significant performance boost.
3. It takes 100+ GBs for install, and 60+ GBs afterwards. Make sure you have enough storage for this.


the content of the documents were last updated at Nov 2023.
