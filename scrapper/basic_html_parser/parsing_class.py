from bs4 import BeautifulSoup
import re

class ParseItemLocators:
    NAME_LOCATOR = 'article.product_pod h3 a'
    RATING_LOCATOR = 'article.product_pod p.star-rating'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    LINK_LOCATOR = 'article.product_pod h3 a'

class ParseItem:
    """
    A class to take in an HTML page and find properties of a selected item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def find_item_name(self):
        locator = ParseItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def find_item_location(self):
        locator = ParseItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['href']
        return item_name

    @property
    def find_price(self):
        pattern = '[0-9]+\.[0-9]+'
        locator = ParseItemLocators.PRICE_LOCATOR
        price_selector = self.soup.select_one(locator)
        # price_selector = soup.find('p', {'class': 'price_color'})
        price = price_selector.string
        price_str = re.findall(pattern, price)[0]
        price_float = float(price_str)
        return price_float

    @property
    def find_rating(self):
        locator = ParseItemLocators.RATING_LOCATOR
        rating_selector = self.soup.select_one(locator)
        classes = rating_selector.attrs['class']
        rating = filter(lambda x: x != 'star-rating', classes)
        return next(rating)

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''

article = ParseItem(ITEM_HTML)

print(article.find_item_name)
print(article.find_rating)
print(article.find_price)
print(article.find_item_location)
