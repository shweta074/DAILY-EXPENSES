from django.contrib import admin
from tracker.models import ExpensesTracker


class ExpensesTrackerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "product_name",
        "price",
        "quantity",
        "total",
        "created_at",
        "pay_type",
        "category",
    )


admin.site.register(ExpensesTracker, ExpensesTrackerAdmin)
