import subprocess
import json

def run_go_calculator(numbers):
    proc = subprocess.Popen(
        ["./calculator"], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    input_data = json.dumps({"numbers": numbers})
    
    stdout, stderr = proc.communicate(input=input_data.encode())
    
    if stdout:
        return json.loads(stdout.decode())
    return stderr.decode()

result = run_go_calculator([1, 2, 3, 4, 5])
print(f"Result Go: {result['sum']}")