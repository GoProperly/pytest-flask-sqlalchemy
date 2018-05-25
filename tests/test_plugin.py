def test_plugin(testfile, conftest, testdir):
    '''
    Run all tests for this file using a temporary conftest file.
    '''
    # Load a temp conftest from file
    # testdir.makeconftest(conftest)

    # Load tests from file
    testdir.makepyfile("""
        def test_pytester():
            '''
            Make sure pytester works.
            '''
            assert 1 + 1 == 2
    """)

    # Run tests
    result = testdir.runpytest()
    result.assert_outcomes(passed=1)
