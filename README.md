# Elbi Dating Sim

A short Ren'Py dating sim set at **UP Los Baños** (Elbi). Romance four fictional classmates over Welcome Week, pick afternoon hangouts, build affection, get an ending on Palma Bridge.

**Art policy:** campus backgrounds only, sourced from [Wikimedia Commons](game/images/ATTRIBUTION.md). No AI-generated images. No character sprites, story is told with dialogue over real campus photos.

## Prerequisites

Install [Ren'Py 8.3+](https://www.renpy.org/latest.html).

## Run locally

### Ren'Py Launcher

1. Clone or download this repo anywhere on your machine.
2. Open the Ren'Py launcher.
3. Set **Projects Directory** to the parent folder that contains this project.
4. Select **visual-novel** (folder name) or **Elbi Dating Sim** (display name) → **Launch Project**.

### Command line

**Linux / macOS:**

```sh
cd /path/to/renpy-sdk
./renpy.sh /path/to/visual-novel run
```

**Windows:**

```bat
cd C:\path\to\renpy-sdk
renpy.exe C:\path\to\visual-novel run
```

## Project layout

```
game/
├── script.rpy # Title + name entry
├── characters.rpy # Rafa, Jules, Sam, Thea
├── systems.rpy # Affection / day counter
├── chapters/
│ ├── prologue.rpy # Arrival + meet cast
│ ├── week_one.rpy # 3-day hangout loop
│ └── endings.rpy # Route endings
├── images/bg/ # UPLB photos (Wikimedia)
└── images/ATTRIBUTION.md # Licenses + credits
```

## Gameplay

1. Choose your major flavor in the prologue (flavor text only).
2. Spend **three afternoons** at campus locations, each visit bumps affection.
3. On **day 3**, Palma Bridge confession scene routes to the character with highest affection (need 5+ points).

## Credits

Background photos: Wikimedia Commons contributors, see [ATTRIBUTION.md](game/images/ATTRIBUTION.md).
