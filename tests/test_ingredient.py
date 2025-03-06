import pytest
from praktikum.ingredient import Ingredient
from input_data import FillingIngredientData, SauceIngredientData


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(FillingIngredientData.TYPE, FillingIngredientData.NAME, FillingIngredientData.PRICE)
        assert ingredient.get_price() == FillingIngredientData.PRICE

    def test_get_name(self):
        ingredient = Ingredient(SauceIngredientData.TYPE, SauceIngredientData.NAME, SauceIngredientData.PRICE)
        assert ingredient.get_name() == SauceIngredientData.NAME

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [FillingIngredientData.TYPE, FillingIngredientData.NAME, FillingIngredientData.PRICE, FillingIngredientData.TYPE],
            [SauceIngredientData.TYPE, SauceIngredientData.NAME, SauceIngredientData.PRICE, SauceIngredientData.TYPE]
        ]
    )
    def test_get_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient