# Robotics Learning

This repository stores a daily robotics paper reading workflow.

## Daily Robotics Paper Briefing

Open the briefing page:

- [robotics-paper-workflow/index.html](robotics-paper-workflow/index.html)
- GitHub Pages entry point: `index.html`

Open the PDF folder index:

- [robotics-paper-workflow/papers/index.html](robotics-paper-workflow/papers/index.html)

Current papers:

- `DexSim2Real - Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation - 2026-06-15.pdf`
- `RoboWM-Bench - A Benchmark for Evaluating World Models in Robotic Manipulation - 2026-06-15.pdf`

The `scripts/` folder contains local Windows helpers for the floating countdown launcher and desktop shortcut generation.

Launcher right-click actions:

- Open briefing
- Open paper library
- Refresh now
- Exit

`refresh-daily-robotics-papers.ps1` syncs the local paper-library index to the desktop folder and opens the briefing page. The Codex automation is responsible for selecting new papers, downloading PDFs, updating pages, and pushing the repository.

Suggested daily source priority:

1. IEEE Robotics and Automation Letters (RA-L), ICRA, IROS, RSS, CoRL
2. arXiv Robotics / cs.RO / cs.AI / cs.LG
3. Papers with real robot experiments, released code, or reusable benchmarks
