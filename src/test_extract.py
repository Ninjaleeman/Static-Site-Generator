import unittest

from src.generate_page import extract_title



class TestExtract(unittest.TestCase):
  def test_extract(self):
    title = extract_title("# Hello")
    expected_title = ("Hello")
    self.assertEqual(title, expected_title)

  def test_exception_raised(self):
      # Markdown with no h1 heading
      markdown_no_h1 = "## This is an h2 heading\nNot an h1 heading."
      
      # This asserts that extract_title raises an Exception when called with markdown_no_h1
      with self.assertRaises(Exception):
          extract_title(markdown_no_h1)


if __name__ == "__main__":
    unittest.main()