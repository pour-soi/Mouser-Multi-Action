# PourInput v1.3.2

Release date: 2026-07-17

Repository: `pour-soi/PourInput`

## Highlights

PourInput v1.3.2 is a maintenance release focused on reliable Windows side-button mapping, startup and tray stability, and clearer multilingual presentation.

## Fixed

- MX Master 3 Back and Forward mappings now use the active Generic Mouse Mode route selected in the UI.
- The application starts correctly with the required Qt slot integration.
- Reopening the main window from the system tray no longer emits a QML focus error.
- Windows side-button handling is more robust during mapping changes, reconnects, queue pressure, and shutdown.
- Locale-aware font fallback and translated labels are more consistent across the interface.

## Hardware validation

- Verified with a real Logitech MX Master 3 connected over Bluetooth.
- Logitech receiver transport has not yet been validated.
- Logitech Options and Options+ coexistence has not yet been validated.

## Compatibility

- Windows remains the only official public release target.
- Existing profiles, mappings, configuration storage, input timing, supported devices, and updater behavior remain compatible.
- Generic Mouse Mode continues to support Middle Button, Side Button 1 (Back), and Side Button 2 (Forward).

## Checksums

The official Windows ZIP SHA-256 is provided in `PourInput-v1.3.2-Windows.zip.sha256` and in `pourinput-v1.3.2-update.json`.
