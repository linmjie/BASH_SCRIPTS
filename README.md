main is the home script from which other scripts are ran
Adding arguments to main finds directories, if it can't find the directory, it tries to run the argument as a file
Example: "./main gradle init -o cat" runs "init -o cat" from inside the gradle directory
