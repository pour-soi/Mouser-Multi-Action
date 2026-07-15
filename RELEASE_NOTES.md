# PourInput v1.3.0 — Visual System and Architecture

Release date: TBD

Repository: `pour-soi/PourInput`

Maintainer: `pour-soi`

## English

PourInput v1.3.0 gives the application and project a cohesive visual identity while keeping its input, remapping, device, and profile behavior unchanged.

### Highlights

- A redesigned desktop interface with a consistent PourInput visual system, refined navigation, spacing, typography, controls, profiles, settings, and light/dark themes.
- Finalized PourInput branding across the Windows executable, macOS and Linux application assets, tray presentation, About view, and repository homepage.
- A complete design-system documentation set covering shared tokens, components, brand assets, screenshots, and visual release checks.
- A complete architecture documentation set covering runtime ownership, event flow, mappings, profiles, settings, state management, QML structure, and project layout.
- Simplified, aligned English and Simplified Chinese README pages with a clearer Windows download path.

This release does not intentionally change mouse input handling, mappings, action execution, device capabilities, profile behavior, updater behavior, or supported platforms.

## 简体中文

PourInput v1.3.0 为应用程序和项目建立了统一的视觉识别，同时保持输入、重映射、设备与配置文件行为不变。

### 主要内容

- 重新设计桌面界面，统一 PourInput 视觉系统，并优化导航、间距、字体、控件、配置文件、设置以及明暗主题。
- 完成 Windows 可执行文件、macOS 与 Linux 应用资源、托盘、关于页面和仓库主页中的 PourInput 品牌统一。
- 新增完整的设计系统文档，包括共享设计变量、组件、品牌资源、截图规范和视觉发布检查表。
- 新增完整的架构文档，包括运行时职责、事件流、映射、配置文件、设置、状态管理、QML 结构和项目目录。
- 简化并对齐英文和简体中文 README，提供更清晰的 Windows 下载路径。

此版本不会有意更改鼠标输入处理、映射、动作执行、设备能力、配置文件行为、更新行为或支持的平台。

## Release Policy

Windows is the only official public release target for v1.3.0.

The public GitHub Release should contain only:

- `PourInput-v1.3.0-Windows.zip`
- `PourInput-v1.3.0-Windows.zip.sha256`
- `pourinput-v1.3.0-update.json`

macOS and Linux CI/build validation may remain, but public macOS and Linux packages are not part of the official v1.3.0 release.

## Validation

The release candidate is expected to pass:

- The full automated test suite.
- Windows PyInstaller packaging and executable startup checks.
- SHA-256 verification of the uploaded Windows archive.
- Version and build-metadata checks inside the packaged application.
- Documentation-link and release-asset audits.
- The PourInput visual release checklist against the candidate build.

## Known Limitations

- Windows remains the only official release target.
- Generic Mouse Mode is Windows-only and supports Middle Button, Side Button 1, and Side Button 2.
- Generic Mouse Mode cannot currently distinguish multiple standard mice by physical source device.
- Device support depends on firmware, operating-system exposure, and HID++ features.
- Long-press timeout is fixed at 300 ms; double-click, macros, and sequential actions are not implemented.
