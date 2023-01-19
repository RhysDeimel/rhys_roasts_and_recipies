import pytest
from roasts_and_recipies import create_app


@pytest.fixture
def browser():
    from selenium import webdriver

    b = webdriver.Firefox()

    yield b

    b.quit()


# def test_project_init(browser):
#     browser.get("http://localhost:5000")

#     assert "Hello, index!" in browser.page_source


# Kristen has heard about Rhys' new cooking website. She goes
# to check out it's homepage
def test_check_can_open_homepage(browser):
    browser.get("http://localhost:5000")

    assert "Hello, index!" in browser.page_source
    assert "Rhys' Roasts" in browser.title


# She notices the page title and header mention recipies

# She notices a search bar, and a random recipie below with an
# an option to add to the recipe list

# She adds the recipe to the recipe list and receives feedback
# that it has been added

# She decides to search for seasonal recipies. When she hits enter,
# the page updates, and now the page lists seasonal recipes

# She adds the recipe to the recipe list and receives feedback
# that it has been added

# She decides to search for a recipie by keyword. When she hits
# enter, the page updates, and now the page lists recipes with
# keyword matches

# She adds the recipe to the recipe list and receives feedback
# that it has been added

# She decides to search for a recipie by ingredient When she hits
# enter, the page updates, and now the page lists all recipes that
# include that ingredient

# She adds the recipe to the recipe list and receives feedback
# that it has been added

# She decides she has enough recipes added and goes to the recipe
# list page

# On the recipe list page, she can see the recipies she has chosen

# She decides she doesn't like one of the recipes she has chosen and
# selects the option to delete it

# The page updates and the recipe is removed from the list

# She then decides she doesn't like any of the recipes she has chosen
# and selects the option to clear the whole list

# The page updates and all recipes are removed from the list

# She decides to leave it up to chance and asks the site to randomly
# select 5 recipes for her.

# The page updates and 5 random seasonal recipes are displayed

# She decides she wants an additional recipe and navigates to the
# home page.

# She adds the random homepage recipe the the recipe list and
# navigates back to the recipe list and can see it has been added
# to the list

# Kristen wonders whether the site will remeber her list. She closes
# the page and then re-opens it and navigates back to the recipe list.
# She can see that the recipes are still there.

# Satisfied with the chosen recipes, she selects the option to generate
# a grocery list

# The page updates and an itemised list of ingredients is displayed

# The items have checkboxes next to them. Kristen goes to the kitchen
# and checks off ingredients she already has

# The checked ingredients are crossed off and moved to the
# bottom of the page

# She can re-check crossed off items, and they are moved back to the top
# of the page

# Once she is finished, Kristen can select and option to convert
# the unchecked items to simple text items that can be copy-pasted

# Kristen can then copy this list into the Coles or Woolworths website
