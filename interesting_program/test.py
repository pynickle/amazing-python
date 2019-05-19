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


class Test(unittest.TestCase):
	def test(self):
		stub_stdin(self, '24\n30\n')
		stub_stdout(self)
		lcm_test()
		#print("first:",sys.stdout.getvalue())
		self.assertEqual(sys.stdout.getvalue(), '120\n')
		
		stub_stdin(self, '24\n30\n')
		stub_stdout(self) # 重置输出
		mcd_test()
		#print("second:",sys.stdout.getvalue())
		self.assertEqual(sys.stdout.getvalue(), '6\n')

unittest.main()
