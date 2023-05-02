from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html,urlencode
from django.db.models.aggregates import Count
from .models import Collection,Promotion,Product,Customer,Order,OrderItem,Address,Cart,CartItem

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title','featured_product','products_count')

    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}>{}</a>',url,collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

    

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('description','discount','discount_applicable')
    list_editable = ('discount',)
    ordering = ['description','discount'] #this is for ordering list
    list_per_page = 25

    # @admin.display(ordering='discount') # this is for ordering on method
    def discount_applicable(self,promotion):
        if promotion.discount > 30:
            return 'Not Applicable'
        return 'Applicable'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','description','price','inventory','last_update','collection_title')
    list_editable = ['price']
    list_select_related = ['collection']
    list_filter = ['collection','last_update']
    list_per_page = 25

    def collection_title(self,product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','phone','birth_date','membership','orders')
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 5
    search_fields = ['first_name','last_name']

    @admin.display(ordering='orders')
    def orders(self,customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            })
        )
        print(url)
        return format_html('<a href={}>{}</a>',url,customer.orders_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('placed_at','payment_status','customer')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity','unit_price')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street','city','customer')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('created_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity')
