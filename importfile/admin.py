from django.contrib import admin

# Register your models here.

from importfile.models import Plants, Order, OrderPlants
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView

from importfile.models import Order
from django.urls import path, reverse
from django.utils.html import format_html
# Register your models here.


@admin.register(Plants)
class PlantsAdmin(admin.ModelAdmin):
    list_display = ['breed', 'quantity']


class OrderPlantsInline(admin.TabularInline):
    model = OrderPlants


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created', 'detail']
    inlines = [OrderPlantsInline]

    def get_urls(self):
        return [
            path(
                "<pk>/detail",
                self.admin_site.admin_view(OrderDetailView.as_view()),
                name=f"Plants_order_detail",
            ),
            *super().get_urls(),
        ]

    def detail(self, obj: Order) -> str:
        url = reverse("admin:Plants_order_detail", args=[obj.pk])
        return format_html(f'<a href="{url}">📝</a>,farmerinfo')


@admin.register(OrderPlants)
class OrderPlantsAdmin(admin.ModelAdmin):
    list_display = ['order', 'Plants', 'count']


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "Plants.view_order"
    template_name = "admin/Plants/Order/detail.html"
    model = Order

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
        }
