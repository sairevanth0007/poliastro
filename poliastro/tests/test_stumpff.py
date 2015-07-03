# coding: utf-8
from numpy import cos, sin, cosh, sinh
from numpy.testing import assert_almost_equal, assert_equal

from poliastro.stumpff import c2, c3


def test_stumpff_functions_near_zero():
    psi = 0.5
    expected_c2 = (1 - cos(psi**.5)) / psi
    expected_c3 = (psi**.5 - sin(psi**.5)) / psi**1.5

    assert_almost_equal(c2(psi), expected_c2)
    assert_almost_equal(c3(psi), expected_c3)


def test_stumpff_functions_above_zero():
    psi = 3.0
    expected_c2 = (1 - cos(psi**.5)) / psi
    expected_c3 = (psi**.5 - sin(psi**.5)) / psi**1.5

    assert_equal(c2(psi), expected_c2)
    assert_equal(c3(psi), expected_c3)


def test_stumpff_functions_under_zero():
    psi = -3.0
    expected_c2 = (cosh((-psi)**.5) - 1) / (-psi)
    expected_c3 = (sinh((-psi)**.5) - (-psi)**.5) / (-psi)**1.5

    assert_equal(c2(psi), expected_c2)
    assert_equal(c3(psi), expected_c3)
