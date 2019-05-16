#!/usr/bin/env bash
# Run tests

# echo path
echo $DIR, `pwd`

# execute specified tests
py.test `pwd`/study_program/test.py