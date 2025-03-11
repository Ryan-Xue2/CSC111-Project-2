"""This module contains helper functions for the app"""
import textwrap


class Helper:
    """A helper class storing all useful help functions for ease of access"""

    @staticmethod
    def wraptext(text: str, length: int) -> str:
        """A stylistic function that helps with wrapping long strings (paragraphs) of text for a more appealing look.
         Text is the string of text being styled and length is the max letter length for one line in a paragraph."""
        return textwrap.fill(text, length)


if __name__ == "__main__":
    # pass
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['R1705', 'E9998', 'E9999']
    })
