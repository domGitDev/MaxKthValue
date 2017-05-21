import unittest
from max_kth_value import find_max_kth_value


class MaxKthValueTest(unittest.TestCase):
	
	def test_find_max_kth_value(self):
		data = [2, 1, 3, 1, 2, 9, 6]
		val = find_max_kth_value(data, 1)
		print '\n', val
		self.assertEqual(9, val)

		val = find_max_kth_value(data, 3)
		print val
		self.assertEqual(3, val)
		
	def test_find_max_kth_value_badtype(self):
		with self.assertRaises(TypeError):
			data = '1 3 4 10 6'
			find_max_kth_value(data, 2)
			
			data = [2, 6, 3]			
			find_max_kth_value(data, 2.5)



suite = unittest.TestLoader().loadTestsFromTestCase(MaxKthValueTest)
unittest.TextTestRunner(verbosity=2).run(suite)
