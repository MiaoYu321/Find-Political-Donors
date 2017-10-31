# README for `find-political-donors`

Author: [Miao Yu](https://www.linkedin.com/in/miao-yu-4728a0126/)

## Input Checking
The inpunt checking is implemented according to [Input file considerations](https://github.com/InsightDataScience/find-political-donors#input-file-considerations).

## Some remarks on implementation
1. Data processing is separated for `medianvals_by_zip.txt` and `medianvals_by_date.txt`. Because the data that should be ignored when calculating median by zip and by data are different.

2. Date info is stored in the standard python datetime format for sorting convenience.

3. To let the `medianvals_by_date.txt` "sorted alphabetical by recipient and then chronologically by date." I use some auxiliary variables: `recipient_list_sorted` and `date_list_sorted` to store the sorted variables. For loop is conduct as the sorted order, and index is use to get the correponding data. 

4. `date_str_matrix` is a copy of `date_matrix` but in `string` format for output.

5. `find-political-donors.py` is a standalone function with three input file: `itcont.txt`, `medianvals_by_zip.txt`, and `medianvals_by_date.txt`. The last two specify the path for the output files.

6. `main.py` is the real enterance for the program. It get input from terminal and prepare input for the `find-political-donors` function. In short, `main.py` is a wrapper program.


## Further consideration
1. The code is not optimized for efficiency for simplicity. Further optimization can be achieved in the following paradigm:
* Calculate median value by zip by updating instead of re-calculate at each iteration.
* Other data structure might be more efficient than `List`.