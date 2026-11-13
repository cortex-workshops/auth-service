from auth.cart import subtotal


def test_subtotal():
    assert subtotal([{"price": 10.0, "qty": 2}, {"price": 5.5, "qty": 1}]) == 25.5
