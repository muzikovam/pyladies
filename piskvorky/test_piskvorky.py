import piskvorky
import ai
import pytest
def test_tah():
    pole = piskvorky.tah('--------------------', 1, "x")
    assert len(pole) == 20


def test_pocitac():
        with pytest.raises(ValueError):
            ai.tah_pocitace('oxoxoxoxoxoxoxoxoxox',"o")
