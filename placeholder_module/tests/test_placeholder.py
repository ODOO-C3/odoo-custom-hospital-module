from odoo.tests.common import TransactionCase


class TestPlaceholder(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Placeholder = self.env["placeholder_module.placeholder_module"]

    def test_value_computation(self):
        record = self.Placeholder.create(
            {
                "name": "Test Record",
                "value": 150,
            }
        )
        self.assertEqual(
            record.value2, 1.5, "The computed value2 should be value / 100"
        )

        record.write({"value": 200})
        self.assertEqual(
            record.value2, 2.0, "The computed value2 should update when value changes"
        )
