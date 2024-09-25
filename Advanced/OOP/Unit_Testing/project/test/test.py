from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def SetUp(self):
        self.media = SocialMedia('Name', 'Platform', 5, 'Type')

    def test_init(self):
        self.assertEqual('Name', self.media._username)
        self.assertEqual('Platform', self.media._platform)
        self.assertEqual(5, self.media._followers)
        self.assertEqual('Type', self.media._content_type)


if __name__ == '__main__':
    main()