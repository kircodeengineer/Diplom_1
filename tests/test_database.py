import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:
    def test_available_buns_count(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        assert len(available_buns) == len(data_bun.buns)

    @pytest.mark.parametrize(
        'expected_bun_name', ["black bun", "white bun", "red bun"]
    )
    def test_available_buns_names(self, expected_bun_name):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        available_buns_names = [i.get_name() for i in available_buns]
        assert expected_bun_name in available_buns_names

    def test_available_ingredients_count(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == len(data_ingredients.ingredients)

    @pytest.mark.parametrize(
        'expected_type, expected_name, expected_price',
        [
            [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
            [INGREDIENT_TYPE_SAUCE, "sour cream", 200],
            [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
            [INGREDIENT_TYPE_FILLING, "cutlet", 100],
            [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
            [INGREDIENT_TYPE_FILLING, "sausage", 300],
        ]
    )
    def test_available_ingredients_names_and_prices(self, expected_type, expected_name, expected_price):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        name_price_type = {i.get_name(): [i.get_price(), i.get_type()]  for i in available_ingredients}
        assert name_price_type[expected_name] == [expected_price, expected_type]
