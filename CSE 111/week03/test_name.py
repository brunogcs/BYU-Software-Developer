import pytest
from names import make_full_name, extract_family_name, extract_given_name

def test_make_full_name():
    # Test case 1
    given_name = "John"
    family_name = "Doe"
    expected_result = "Doe;John"
    result = make_full_name(given_name, family_name)
    assert result == expected_result

    # Test case 2
    given_name = "Jane"
    family_name = "Smith"
    expected_result = "Smith;Jane"
    result = make_full_name(given_name, family_name)
    assert result == expected_result

def test_extract_family_name():
    # Test case 1
    full_name = "Doe; John"
    expected_result = "Doe"
    result = extract_family_name(full_name)
    assert result == expected_result

    # Test case 2
    full_name = "Smith; Jane"
    expected_result = "Smith"
    result = extract_family_name(full_name)
    assert result == expected_result

def test_extract_given_name():
    # Test case 1
    full_name = "Doe/ John"
    expected_result = "John"
    assert extract_given_name(full_name) == expected_result

    # Test case 2
    full_name = "Smith/ Jane"
    expected_result = "Jane"
    assert extract_given_name(full_name) == expected_result

    # Test case 3
    full_name = "Doe/ John/ Doe"
    expected_result = "John/ Doe"
    assert extract_given_name(full_name) == expected_result


# Run the tests using pytest
pytest.main(["-v", "--tb=line", "-rN", __file__])