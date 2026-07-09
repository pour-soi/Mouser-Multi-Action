import unittest

from ui.locale_manager import AVAILABLE_LANGUAGES, LocaleManager, _TRANSLATIONS


class LocaleManagerTranslationTests(unittest.TestCase):
    def test_default_language_is_english(self):
        manager = LocaleManager()

        self.assertEqual(manager.language, "en")
        self.assertEqual(manager.tr("scroll.language"), "Language / \u8bed\u8a00")

    def test_available_languages_are_english_and_simplified_chinese(self):
        self.assertEqual(
            AVAILABLE_LANGUAGES,
            [
                {"code": "en", "name": "English"},
                {"code": "zh_CN", "name": "\u7b80\u4f53\u4e2d\u6587"},
            ],
        )

    def test_saved_simplified_chinese_language_is_restored(self):
        manager = LocaleManager("zh_CN")

        self.assertEqual(manager.language, "zh_CN")
        self.assertEqual(manager.tr("scroll.title"), "\u901a\u7528\u8bbe\u7f6e")

    def test_unsupported_saved_language_falls_back_to_english(self):
        manager = LocaleManager("zh_TW")

        self.assertEqual(manager.language, "en")
        self.assertEqual(manager.tr("scroll.title"), "General Settings")

    def test_switching_to_chinese_updates_display_labels(self):
        manager = LocaleManager()

        manager.setLanguage("zh_CN")

        self.assertEqual(manager.language, "zh_CN")
        self.assertEqual(manager.tr("mouse.generic_mouse_mode"), "\u901a\u7528\u9f20\u6807\u6a21\u5f0f")
        self.assertEqual(manager.tr("mouse.generic_ready"), "\u901a\u7528\u9f20\u6807\u6a21\u5f0f\u5df2\u5c31\u7eea")
        self.assertEqual(manager.tr("mouse.no_supported_mouse_detected"), "\u672a\u68c0\u6d4b\u5230\u53d7\u652f\u6301\u7684\u9f20\u6807")
        self.assertEqual(manager.tr("mouse.click_action"), "\u5355\u51fb\u64cd\u4f5c")
        self.assertEqual(manager.tr("mouse.long_press_action"), "\u957f\u6309\u64cd\u4f5c")

    def test_switching_back_to_english_restores_english_labels(self):
        manager = LocaleManager("zh_CN")

        manager.setLanguage("en")

        self.assertEqual(manager.language, "en")
        self.assertEqual(manager.tr("mouse.generic_mouse_mode"), "Generic Mouse Mode")
        self.assertEqual(manager.tr("mouse.generic_ready"), "Generic Mouse Mode Ready")
        self.assertEqual(manager.tr("mouse.no_supported_mouse_detected"), "No supported mouse detected")
        self.assertEqual(manager.tr("mouse.click_action"), "Click Action")
        self.assertEqual(manager.tr("mouse.long_press_action"), "Long Press Action")

    def test_generic_mouse_button_names_translate(self):
        manager = LocaleManager("zh_CN")

        self.assertEqual(manager.trButton("Middle Button"), "\u4e2d\u952e")
        self.assertEqual(manager.trButton("Side Button 1"), "\u4fa7\u952e 1")
        self.assertEqual(manager.trButton("Side Button 2"), "\u4fa7\u952e 2")

    def test_action_display_names_translate_without_changing_inputs(self):
        manager = LocaleManager("zh_CN")
        cases = {
            "Copy (Ctrl+C)": "\u590d\u5236 (Ctrl+C)",
            "Paste (Ctrl+V)": "\u7c98\u8d34 (Ctrl+V)",
            "Volume Mute": "\u9759\u97f3",
            "Alt + Tab (Switch Windows)": "Alt + Tab\uff08\u5207\u6362\u7a97\u53e3\uff09",
            "Screenshot Region \u2192 Clipboard": "\u533a\u57df\u622a\u56fe \u2192 \u526a\u8d34\u677f",
            "Switch Scroll Mode (Ratchet / Free Spin)": "\u5207\u6362\u6eda\u8f6e\u6a21\u5f0f\uff08\u68d8\u8f6e / \u98de\u8f6e\uff09",
        }

        for english, translated in cases.items():
            with self.subTest(english=english):
                self.assertEqual(manager.trAction(english), translated)

    def test_missing_translations_fall_back_safely(self):
        manager = LocaleManager("zh_CN")

        self.assertEqual(manager.tr("missing.key"), "missing.key")
        self.assertEqual(manager.trButton("Unknown Button"), "Unknown Button")
        self.assertEqual(manager.trAction("Custom App Action"), "Custom App Action")

    def test_key_capture_error_messages_exist_in_all_locales(self):
        required = {
            "key_capture.error.unsupported_key",
            "key_capture.error.unknown_key",
            "key_capture.error.duplicate_key",
            "key_capture.error.multiple_main_keys",
            "key_capture.error.missing_main_key",
            "key_capture.error.empty_segment",
            "key_capture.error.unsupported",
            "key_capture.error.invalid",
        }

        for locale, strings in _TRANSLATIONS.items():
            with self.subTest(locale=locale):
                self.assertTrue(required.issubset(strings))
                for key in required:
                    self.assertTrue(strings[key].strip())

    def test_update_install_messages_exist_in_all_locales(self):
        required = {
            "scroll.update_idle",
            "scroll.update_available",
            "scroll.update_checking",
            "scroll.update_downloading",
            "scroll.update_verifying",
            "scroll.update_ready",
            "scroll.update_installing",
            "scroll.update_installed",
            "scroll.update_installed_version",
            "scroll.update_cancelled",
            "scroll.update_manual",
            "scroll.update_manual_windows",
            "scroll.update_manual_macos",
            "scroll.update_manual_linux",
            "scroll.update_no_asset",
            "scroll.update_error",
            "scroll.update_error_check_first",
            "scroll.update_error_network_error",
            "scroll.update_error_metadata_missing",
            "scroll.update_error_metadata_invalid",
            "scroll.update_error_permission_denied",
            "scroll.update_error_file_error",
            "scroll.update_error_install_failed",
            "scroll.update_error_sha256_mismatch",
            "scroll.update_error_size_mismatch",
            "scroll.update_error_expired_metadata",
            "scroll.update_error_older_build",
            "scroll.update_check",
            "scroll.update_download",
            "scroll.update_cancel",
            "scroll.update_verify",
            "scroll.update_install",
            "scroll.update_open_release",
        }

        for locale, strings in _TRANSLATIONS.items():
            with self.subTest(locale=locale):
                self.assertTrue(required.issubset(strings))
                for key in required:
                    self.assertTrue(strings[key].strip())


