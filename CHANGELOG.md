# Changelog

All notable changes to Mouser Multi-Action are documented here.

This project uses Semantic Versioning.

## v0.1.0 - 2026-07-06

### Added

- Added generic Multi-Action Button framework.
- Added Click and Long Press support.
- Added Mode Shift Click and Long Press support.
- Added Back Button Click and Long Press support.
- Added Forward Button Click and Long Press support.
- Added generic dispatcher shared by supported multi-action buttons.
- Added config migration for long-press mappings and default 300 ms threshold.
- Added UI sections for Click Action and Long Press Action.
- Added versioned Windows release packaging.
- Added release notes and open-source release documentation.
- Standardized project metadata as Mouser Multi-Action.
- Set release repository metadata to pour-soi/Mouser-Multi-Action.

### Fixed

- Improved HID diversion synchronization for Mode Shift remapping.
- Ensured Mode Shift diversion also applies when only the long-press slot is configured.
- Replaced placeholder maintainer metadata with pour-soi.

### Known Limitations

- Double Click is not implemented yet.
- Long-press timeout is global and not editable in the UI yet.
- Per-button timeout is not implemented yet.
- Macro and sequential actions are not implemented yet.
