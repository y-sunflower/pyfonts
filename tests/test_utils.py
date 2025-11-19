from pyfonts.utils import _map_weight_to_numeric
import pytest


def test_map_weight_to_numeric():
    assert _map_weight_to_numeric("thin") == 100
    assert _map_weight_to_numeric("extra-light") == 200
    assert _map_weight_to_numeric("light") == 300
    assert _map_weight_to_numeric("regular") == 400
    assert _map_weight_to_numeric("medium") == 500
    assert _map_weight_to_numeric("semi-bold") == 600
    assert _map_weight_to_numeric("bold") == 700
    assert _map_weight_to_numeric("extra-bold") == 800
    assert _map_weight_to_numeric("black") == 900

    assert _map_weight_to_numeric(200) == 200
    assert _map_weight_to_numeric(700) == 700

    with pytest.raises(ValueError, match="Invalid weight descriptor: "):
        _map_weight_to_numeric("invalid-weight")
