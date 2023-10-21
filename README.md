[![Continuous Integration Test](https://github.com/nogibjj/RustProc_YCLiu/actions/workflows/CICD.yml/badge.svg)](https://github.com/nogibjj/RustProc_YCLiu/actions/workflows/CICD.yml)

## Compare Processing Speed of Rust and Python 

This repository compares the processing speed of Rust and python by **getting the sum of _1 million_ integers**.

Below is an overview of the files in this project:

1. **Main functions Rust Python Speed Comparison**
   <br>a. _main.py_: create a list of integers from 1 to 1,000,000, output the sum, and processing time. Below is the result.
```
Added 1,000,000 numbers within 0.0318 seconds
```
   <br>b. _DataProc/src/_main.rs_: create a list of integers from 1 to 1,000,000, output and test the sum, and processing time. Below is the result.
```
Added 1,000,000 numbers within 9.466237ms
```
From the results above, we can see that **rust processed this 1,000,000 datapoints around _3.5 times faster_ than python**
 
3. **Testing Functions**
   <br>c. _test_main.py_: test the output sum of main.py.
   
4. **Github actions setup for continuous integration**
  <br>d. _.github/workflows/cicd.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

5. **Other files for development environment settings**
  <br>e. _.devcontainer_: set up the environment for development.
  <br>f. _.gitignore_: specify file names to ignore.
  <br>g. _requirements.txt_: list required packages for the project.

6. **Description of the project**
   <br>h. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


