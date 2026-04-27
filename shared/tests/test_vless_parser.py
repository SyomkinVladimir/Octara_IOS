import unittest

from shared.profile_parser.vless_parser import parse_vless_link


class TestVLESSParser(unittest.TestCase):
    def test_parse_basic_vless_link(self):
        link = "vless://123e4567-e89b-12d3-a456-426614174000@example.com:443#TestProfile"

        profile = parse_vless_link(link)

        self.assertEqual(profile.raw_link, link)
        self.assertEqual(profile.name, "TestProfile")
        self.assertEqual(profile.server, "example.com")
        self.assertEqual(profile.port, 443)
        self.assertEqual(profile.uuid, "123e4567-e89b-12d3-a456-426614174000")


if __name__ == "__main__":
    unittest.main()
