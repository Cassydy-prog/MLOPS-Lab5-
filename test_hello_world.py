from hello_world import greet, generate_html

def test_greet():
    assert greet() == 'Welcome to CI/CD 101 using GitHub Actions!'

def test_generate_html():
    message = "Test Message"
    html = generate_html(message)
    assert message in html
    assert "<html>" in html and "<div" in html and "<image" in html