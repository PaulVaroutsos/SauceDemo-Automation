# What is this?

This is a sample test automation framework for www.saucedemo.com.  SauceDemo is a sample website built by SauceLabs that allows users to practice browser automation.

**Why would you write automated tests for a fake website?**

Many Selenium tutorials online show:
- How to load a page
- How to select elements
- How to interact with elements

For example: 

```py
def test_google_search():
  driver.get("www.google.com")
  text_box = driver.find_element_by_name("q")
  text_box.send_keys("selenium tutorial") # Enter search text
  button = driver.find_element_by_name("btnK") # Click search
  button.click()
  print("Test passed.")
  ```

This is great.  It shows how simply and quickly selenium scripts can be set-up and run without much
programming experience.  The Selenium scripts are intuitive and easy to follow with a basic understanding
of Python.

However, this doesn't give a lot of insight into what a test automation framework might look like
using the page object model. i.e. Something that isn't just searching google.com.  This framework is a slightly more in-depth example that shows:
- Examples using the Page Object Model.
- How to run multiple tests simultaneously.
- How to include test frameworks like Pytest.

This example can be used as a starting point for beginners of Selenium to play around and experiment with. It utilizes SauceLab's simple and easy website so you don't have to worry about overly complex test cases.

**Why saucedemo.com?**

Saucelabs is a reputable automation testing platform company. It is likely to remain online without being taken down, allowing this demo to be viewed and run by others. This website was built to be automated against. Saucedemo.com is reliable and quick which leads to few false positive test failures.

**What do these tests cover?**

These tests cover many test cases such as signing in/out, adding items to the cart, and checking out.

**What isn't tested?**

Layout issues, sessions, cookies, APIs, etc.

**What do I need to run this example?**

See the requirements file.
