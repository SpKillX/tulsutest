package main

import (
	"encoding/json"
	"os"
)

type Input struct {
	Numbers []int `json:"numbers"`
}
type Output struct {
	Sum int `json:"sum"`
}

func main() {
	var input Input
	json.NewDecoder(os.Stdin).Decode(&input)

	sum := 0
	for _, n := range input.Numbers {
		sum += n * n
	}

	output := Output{Sum: sum}
	json.NewEncoder(os.Stdout).Encode(output)
}
