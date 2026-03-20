import pytest
from call import run_go_calculator

@pytest.mark.parametrize("input_list, expected_sum", [
    ([1, 2, 3], 14),        # 1^2 + 2^2 + 3^2 = 1+4+9 = 14
    ([0, 5], 25),           # 0^2 + 5^2 = 25
    ([1, 1, 1, 1], 4),      # 1+1+1+1 = 4
    ([], 0)                 # Пустой список
])
def test_calculator_logic(input_list, expected_sum):
    result = run_go_calculator(input_list)
    
    assert "sum" in result
    assert result["sum"] == expected_sum

def test_calculator_file_exists():
    import os
    assert os.path.exists("./calculator.exe"), "Файл calculator.exe не найден!"