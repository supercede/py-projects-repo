from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotesPageLocators.QUOTE
        quote_collection = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quote_collection]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.TAG_DROPDOWN)
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(QuotesPageLocators.SEARCH_BUTTON)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        tags = self.tag_dropdown.options
        return [option.text.strip() for option in tags]

    def select_tag(self, tag: str):
        self.tag_dropdown.select_by_visible_text(tag)

    def search_for_quotes(self, author_name: str, tag_name: str) -> List[QuoteParser]:
        self.select_author(author_name)

        # Ask selenium to wait either until dropdown options show on the page or for 10 seconds
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTIONS)
            )
        )
        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author {author_name} does not have any quotes with this tag")
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass
