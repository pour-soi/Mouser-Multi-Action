import inspect
from pathlib import Path
import unittest

try:
    import main_qml
except Exception:  # pragma: no cover - env without PySide6 / project deps
    main_qml = None


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipIf(main_qml is None, "main_qml / PySide6 not available")
class LinuxInputPolicyTests(unittest.TestCase):
    def test_main_window_lifecycle_does_not_toggle_linux_passthrough(self):
        source = inspect.getsource(main_qml.main)

        self.assertNotIn("set_ui_passthrough", source)
        self.assertNotIn("_sync_linux_ui_passthrough", source)


class LanguageSwitchingQmlPolicyTests(unittest.TestCase):
    def test_settings_language_selector_uses_locale_manager(self):
        source = (ROOT / "ui" / "qml" / "ScrollPage.qml").read_text(encoding="utf-8")

        self.assertIn('s["scroll.language"]', source)
        self.assertIn("model: lm.availableLanguages", source)
        self.assertIn("lm.setLanguage(modelData.code)", source)

    def test_mouse_page_user_visible_debug_strings_use_locale_manager(self):
        source = (ROOT / "ui" / "qml" / "MousePage.qml").read_text(encoding="utf-8")

        self.assertIn('s["mouse.dpi_presets"]', source)
        self.assertIn('s["mouse.press_button_to_cycle"]', source)
        self.assertIn('s["mouse.copy_device_info"]', source)
        self.assertIn('s["mouse.device_info_copied"]', source)
        self.assertIn('s["mouse.no_device_connected"]', source)
        self.assertIn("backend.deviceStatusKind", source)
        self.assertIn('s["mouse.generic_ready"]', source)
        self.assertIn('s["mouse.no_supported_mouse_detected"]', source)
        self.assertNotIn('text: "DPI PRESETS"', source)
        self.assertNotIn('text: "Copy device info"', source)

    def test_key_capture_validation_fallback_uses_locale_manager(self):
        source = (ROOT / "ui" / "qml" / "KeyCaptureDialog.qml").read_text(encoding="utf-8")

        self.assertIn('s["key_capture.error.invalid"]', source)
        self.assertIn('s["key_capture.error.unsupported"]', source)


@unittest.skipIf(main_qml is None, "main_qml / PySide6 not available")
class LanguageSwitchingStartupPolicyTests(unittest.TestCase):
    def test_startup_restores_and_persists_locale_manager_language(self):
        source = inspect.getsource(main_qml.main)

        self.assertIn('initial_lang = cfg_settings.get("language", "en")', source)
        self.assertIn("LocaleManager(language=initial_lang)", source)
        self.assertIn("backend = Backend(engine, root_dir=ROOT, locale_manager=locale_mgr)", source)
        self.assertIn('saved_cfg.setdefault("settings", {})["language"] = locale_mgr.language', source)
        self.assertIn("locale_mgr.languageChanged.connect(_save_language)", source)


if __name__ == "__main__":
    unittest.main()
