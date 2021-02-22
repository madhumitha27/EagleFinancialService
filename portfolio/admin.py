import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Customer, Investment, Stock

class ExportCsvMixin ( object ) :
    def export_as_csv( self, request, queryset ):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer (response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj,field) for field in field_names])
        return response
    export_as_csv.short_description= "Export Selected as  CSV"

class InvestmentExportCsvMixin ( object ) :
    def export_as_csv( self, request, queryset ):
        meta = self.model._meta
        field_names = ['Customer','Category','Description','Acquired Value','Acquired Date','Recent Value','Recent Date']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer (response)
        writer.writerow(field_names)
        for investment in queryset :
            writer.writerow ([investment.customer , investment.category,investment.description,
                              investment.acquired_value,investment.acquired_date.strftime ( "%d-%m-%Y %H:%M:%S" ),
                               investment.recent_value,investment.recent_date.strftime ( "%d-%m-%Y %H:%M:%S" )])
        return response
    export_as_csv.short_description= "Export Selected as  CSV"

class StockExportCsvMixin ( object ) :
    def export_as_csv( self, request, queryset ):
        meta = self.model._meta
        field_names = ['Customer','Symbol','Name','Shares','Purchase Price','Purchase Date']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer (response)
        writer.writerow(field_names)
        for stock in queryset :
            writer.writerow ( [stock.customer , stock.symbol,stock.name,stock.shares,stock.purchase_price,
                               stock.purchase_date.strftime ( "%d-%m-%Y %H:%M:%S" )])
        return response
    export_as_csv.short_description= "Export Selected as  CSV"

class CustomerList(admin.ModelAdmin,ExportCsvMixin):
    list_display = ('cust_number', 'name', 'city', 'cell_phone')
    list_filter = ('cust_number', 'name', 'city')
    search_fields = ('cust_number', 'name')
    ordering = ['cust_number']
    actions = ["export_as_csv"]


class InvestmentList(admin.ModelAdmin,InvestmentExportCsvMixin):
    list_display = ('customer', 'category', 'description', 'recent_value')
    list_filter = ('customer', 'category')
    search_fields = ('customer', 'category')
    ordering = ['customer']
    actions = ["export_as_csv"]

class StockList(admin.ModelAdmin,StockExportCsvMixin):
    list_display = ('customer','symbol', 'name', 'shares', 'purchase_price')
    list_filter = ('customer','symbol', 'name')
    search_fields = ('customer','symbol', 'name')
    ordering = ['customer']
    actions = ["export_as_csv"]

admin.site.register(Customer, CustomerList)
admin.site.register(Investment, InvestmentList)
admin.site.register(Stock, StockList)


