from scrape_mate.scraper import fetch_content, parse_html


def test_fetch_content():
    url = "https://example.com"
    content = fetch_content(url)
    assert "<title>Example Domain</title>" in content


def test_parse_html():
    html = "<html><body><div class='test'>Hello World</div></body></html>"
    result = parse_html(html, "div", "test")
    assert len(result) == 1
    assert result[0].text == "Hello World"
