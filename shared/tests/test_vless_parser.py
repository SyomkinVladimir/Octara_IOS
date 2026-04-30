import unittest

from shared.profile_parser.vless_parser import parse_vless_url


class TestVlessParser(unittest.TestCase):
    def test_parse_basic_vless_url(self):
        url = (
            "vless://123e4567-e89b-12d3-a456-426614174000@example.com:443"
            "?security=reality&type=tcp&sni=google.com&fp=chrome&pbk=testkey&sid=abcd"
            "#TestProfile"
        )

        profile = parse_vless_url(url)

        self.assertEqual(profile.uuid, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(profile.address, "example.com")
        self.assertEqual(profile.port, 443)
        self.assertEqual(profile.security, "reality")
        self.assertEqual(profile.network, "tcp")
        self.assertEqual(profile.sni, "google.com")
        self.assertEqual(profile.fingerprint, "chrome")
        self.assertEqual(profile.public_key, "testkey")
        self.assertEqual(profile.short_id, "abcd")
        self.assertEqual(profile.remark, "TestProfile")

    def test_rejects_non_vless_url(self):
        with self.assertRaises(ValueError):
            parse_vless_url("https://example.com")
    
    def test_rejects_url_without_port(self):
        with self.assertRaises(ValueError):
            parse_vless_url(
                "vless://123e4567-e89b-12d3-a456-426614174000@example.com?security=reality#NoPort"
            ) 


if __name__ == "__main__":
    unittest.main()