# PourInput v1.3.3

Release date: 2026-07-19

Repository: `pour-soi/PourInput`

## Highlights

PourInput v1.3.3 fixes device-specific Back and Forward shortcut editing for the Logitech MX Master 3 on Windows.

## Fixed

- Fixed MX Master 3 Back and Forward shortcut changes not taking effect.
- Added a dedicated Logitech HID++ route for Back CID `0x0053` and Forward CID `0x0056`.
- Fixed a reconnect loop caused by adding and removing side-button HID++ diverts during connection refresh.
- Device-specific mappings now remain separate from Generic Mouse Mode.
- Side-button mappings apply immediately, remain profile-specific, and persist after restart.

## Hardware validation

- Verified with a real Logitech MX Master 3 connected over Bluetooth with Generic Mouse Mode disabled.
- Confirmed Back CID `0x0053` and Forward CID `0x0056` reach their independent selected actions through the dedicated Logitech HID++ route.
- Logitech receiver transport has not yet been validated.
- Logitech Options and Options+ coexistence has not yet been validated.

## Compatibility

- Windows remains the only official public release target.
- Existing profiles, configuration storage, input timing, supported devices, and updater behavior remain compatible.
- Generic Mouse Mode continues to support Middle Button, Side Button 1 (Back), and Side Button 2 (Forward).

## Checksums

The official Windows ZIP SHA-256 is provided in `PourInput-v1.3.3-Windows.zip.sha256` and in `pourinput-v1.3.3-update.json`.
