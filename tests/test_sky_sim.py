import pytest

from mymodule.sky_sim import get_radec, segadecimal_to_float, float_to_segadecimal

def test_module_import():
    try:
        import mymodule.sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return

def test_get_radec_values():
    """
    This checks that get_radec gives back thecorrect values of Andromeda in decimal form
    """
    ra, dec = get_radec()
    assert ra == pytest.approx(14.215420962967535, rel = 1e-20)
    assert dec == pytest.approx(41.26916666666667, rel = 1e-20)

@pytest.mark.parameterize("ra,dec", [(14.215420962967535,41.26916666666667)])
def test_segadecimal_to_float(ra, dec):
    new_ra, new_dec = segadecimal_to_float(
        *float_to_segadecimal(ra, dec))
    
    assert new_ra == pytest.approx(ra)
    assert new_dec == pytest.approx(dec)