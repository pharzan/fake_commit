# Fake Commit
A git fake commit generator to make those github squares green.

This simple script generates a linux shell script which in turn creates random number of *empty git commits* 
in desired number of days from now.

## Usage:

Create an empty repository.

Install the python dependecies.
```
pip install -r requirements.txt

pip3 install -r requirements.txt #if you're using pip3
```
Run the script.
```
python fake_commit.py
```
The script needs three parameters to run correctly:
__github user name__, __repository name__, __number of days to go back__

* Make sure the repository name is the same as the empty repository you created before running the script.
* A random number is generated in the script which is hard coded and needs to be the maximum number of commits you have,
so if your maximum commits is 50, you should change the random number interval from 1,20 to 30,50. This is because 
the square color darkness indicates the maximum number of commits you've made.
* It may take up to a few minutes to generate and do the commits.


