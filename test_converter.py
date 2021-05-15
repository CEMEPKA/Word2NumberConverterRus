import pytest
from number_convertor import NumberConvertor


@pytest.fixture(scope='module')
def convertor():
    return NumberConvertor()


tests = [
    (
        "Я купил сорок пять килограмм картошки и 7 пудов моркови",
        "Я купил 45 килограмм картошки и 7 пудов моркови"
    ),
    (
        "Девятьсот восемьдесят семь тысяч шестьсот пятьдесят четыре минус 321",
        "987654 минус 321"
    ),
    (
        "Госдолг США в середине прошлого века составил двести пятьдесят шесть миллиардов девятьсот миллионов долларов",
        "Госдолг США в середине прошлого века составил 256900000000 долларов"
    )
]


@pytest.mark.parametrize('test', tests)
def test_extractor(convertor: NumberConvertor, test: any):
    text, result = test
    guess = convertor.convert_groups(text)
    assert guess == result
