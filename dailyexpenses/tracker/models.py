from django.db import models


class ExpensesTracker(models.Model):
    name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(
        max_length=10,
        choices=[
            # Weight
            ("mg", "Milligrams"),
            ("g", "Grams"),
            ("kg", "Kilograms"),
            # Volume
            ("ml", "Milliliters"),
            ("l", "Liters"),
            # Length
            ("mm", "Millimeters"),
            ("cm", "Centimeters"),
            ("m", "Meters"),
            ("km", "Kilometers"),
            # Count
            ("pcs", "Pieces"),
            ("dozen", "Dozen"),
            ("nos", "nos"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    pay_type = models.CharField(
        max_length=50, choices=[("CASH", "Cash"), ("ONLINE", "Online")]
    )

    category = models.CharField(
        max_length=50,
        choices=[
            ("food", "Food & Dining"),
            ("travel", "Travel"),
            ("shopping", "Shopping"),
            ("bills", "Bills & Utilities"),
            ("health", "Health"),
            ("entertainment", "Entertainment"),
            ("education", "Education"),
            ("other", "Other"),
        ],
    )

    @property
    def total(self):
        return self.price * self.quantity
