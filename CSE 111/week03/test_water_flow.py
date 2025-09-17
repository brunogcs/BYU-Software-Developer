from waterflow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest

def test_water_column_height():
    # Test case 1
    tower_height = 0.0
    tank_height = 0.0
    expected_result = 0.0
    result = water_column_height(tower_height, tank_height)
    assert result == expected_result

    # Test case 2
    tower_height = 0.0
    tank_height = 10.0
    expected_result = 7.5
    result = water_column_height(tower_height, tank_height)
    assert result == expected_result

    # Test case 3
    tower_height = 25.0
    tank_height = 0.0
    expected_result = 25.0
    result = water_column_height(tower_height, tank_height)
    assert result == expected_result

    # Test case 4
    tower_height = 48.3
    tank_height = 12.8
    expected_result = 57.9
    result = water_column_height(tower_height, tank_height)
    assert result == expected_result

def test_pressure_gain_from_water_height():
    # Test case 1
    water_height = 0.0
    expected_pressure = 0.000
    result = pressure_gain_from_water_height(water_height)
    assert result == pytest.approx(expected_pressure, abs=0.001)

    # Test case 2
    water_height = 30.2
    expected_pressure = 295.628
    result = pressure_gain_from_water_height(water_height)
    assert result == pytest.approx(expected_pressure, abs=0.001)

    # Test case 3
    water_height = 50.0
    expected_pressure = 489.450
    result = pressure_gain_from_water_height(water_height)
    assert result == pytest.approx(expected_pressure, abs=0.001)

def test_pressure_loss_from_pipe():
    # Test case 1
    diameter = 0.048692
    length = 0.00
    friction = 0.018
    velocity = 1.75
    expected_loss = 0.000
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 2
    diameter = 0.048692
    length = 200.00
    friction = 0.000
    velocity = 1.75
    expected_loss = 0.000
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 3
    diameter = 0.048692
    length = 200.00
    friction = 0.018
    velocity = 0.00
    expected_loss = 0.000
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 4
    diameter = 0.048692
    length = 200.00
    friction = 0.018
    velocity = 1.75
    expected_loss = -113.0078
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 5
    diameter = 0.048692
    length = 200.00
    friction = 0.018
    velocity = 1.65
    expected_loss = -100.462
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 6
    diameter = 0.286870
    length = 1000.00
    friction = 0.013
    velocity = 1.65
    expected_loss = -61.576
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    assert result == pytest.approx(expected_loss, abs=0.001)

    # Test case 7
    diameter = 0.286870
    length = 1800.75
    friction = 0.013
    velocity = 1.65
    expected_loss = -110.884
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    assert result == pytest.approx(expected_loss, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])