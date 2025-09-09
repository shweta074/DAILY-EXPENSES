from .models import ExpensesTracker
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.db.models import Sum, F



class ExpensesTrackerlistView(ListView):
    model = ExpensesTracker
    template_name = "list.html"
    context_object_name = "ExpensesTracker"

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get("date")
        category = self.request.GET.get("category")
        if date:
            queryset = queryset.filter(create__date=date)
        if category:
            queryset = queryset.filter(category=category)
        return queryset
            
        
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        total = self.get_queryset().aggregate(total_sum=Sum(F("price") * F("quantity")))
        data["total"] = total["total_sum"]
        return data


class ExpensesTrackerCreateView(CreateView):
    model = ExpensesTracker
    template_name = "create.html"
    fields = "__all__"
    success_url = reverse_lazy("list")
