from django.urls import path
from .views import ExpensesTrackerlistView, ExpensesTrackerCreateView


urlpatterns = [
    path("", ExpensesTrackerlistView.as_view(), name="list"),
    path('create/', ExpensesTrackerCreateView.as_view(), name='create'),
]
