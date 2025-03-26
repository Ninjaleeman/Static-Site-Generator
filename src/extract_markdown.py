import re

def extract_markdown_images(text):
    """
    Extracts matches for Markdown-formatted images, e.g., ![alt text](url),
    and returns a list of tuples (alt_text, url).
    """
    # Regex pattern for images
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)\"\']*)\)"  # Avoid nested brackets or invalid chars like quotes in the URL

    # Find all matches
    matches = re.findall(pattern, text)

    # Strip matches for cleaner output
    cleaned_matches = [(alt_text.strip(), url.strip()) for alt_text, url in matches]

    return cleaned_matches


def extract_markdown_links(text):
    """
    Extracts matches for Markdown-formatted links, e.g., [link text](url),
    and returns a list of tuples (link_text, url).
    """
    # Regex pattern for links (exclude image links using negative lookbehind)
    pattern = r"(?<!!)\[(.*?)\]\(([^\(\)\"\']*)\)"  # No nested parens/quotes in URL

    # Find all matches
    matches = re.findall(pattern, text)

    # Strip matches for cleaner output
    cleaned_matches = [(link_text.strip(), url.strip()) for link_text, url in matches]

    return cleaned_matches