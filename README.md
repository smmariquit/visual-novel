# visual-novel

Ren'Py 8 visual novel scaffold (1280×720).

## Prerequisites

Install [Ren'Py 8.3+](https://www.renpy.org/latest.html) or point the launcher at this folder.

## Project layout

```
visual-novel/
├── game/
│   ├── script.rpy          # start label → jumps into story
│   ├── characters.rpy      # Character() definitions
│   ├── chapters/           # Story scripts (one file per chapter/act)
│   ├── images/             # Backgrounds, sprites (bg room.png, eileen happy.png, …)
│   ├── audio/              # Music and sound effects
│   ├── gui/                # Generated UI assets (from template)
│   ├── gui.rpy
│   ├── screens.rpy
│   └── options.rpy
└── README.md
```

Ren'Py compiles every `.rpy` file under `game/` (including subfolders), so you can split routes and chapters freely.

## Run locally

**Launcher:** Add `/home/stimmie/dev/personal` as the projects directory, open **visual-novel**, click **Launch Project**.

**CLI** (with SDK on your PATH or adjust the path):

```sh
cd /path/to/renpy-sdk
./renpy.sh /home/stimmie/dev/personal/visual-novel run
```

**Lint:**

```sh
./renpy.sh /home/stimmie/dev/personal/visual-novel lint
```

## Next steps

1. Replace placeholder dialogue in `game/chapters/prologue.rpy`.
2. Add art to `game/images/` (see [Displaying Images](https://www.renpy.org/doc/html/displaying_images.html)).
3. Tune `game/options.rpy` (title, version, `build.name`).
4. Add routes as new files under `game/chapters/` or `game/routes/`.
