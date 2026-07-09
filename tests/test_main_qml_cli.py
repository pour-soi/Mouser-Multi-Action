import unittest

try:
    import main_qml
except Exception:  # pragma: no cover - env without PySide6 / project deps
    main_qml = None


@unittest.skipIf(main_qml is None, "main_qml / PySide6 not available")
class MainQmlCliTests(unittest.TestCase):
    def test_parse_known_cli_flags_and_forwards_qt_args(self):
        parsed = main_qml._parse_cli_args([
            "main_qml.py",
            "--start-hidden",
            "--hid-backend=auto",
            "--qt-flag",
        ])

        self.assertEqual(
            parsed,
            (
                ["main_qml.py", "--qt-flag"],
                "auto",
                True,
                False,
            ),
        )


if __name__ == "__main__":
    unittest.main()
