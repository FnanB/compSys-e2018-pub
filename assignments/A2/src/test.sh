#!/usr/bin/env bash

# Exit immediately if any command below fails.
set -e

make

# Test programs written in x86prime are expected to be located in a subdirectory called test_programs.
#   The file extension of the files are ".s"
#    TODO: Make more tests there

# The command with which you run x86prime
X86PRIME=x86prime
# The name of the function to run in the following is "runtest"
TESTMAIN=runtest


echo "Generating a test_files directory.."
mkdir -p test_runs
rm -f test_runs/*


echo "Running the tests.."
exitcode=0
for f in test_programs/*.s; do
  echo ">>> Testing ${f} ..."
  fname=${f#"test_programs/"}
  fname=${fname%".s"}

  ${X86PRIME} -f ${f} -asm -list > test_runs/${fname}.hex
  ${X86PRIME} -f ${f} -asm -run ${TESTMAIN} -tracefile test_runs/${fname}.trc
  ./sim test_runs/${fname}.hex 0 test_runs/${fname}.trc
done

exit $exitcode
