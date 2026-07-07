import importlib
import os
import sys
import unittest
from unittest.mock import patch

from core import app_detector


class AppDetectorLinuxTests(unittest.TestCase):
    def _reload_for_linux(self, session_type: str, desktop: str):
        with (
            patch.object(sys, "platform", "linux"),
            patch.dict(
                os.environ,
                {
                    "XDG_SESSION_TYPE": session_type,
                    "XDG_CURRENT_DESKTOP": desktop,
                },
                clear=False,
            ),
        ):
            importlib.reload(app_detector)
        self.addCleanup(importlib.reload, app_detector)
        return app_detector

    def test_kde_wayland_prefers_kdotool(self):
        module = self._reload_for_linux("wayland", "KDE")

        with (
            patch.object(module, "_get_foreground_kdotool", return_value="/tmp/kde-app"),
            patch.object(module, "_get_foreground_xdotool", return_value="/tmp/x11-app") as xdotool,
        ):
            self.assertEqual(module.get_foreground_exe(), "/tmp/kde-app")
            xdotool.assert_not_called()

    def test_kde_wayland_falls_back_to_xdotool(self):
        module = self._reload_for_linux("wayland", "KDE")

        with (
            patch.object(module, "_get_foreground_kdotool", return_value=None),
            patch.object(module, "_get_foreground_xdotool", return_value="/tmp/xwayland-app") as xdotool,
        ):
            self.assertEqual(module.get_foreground_exe(), "/tmp/xwayland-app")
            xdotool.assert_called_once_with()

    def test_non_kde_wayland_returns_none(self):
        module = self._reload_for_linux("wayland", "GNOME")

        with patch.object(module, "_get_foreground_xdotool", return_value="/tmp/x11-app") as xdotool:
            self.assertIsNone(module.get_foreground_exe())
            xdotool.assert_not_called()

    def test_x11_uses_xdotool(self):
        module = self._reload_for_linux("x11", "KDE")

        with patch.object(module, "_get_foreground_xdotool", return_value="/tmp/x11-app") as xdotool:
            self.assertEqual(module.get_foreground_exe(), "/tmp/x11-app")
            xdotool.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
