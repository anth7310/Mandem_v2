import unittest
import read_json

class TestMessengerMethods(unittest.TestCase):
    
    def setUp(self):
        self.messager = read_json.Messenger('kenneth.json')

    def test_participants(self):
        self.assertEqual(self.messager.participants(), ['Kenneth CK', 'Anthony Inthavong'], 'Names are not correct')

    def test_title(self):
        self.assertTrue(self.messager.is_still_participant(), 'title of chat is wrong')

    def test_is_still_participant(self):
        self.assertTrue(self.messager.is_still_participant(), 'is still participant is wrong')

    def test_generate_messages_keys(self):
        self.assertSetEqual(self.messager._generate_messages_keys(), {'timestamp_ms', 'reactions', 'sender_name', 'share', 'gifs', 'sticker', 'type', 'photos', 'content', 'files'})

    def test_messages(self):
        pass

    def test_messages_to_bytes(self):
        self.assertEqual

if __name__ == '__main__':
    unittest.main()