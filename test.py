import unittest
import json
from resources.telegram import handleTelegramResponse

class TelegramTests(unittest.TestCase):
  def test_channel_1(self):
    f = open('fixtures/channel.1.input.json')
    data = json.load(f)
    f.close()
    res = handleTelegramResponse(data)
    self.assertEqual(len(res), 8)
  def test_group_1(self):
    f = open('fixtures/group.1.input.json')
    data = json.load(f)
    f.close()
    res = handleTelegramResponse(data)
    self.assertEqual(len(res), 2)
  def test_fail(self):
    f = open('fixtures/fail.json')
    data = json.load(f)
    f.close()
    res = handleTelegramResponse(data)
    self.assertEqual(len(res), 0)
  def test_empty(self):
    f = open('fixtures/empty.json')
    data = json.load(f)
    f.close()
    res = handleTelegramResponse(data)
    self.assertEqual(len(res), 0)
if __name__ == "__main__":
  unittest.main()