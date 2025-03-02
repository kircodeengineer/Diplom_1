from input_data import BunData
from praktikum.bun import Bun


class TestBun:
    def test_get_name(self):
        bun = Bun(BunData.NAME, BunData.PRICE)
        assert bun.get_name() == BunData.NAME

    def test_get_price(self):
        bun = Bun(BunData.NAME, BunData.PRICE)
        assert bun.get_price() == BunData.PRICE