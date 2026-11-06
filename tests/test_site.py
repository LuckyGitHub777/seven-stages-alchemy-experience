import unittest
from pathlib import Path

HTML=Path(__file__).resolve().parents[1].joinpath("index.html").read_text(encoding="utf-8")
class AlchemySiteTests(unittest.TestCase):
    def test_stages_and_scope(self):
        for name in ("Calcination","Dissolution","Separation","Conjunction","Fermentation","Distillation","Coagulation"):
            self.assertIn(name,HTML)
        self.assertIn("Content-Security-Policy",HTML)
        self.assertNotIn("luckygithub777.github.io",HTML)
    def test_self_contained(self):
        self.assertIn("<script",HTML)
        self.assertNotIn("<script src=",HTML)
        self.assertNotIn("<iframe",HTML)
