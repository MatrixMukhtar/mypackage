from mypackage import myModule


def test_top_n():
    ''' Ensuring the funstion works, we use this
    for unit testing'''

    assert myModule.top_n([2,3,1,56,33],3)==[56, 33, 3],'incorrect'


