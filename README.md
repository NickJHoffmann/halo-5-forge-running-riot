## Halo 5 Forge - Running Riot Achievement

This is a python script to automate the process of grinding out the Halo 5 Forge PC "Running Riot" achievement.
Script adapted from the [TrueAchievements Guide](https://www.trueachievements.com/a221259/running-riot-achievement).

You must run this directly in Windows, it will not work from WSL unless you do a bunch of work to adapt it that I did not want to bother with.

### Prerequisites
- Make sure that you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- I also recommend [pyenv-win](https://github.com/pyenv-win/pyenv-win)

### Usage
- Open Halo 5 Forge PC
- Go to Multiplayer -> Custom Game
- Select the correct map and game mode
- Make sure the "Privacy" menu option is highlighted (do not actually click it)
- Run the script with

```powershell
uv sync
uv run python main.py --help
```

- Switch back to the Halo 5 window so that it is the active window before the script execution resumes
