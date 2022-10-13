# TP-HSE-2022-HW
![workflow](https://github.com/evgenius1544/tp-hse-2022-hw/actions/workflows/github-actions-demo.yml/badge.svg)
![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

## Usage

- Run application
```shell
python3 main.py test_my_own_values.txt 
```

- Run tests
```shell
python3 test.py
```

- Run generator for speed test
```shell
python3 test_generator.py
```

- Run tests for checking work time dependence of elements
```shell
python3 test_work_time.py
``` 

> Graph of the dependence of the execution time on the number of numbers in the file; `x - elements, y - time`.

![](test_work_time_result.png)

## Results
- Realised tests for all function: min, max, sum, mult. 
- Also created own test for reading function.
- Used type hint, read doc strings and used python standard library: functools, unittest, os, sys.
- Processed some actions in friendly form when user don't upload file or file doesn't exist.
- Created own test generator.
- Built graph of the dependence time and elements.