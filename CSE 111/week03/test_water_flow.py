from waterflow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings
from waterflow import reynolds_number, pressure_loss_from_pipe_reduction, kpa_to_psi
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

def test_pressure_loss_from_fittings():
    # Test case 1
    velocity = 0.00
    quantity = 3
    expected_loss = 0.000
    result = pressure_loss_from_fittings(velocity, quantity)
    assert result == pytest.approx(expected_loss, abs=0.001)
    # Test case 2
    velocity = 1.65
    quantity = 0
    expected_loss = 0.000
    result = pressure_loss_from_fittings(velocity, quantity)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 3
    velocity = 1.65
    quantity = 2
    expected_loss = -0.109
    result = pressure_loss_from_fittings(velocity, quantity)
    assert result == pytest.approx(expected_loss, abs=0.001)

    # Test case 4
    velocity = 1.75
    quantity = 2
    expected_loss = -0.122
    result = pressure_loss_from_fittings(velocity, quantity)
    assert result == pytest.approx(expected_loss, abs=0.001)

    # Test case 5
    velocity = 1.75
    quantity = 5
    expected_loss = -0.306
    result = pressure_loss_from_fittings(velocity, quantity)
    assert result == pytest.approx(expected_loss, abs=0.001)

def test_reynolds_number():
    # Test case 1
    diameter = 0.048692
    velocity = 0.00
    expected_reynolds_number = 0
    result = reynolds_number(diameter, velocity)
    assert result == pytest.approx(expected_reynolds_number, abs=1)
    
    # Test case 2
    diameter = 0.048692
    velocity = 1.65
    expected_reynolds_number = 80069
    result = reynolds_number(diameter, velocity)
    assert result == pytest.approx(expected_reynolds_number, abs=1)
    
    # Test case 3
    diameter = 0.048692
    velocity = 1.75
    expected_reynolds_number = 84922
    result = reynolds_number(diameter, velocity)
    assert result == pytest.approx(expected_reynolds_number, abs=1)
    
    # Test case 4  
    diameter = 0.286870
    velocity = 1.65
    expected_reynolds_number = 471729
    result = reynolds_number(diameter, velocity)
    assert result == pytest.approx(expected_reynolds_number, abs=1)

    # Test case 5
    diameter = 0.286870
    velocity = 1.75
    expected_reynolds_number = 500318
    result = reynolds_number(diameter, velocity)
    assert result == pytest.approx(expected_reynolds_number, abs=1)

def test_pressure_loss_from_pipe_reduction():
    # Test case 1
    diameter = 0.28687
    velocity = 0.00
    reynolds_number = 1
    smaller_diameter = 0.048692
    expected_loss = 0.000
    result = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds_number, smaller_diameter)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 2
    diameter = 0.28687
    velocity = 1.65
    reynolds_number = 471729
    smaller_diameter = 0.048692
    expected_loss = -163.744    
    result = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds_number, smaller_diameter)
    assert result == pytest.approx(expected_loss, abs=0.001)
    
    # Test case 3
    diameter = 0.28687
    velocity = 1.75
    reynolds_number = 500318
    smaller_diameter = 0.048692
    expected_loss = -184.182
    result = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds_number, smaller_diameter)
    assert result == pytest.approx(expected_loss, abs=0.001)

def test_kpa_to_psi():
    # Test case 1:
    kpa = 0
    result = kpa_to_psi(kpa)
    expected_result = 0.0
    assert result == pytest.approx(expected_result, abs=0.001)

    # Test case 2:
    kpa = 1
    result = kpa_to_psi(kpa)
    expected_result = 0.145
    assert result == pytest.approx(expected_result, abs=0.001)

    # Test case 3:
    kpa = 101.325
    result = kpa_to_psi(kpa)
    expected_result = 14.696
    assert result == pytest.approx(expected_result, abs=0.001)

    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])