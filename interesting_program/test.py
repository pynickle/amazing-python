import sys
import io
import unittest


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin
    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)

def stub_stdout(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()

def test_import(slf, file, result, input_value = None):
	if input is not None:
		stub_stdin(slf, input_value)
	stub_stdout(slf)
	exec("import " + file)
	slf.assertEqual(sys.stdout.getvalue(), result)

class Test(unittest.TestCase):
	def test(self):
		test_import(self, "fibonacci", "1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n")
		test_import(self, "24\n30\n", "lcm", "120\n")
		test_import(self, "24\n30\n", "mcd", "6\n")
		test_import(self, "2000\n", "leap_year", True)
		
unittest.main()
