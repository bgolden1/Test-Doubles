import unittest
from unittest.mock import MagicMock
from main import Program2


class TestProgram2(unittest.TestCase):
    #none
    def test_init_customers(self):
        program2 = Program2()
        self.assertIsNotNone(program2.customers)

    #none
    def test_init_orders(self):
        program2 = Program2()
        self.assertIsNotNone(program2.orders)

    #mock
    def test_create_simple_customer(self):
        program2 = Program2()
        program2.customers.insert_one = MagicMock()
        program2.create_customer(_id='1', name='Person', num_goods_purchased=5)
        program2.customers.insert_one.assert_called_once_with({'_id': '1', 'name': 'Person', 'num_goods_purchased': 5})

    #stub
    def test_create_customer_invalid_id(self):
        program2 = Program2()
        program2.customers.insert_one = MagicMock()
        with self.assertRaises(TypeError):
            program2.create_customer(_id=1, name='Person', num_goods_purchased=5)

    #stub
    def test_create_customer_invalid_goods_purchased(self):
        program2 = Program2()
        program2.customers.insert_one = MagicMock()
        with self.assertRaises(TypeError):
            program2.create_customer(_id='1', name='Person', num_goods_purchased=5.5)

    #mock
    def test_create_simple_order(self):
        program2 = Program2()
        program2.orders.insert_one = MagicMock()
        program2.create_order(customer_id='1', num_goods_purchased=5)
        program2.orders.insert_one.assert_called_once_with({'customer_id': '1', 'num_goods_purchased': 5})

    #stub
    def test_get_customers(self):
        program2 = Program2()
        program2.customers.find = MagicMock(return_value=[{'_id': '1', 'name': 'Person', 'num_goods_purchased': 5}])
        actual = program2.get_customers()
        expected = [{'_id': '1', 'name': 'Person', 'num_goods_purchased': 5}]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
