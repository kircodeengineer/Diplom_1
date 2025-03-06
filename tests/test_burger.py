from unittest.mock import Mock

from praktikum.burger import Burger, Bun
from input_data import *


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(BunData.NAME, BunData.PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name = SauceIngredientData.NAME
        mock_ingredient.price = SauceIngredientData.PRICE
        mock_ingredient.type = SauceIngredientData.TYPE
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].name == mock_ingredient.name
        assert burger.ingredients[0].price == mock_ingredient.price
        assert burger.ingredients[0].type == mock_ingredient.type

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient(self):
        burger = Burger()

        mock_buns = Bun(BunData.NAME, BunData.PRICE)

        mock_first_ingredient = Mock()
        mock_first_ingredient.name = SauceIngredientData.NAME
        mock_first_ingredient.get_name.return_value = SauceIngredientData.NAME
        mock_first_ingredient.get_price.return_value = SauceIngredientData.PRICE
        mock_first_ingredient.get_type.return_value = SauceIngredientData.TYPE

        mock_second_ingredient = Mock()
        mock_second_ingredient.name = FillingIngredientData.NAME
        mock_second_ingredient.get_name.return_value = FillingIngredientData.NAME
        mock_second_ingredient.get_price.return_value = FillingIngredientData.PRICE
        mock_second_ingredient.get_type.return_value = FillingIngredientData.TYPE

        burger.set_buns(mock_buns)
        burger.add_ingredient(mock_first_ingredient)
        sauce_index = len(burger.ingredients) - 1
        burger.add_ingredient(mock_second_ingredient)
        filling_index = len(burger.ingredients) - 1
        burger.move_ingredient(sauce_index, filling_index)
        expected_receipt = f"= filling {mock_second_ingredient.name} =\n" \
                           f"= sauce {mock_first_ingredient.name} =\n"
        assert expected_receipt in burger.get_receipt()

    def test_get_price(self):
        burger = Burger()

        mock_buns = Bun(BunData.NAME, BunData.PRICE)

        mock_first_ingredient = Mock()
        mock_first_ingredient.name = SauceIngredientData.NAME
        mock_first_ingredient.get_name.return_value = SauceIngredientData.NAME
        mock_first_ingredient.get_price.return_value = SauceIngredientData.PRICE
        mock_first_ingredient.get_type.return_value = SauceIngredientData.TYPE

        mock_second_ingredient = Mock()
        mock_second_ingredient.name = FillingIngredientData.NAME
        mock_second_ingredient.get_name.return_value = FillingIngredientData.NAME
        mock_second_ingredient.get_price.return_value = FillingIngredientData.PRICE
        mock_second_ingredient.get_type.return_value = FillingIngredientData.TYPE

        burger.set_buns(mock_buns)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        expected_price = mock_buns.price * 2
        expected_price += mock_first_ingredient.get_price()
        expected_price += mock_second_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()

        mock_buns = Bun(BunData.NAME, BunData.PRICE)

        mock_first_ingredient = Mock()
        mock_first_ingredient.name = SauceIngredientData.NAME
        mock_first_ingredient.get_name.return_value = SauceIngredientData.NAME
        mock_first_ingredient.get_price.return_value = SauceIngredientData.PRICE
        mock_first_ingredient.get_type.return_value = SauceIngredientData.TYPE

        mock_second_ingredient = Mock()
        mock_second_ingredient.name = FillingIngredientData.NAME
        mock_second_ingredient.get_name.return_value = FillingIngredientData.NAME
        mock_second_ingredient.get_price.return_value = FillingIngredientData.PRICE
        mock_second_ingredient.get_type.return_value = FillingIngredientData.TYPE

        burger.set_buns(mock_buns)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        expected_price = mock_buns.price * 2
        expected_price += mock_first_ingredient.get_price()
        expected_price += mock_second_ingredient.get_price()
        expected_receipt = f"(==== {mock_buns.name} ====)\n" \
                           f"= sauce {mock_first_ingredient.name} =\n" \
                           f"= filling {mock_second_ingredient.name} =\n" \
                           f"(==== {mock_buns.name} ====)\n\n" \
                           f"Price: {expected_price}"
        assert burger.get_receipt() == expected_receipt