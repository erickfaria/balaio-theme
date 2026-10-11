"""Regressions for Designer substitutions, locales and default contrast."""
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_theme import designer_settings, preview_css

B = "{http://www.google.com/2005/gml/b}"
DECL = '<Variable name="paper" description="Background" type="color" default="#fffefb"/>'


def skin(path):
    return ET.parse(path).getroot().find(f".//{B}skin").text


def luminance(hex_color):
    channels = [int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


class DesignerTests(unittest.TestCase):
    def test_unknown_reference_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Undeclared"):
            preview_css("body { color:$missing; }")

    def test_duplicate_declarations_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            designer_settings("/*" + DECL * 2 + "*/")

    def test_default_and_saved_value_resolution(self):
        css = "/*" + DECL + "*/body { background:$paper; }"
        self.assertIn("background:#fffefb", preview_css(css))
        saved = css.replace('default="#fffefb"', 'default="#fffefb" value="#eef2f6"')
        self.assertIn("background:#eef2f6", preview_css(saved))

    def test_locales_preserve_customization_values(self):
        def config(path):
            return {name: {key: value for key, value in attrs.items() if key != "description"}
                    for name, attrs in designer_settings(skin(path)).items()}
        self.assertEqual(config(ROOT / "theme/balaio.xml"), config(ROOT / "theme/balaio.en.xml"))

    def test_default_text_contrast_on_pastel_surfaces(self):
        settings = designer_settings(skin(ROOT / "theme/balaio.xml"))
        for text in ("inkcolor", "mutedcolor", "accentcolor"):
            for surface in ("papercolor", "washcolor", "sandcolor", "bluecolor"):
                a, b = sorted((luminance(settings[text]["default"]), luminance(settings[surface]["default"])))
                with self.subTest(text=text, surface=surface):
                    self.assertGreaterEqual((b + 0.05) / (a + 0.05), 4.5)


if __name__ == "__main__":
    unittest.main()
