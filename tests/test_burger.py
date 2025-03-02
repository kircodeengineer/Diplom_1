from unittest.mock import Mock

from database import Database
from praktikum.burger import Burger, Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

from input_data import BunData


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(BunData.NAME, BunData.PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = BunData.NAME
        mock_ingredient.get_price.return_value = BunData.PRICE
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_name() == BunData.NAME
        assert burger.ingredients[0].get_price() == BunData.PRICE
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient(self):
        burger = Burger()
        database = Database()
        buns = database.available_buns()[0]
        sauce = database.available_ingredients()[0]
        filling = database.available_ingredients()[3]
        burger.set_buns(buns)
        burger.add_ingredient(sauce)
        sauce_index = len(burger.ingredients) - 1
        burger.add_ingredient(filling)
        filling_index = len(burger.ingredients) - 1
        burger.move_ingredient(sauce_index, filling_index)
        expected_price = buns.price * 2
        expected_price += sauce.price
        expected_price += filling.price
        expected_receipt = f"(==== {buns.name} ====)\n" \
                           f"= filling {filling.name} =\n" \
                           f"= sauce {sauce.name} =\n" \
                           f"(==== {buns.name} ====)\n\n" \
                           f"Price: {expected_price}"
        assert burger.get_receipt() == expected_receipt

    def test_get_price(self):
        burger = Burger()
        database = Database()
        buns = database.available_buns()[0]
        sauce = database.available_ingredients()[0]
        filling = database.available_ingredients()[3]
        burger.set_buns(buns)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        expected_price = buns.price * 2
        expected_price += sauce.price
        expected_price += filling.price
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        buns = database.available_buns()[0]
        sauce = database.available_ingredients()[0]
        filling = database.available_ingredients()[3]
        burger.set_buns(buns)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        expected_price = buns.price * 2
        expected_price += sauce.price
        expected_price += filling.price
        expected_receipt = f"(==== {buns.name} ====)\n"\
                           f"= sauce {sauce.name} =\n"\
                           f"= filling {filling.name} =\n"\
                           f"(==== {buns.name} ====)\n\n"\
                           f"Price: {expected_price}"
        assert burger.get_receipt() == expected_receipt