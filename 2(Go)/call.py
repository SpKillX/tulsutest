import subprocess
import json
import os
import sys

def run_go_calculator(numbers):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    executable_path = os.path.join(current_dir, "calculator.exe")
    
    if not os.path.exists(executable_path):
        raise FileNotFoundError(f"Не найден файл по пути: {executable_path}")

    proc = subprocess.Popen(
        [executable_path], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    input_data = json.dumps({"numbers": numbers})
    stdout, stderr = proc.communicate(input=input_data.encode())
    
    if stderr:
        print(f"Ошибка Go: {stderr.decode()}", file=sys.stderr)
        
    return json.loads(stdout.decode())

result = run_go_calculator([1, 2, 3, 4, 5])
print(f"Result Go: {result['sum']}")