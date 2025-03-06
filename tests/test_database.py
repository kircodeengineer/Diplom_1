import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:
    def test_available_buns_count(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        assert len(available_buns) == len(data_bun.buns)

    @pytest.mark.parametrize(
        'expected_bun_name_id', [["black bun", 0], ["white bun", 1], ["red bun", 2]]
    )
    def test_available_buns_names(self, expected_bun_name_id):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        expected_bun_name = expected_bun_name_id[0]
        id = expected_bun_name_id[1]
        assert expected_bun_name in available_buns[id].name

    def test_available_ingredients_count(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == len(data_ingredients.ingredients)

    @pytest.mark.parametrize(
        'expected_type, expected_name, expected_price, id',
        [
            [INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 0],
            [INGREDIENT_TYPE_SAUCE, "sour cream", 200, 1],
            [INGREDIENT_TYPE_SAUCE, "chili sauce", 300, 2],
            [INGREDIENT_TYPE_FILLING, "cutlet", 100, 3],
            [INGREDIENT_TYPE_FILLING, "dinosaur", 200, 4],
            [INGREDIENT_TYPE_FILLING, "sausage", 300, 5],
        ]
    )
    def test_available_ingredients_names_and_prices(self, expected_type, expected_name, expected_price, id):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert available_ingredients[id].name == expected_name
        assert available_ingredients[id].type == expected_type
        assert available_ingredients[id].price == expected_price
