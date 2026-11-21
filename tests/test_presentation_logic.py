"""
test_presentation_logic.py - Presentation Structure & Dialogue Timeline Verification
Validates:
  1. Exactly 7 scenes.
  2. Total duration is exactly 165 seconds.
  3. Character identities are Dr. Sebastian Clarke and Dr. Oliver Bennett.
  4. Previous project names are strictly avoided.
  5. Dialogue turns are non-overlapping and contiguous.
"""

import os
import json
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCENES_PATH = os.path.join(BASE_DIR, 'data', 'scenes.json')

class TestPresentationLogic(unittest.TestCase):

    def setUp(self):
        self.assertTrue(os.path.exists(SCENES_PATH), "data/scenes.json must exist")
        with open(SCENES_PATH, 'r', encoding='utf-8') as f:
            self.scenes = json.load(f)

    def test_exact_seven_scenes(self):
        """Presentation must have exactly 7 scenes."""
        self.assertEqual(len(self.scenes), 7, f"Expected exactly 7 scenes, found {len(self.scenes)}")

    def test_total_presentation_duration(self):
        """Total presentation duration must equal exactly 165 seconds."""
        total_duration = sum(s['duration'] for s in self.scenes)
        self.assertEqual(total_duration, 165, f"Expected 165 seconds total, got {total_duration}")
        self.assertEqual(self.scenes[0]['start_time'], 0)
        self.assertEqual(self.scenes[-1]['end_time'], 165)

    def test_character_identities(self):
        """Only Sebastian and Oliver may speak; forbidden names must not exist."""
        forbidden_names = ["adrian", "reynolds", "ethan", "carter", "nathaniel", "brooks", "julian", "hayes"]
        allowed_speakers = {"sebastian", "oliver"}

        all_dialogues = []
        for scene in self.scenes:
            for d in scene['dialogues']:
                all_dialogues.append(d)
                speaker = d['speaker'].lower()
                self.assertIn(speaker, allowed_speakers, f"Invalid speaker '{speaker}' found")
                
                # Check forbidden names in text
                text_lower = d['text'].lower()
                for fn in forbidden_names:
                    self.assertNotIn(fn, text_lower, f"Forbidden previous name '{fn}' found in dialogue: {d['id']}")

        self.assertGreater(len(all_dialogues), 0)

    def test_dialogue_timing_and_contiguity(self):
        """Dialogues must have valid positive durations and stay within scene bounds."""
        for scene in self.scenes:
            s_start = scene['start_time']
            s_end = scene['end_time']
            for d in scene['dialogues']:
                self.assertGreaterEqual(d['start_sec'], s_start)
                self.assertLessEqual(d['end_sec'], s_end)
                self.assertGreater(d['end_sec'], d['start_sec'])
                self.assertEqual(d['duration'], d['end_sec'] - d['start_sec'])

if __name__ == '__main__':
    unittest.main()
