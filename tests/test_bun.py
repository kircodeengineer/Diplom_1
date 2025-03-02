from praktikum.bun import Bun


class TestBun:
    class BunTestData:
        NAME = "Тестовая булка"
        PRICE = 123

    def test_get_name_return_valid_name(self):
        bun = Bun(self.BunTestData.NAME, self.BunTestData.PRICE)
        assert bun.get_name() == self.BunTestData.NAME

    def test_get_price_return_valid_price(self):
        bun = Bun(self.BunTestData.NAME, self.BunTestData.PRICE)
        assert bun.get_price() == self.BunTestData.PRICE