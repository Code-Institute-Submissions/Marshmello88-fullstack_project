from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = 'catalog'

class CategoryConfig(AppConfig): #to be added here also or no?
    name = "Category"
    verbose_name = "Categories"