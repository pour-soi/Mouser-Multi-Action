# Mouser Multi-Action

Mouser Multi-Action is a customized open-source fork of [TomBadash/Mouser](https://github.com/TomBadash/Mouser). It extends the original Mouser project with a generic Multi-Action Button framework so supported mouse buttons can have separate Click and Long Press actions.

Repository name: `Mouser-Multi-Action`

Maintainer: `pour-soi`

Current release: v0.1.0

## Features

- Generic Multi-Action Button framework
- One reusable dispatcher for Click and Long Press behavior
- Default long-press threshold: 300 ms
- Mode Shift Click and Long Press mappings
- Back Button Click and Long Press mappings
- Forward Button Click and Long Press mappings
- Config migration for existing Mouser Multi-Action profiles
- UI fields for Click Action and Long Press Action
- HID++ Mode Shift diversion synchronization inherited from the customized Mouser Multi-Action work in this fork

## Screenshots

Screenshots will be added in a future release.

Suggested placeholders:

- Mouse page with Mode Shift selected
- Back Button with Click and Long Press configured
- Forward Button with Click and Long Press configured
- About dialog showing version and commit

## Installation

1. Download `Mouser-Multi-Action-v0.1.0-Windows.zip` from the release.
2. Extract the zip.
3. Open `Mouser-Multi-Action-v0.1.0/Mouser.exe`.
4. Configure Click Action and Long Press Action for Mode Shift, Back, or Forward.

On Windows, if another Mouser Multi-Action build is already running, quit it from the tray before launching this build.

## How To Use

Open the Mouse page and select a supported button:

- Mode Shift
- Back Button
- Forward Button

Each supported button shows:

- Click Action
- Long Press Action

Examples:

- Back: Click -> Browser Back, Long Press -> Copy
- Forward: Click -> Browser Forward, Long Press -> Paste
- Mode Shift: Click -> Screenshot Region -> Clipboard, Long Press -> Switch Scroll Mode

A press shorter than 300 ms dispatches the Click Action. A press held for at least 300 ms dispatches the Long Press Action when released.

If a button has no Long Press Action configured, Mouser Multi-Action keeps the original behavior for that button.

## How To Build

Requirements:

- Windows
- Python 3.12
- Project dependencies from `requirements.txt`
- PyInstaller

From the repository root:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller Mouser.spec --noconfirm
```

The raw build output is written to:

```text
dist/Mouser/
```

## How To Package

Use the release script:

```powershell
.\scripts\create_release.ps1 -Version v0.1.0
```

If no version is specified, the script reads the latest versioned Windows zip in `release/` and increments the patch version.

The release output is:

```text
release/
    Mouser-Multi-Action-v0.1.0-Windows.zip
    RELEASE_NOTES-v0.1.0.md
    CHANGELOG.md
```

The zip contains:

```text
Mouser-Multi-Action-v0.1.0/
    Mouser.exe
    LICENSE
    README.md
    CHANGELOG.md
    RELEASE_NOTES.md
    all required runtime files
```

The script removes only temporary build output before packaging. It does not remove `.git`, source code, release history, README, changelog, settings, logs, or versioned release zips.

## GitHub Publishing

Publish this project as:

```text
pour-soi/Mouser-Multi-Action
```

Suggested release flow:

1. Commit the source changes.
2. Create and push the tag `v0.1.0`.
3. Create a GitHub Release named `Mouser Multi-Action v0.1.0`.
4. Upload `release/Mouser-Multi-Action-v0.1.0-Windows.zip`.
5. Use `release/RELEASE_NOTES-v0.1.0.md` as the release body.

## Versioning

This project uses Semantic Versioning:

```text
Major.Minor.Patch
```

Examples:

- v0.1.0
- v0.1.1
- v0.2.0
- v1.0.0

If no version is provided to the release script, the patch version is incremented automatically.

## Roadmap

### v0.2.0

- Double Click support
- Custom long-press timeout

### v0.3.0

- Per-button timeout
- Export/Import configuration

### v0.4.0

- Macro support
- Sequential actions

### v1.0.0

- Stable release

## Contributing

Future buttons should be added through the generic multi-action configuration instead of adding new button-specific timer logic.

To add another multi-action button:

1. Add the button key to `MULTI_ACTION_BUTTONS` in `core/config.py`.
2. Ensure the button has down/up events in `BUTTON_TO_EVENTS`.
3. Add a default `<button>_long` mapping.
4. Confirm the backend exposes the button through `supportsMultiAction`.
5. Add focused engine and UI/backend tests.

## Original Project

This project is based on:

- [TomBadash/Mouser](https://github.com/TomBadash/Mouser)

Maintainer:

- `pour-soi`

## License

This project keeps the original Mouser license. See [LICENSE](LICENSE).
