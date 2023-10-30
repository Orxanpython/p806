from modeltranslation.translator import translator, TranslationOptions

from core.models import *

class NewsTranslationOptions(TranslationOptions):
      fields = ("title", "content",)
      
class CategoryTranslationOptions(TranslationOptions):
      fields = ("title",)

class ProductTranslationOptions(TranslationOptions):
      fields = ("title", "content",)

class ContactTranslationOptions(TranslationOptions):
      fields = ('name', 'email', 'message')
      
      
class TagTranslationOptions(TranslationOptions):
      fields = ("title",)
      
      
translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
translator.register(Tag, TagTranslationOptions)