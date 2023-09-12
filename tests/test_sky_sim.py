import pytest
import numpy as np

from mymodule.sky_sim import get_radec, make_stars
# segadecimal_to_float, float_to_segadecimal

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

@pytest.mark.parametrize("ra,dec,nsrc", [(0, 0, 100), (0, 0, 1000)])
def test_make_stars_length(ra, dec, nsrc):
    """
    Check if the array output by make_stars is the right length
    """
    ras, decs = make_stars(ra, dec, nsrc=nsrc)

    assert len(ras) == nsrc
    assert len(decs) == nsrc

@pytest.mark.parametrize("ra,dec", [(0,0), (14.215420962967535,41.26916666666667)])
def test_make_stars_range(ra, dec):
    """
    Check all of the values generated are in the right range (within one degree of the centre)
    """
    ras, decs = make_stars(ra, dec)

    assert np.all(np.array(ras) > ra - 1)
    assert np.all(np.array(ras) < ra + 1)

    assert np.all(np.array(decs) > dec - 1)
    assert np.all(np.array(decs) < dec + 1)

# @pytest.mark.parameterize("ra,dec", [(14.215420962967535,41.26916666666667)])
# def test_segadecimal_to_float(ra, dec):
#     new_ra, new_dec = segadecimal_to_float(
#         *float_to_segadecimal(ra, dec))
    
#     assert new_ra == pytest.approx(ra)
#     assert new_dec == pytest.approx(dec)