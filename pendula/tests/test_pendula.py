from __future__ import absolute_import, division, print_function
import os.path as op
import numpy as np
import pandas as pd
import numpy.testing as npt
import pendula as pu

def test_testing():
    """
    runs dummy test

    Returns
    -------
    None.

    """
    Pendulum = pu.Pendulum()
    ans = Pendulum.dummytest()
    assert ans