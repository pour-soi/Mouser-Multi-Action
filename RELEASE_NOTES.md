# PourInput v1.1.0

Release date: 2026-07-08

Repository: `pour-soi/PourInput`

Based on: `TomBadash/Mouser`

Maintainer: `pour-soi`

## Summary

PourInput v1.1.0 introduces the capability-based device support architecture.

The app now keeps the existing device catalog and layouts, but runtime support decisions increasingly use the HID++ features and controls detected from the connected mouse. This makes device handling safer for known devices and less MX Master-specific for unknown Logitech devices.

## Highlights

- Added a `DeviceCapabilities` model for runtime device features.
- Added safer generic fallbacks for unknown or generic Logitech devices.
- Battery support now consults detected battery capability where safe.
- DPI support now consults adjustable-DPI capability where safe.
- SmartShift support now consults SmartShift capability where safe.
- Gesture support now consults gesture-button capability where safe.
- Button support now consults capability-derived reprogrammable buttons where safe.
- Existing catalog-based layouts and known-device defaults remain in place.

## Device Support Notes

- MX Master 3 remains the tested device.
- This release does not add confirmed support for untested devices.
- Experimental or potentially compatible devices, such as MX Master 3S, M720 Triathlon, MX Anywhere series, and other Logitech HID++ devices, may work only when they expose matching HID++ capabilities.
- If capability information is missing, uncertain, or runtime discovery is incomplete, PourInput preserves conservative fallback behavior instead of hiding or enabling features aggressively.

## Compatibility

No behavior change is intended for MX Master 3, MX Master 3S, or MX Master 4 catalog paths.

Unknown Logitech devices should now fall back to generic buttons and generic behavior more safely instead of inheriting MX Master-specific assumptions.

## Validation

The capability refactor was covered by focused tests for:

- Known MX Master device capability exposure.
- Generic fallback devices avoiding MX Master-specific assumptions.
- Battery, DPI, SmartShift, gesture, and button behavior preserving existing fallback paths.
- Existing multi-action behavior.

## Known Limitations

- Windows remains the only official release target.
- Device support still depends on firmware, operating system exposure, and HID++ features.
- Some devices may be detected but expose only partial controls.
- Double Click is planned but not implemented yet.
- Long Press timeout defaults to 300 ms and is not editable in the UI yet.
- Macro support and sequential actions are not implemented yet.