class AccessibilityLocaleTests(unittest.TestCase):
    """The QML accessibility labels added in this batch reference these
    keys. Missing them in a non-English locale silently regresses to a
    KeyError-as-empty-string in the QML lookup ``s[...]``, which leaves
    screen readers reading nothing for an interactive control.
    """

    REQUIRED_KEYS = frozenset({
        "dialog.close",
        "scroll.ignore_trackpad",
        "scroll.ignore_trackpad_desc",
        "scroll.smart_shift",
    })
    ENGLISH_VALUES = frozenset({
        "Close",
        "Ignore trackpad",
        "Only respond to mouse events, not trackpad or Magic Mouse",
    })

    def test_required_accessibility_keys_present_in_all_locales(self):
        for locale, strings in _TRANSLATIONS.items():
            with self.subTest(locale=locale):
                missing = self.REQUIRED_KEYS - strings.keys()
                self.assertFalse(missing, f"{locale} missing keys: {missing}")
                for key in self.REQUIRED_KEYS:
                    self.assertTrue(
                        strings[key].strip(),
                        f"{locale}.{key} is blank",
                    )

    def test_chinese_locales_do_not_passthrough_english(self):
        """Trackpad strings used to ship English text in the zh_CN and
        zh_TW maps. Pin that they are now actually localized."""
        for locale in ("zh_CN", "zh_TW"):
            with self.subTest(locale=locale):
                for key in (
                    "scroll.ignore_trackpad",
                    "scroll.ignore_trackpad_desc",
                ):
                    self.assertNotIn(
                        _TRANSLATIONS[locale][key],
                        self.ENGLISH_VALUES,
                        f"{locale}.{key} still ships English",
                    )
                self.assertNotEqual(
                    _TRANSLATIONS[locale]["scroll.smart_shift"],
                    "SmartShift",
                    f"{locale}.scroll.smart_shift still ships English",
                )


if __name__ == "__main__":
    unittest.main()
