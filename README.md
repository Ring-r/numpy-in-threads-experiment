# python threads and numpy experiment

there is an experiment to check if code with python multithreading works parallel when using numpy


## motivation

I hear and read that GIL is used only for Python Virtual Machine. It isn't used for external code.
And it is interesting to check if it is right and if it brings benefits.


## environment

- gnu/linux
- python
- poetry


# results

I'v run scripts several times and select minimal.

There is result for code without using threads:
```shell
$ time python ./app.py
10000000000

real	0m5.698s
user	0m4.566s
sys	0m1.827s
```

There is result for code with using threads:
```shell
$ time python ./app.py 4
10000000000

real	0m2.961s
user	0m5.724s
sys	0m1.891s
```
