from modeltranslation.translator import translator, TranslationOptions

from core.models import(
      Category,
      
      News,
      Product,
      Contact,      
      
)

class NewsTranslationOptions(TranslationOptions):
      fields = ("title", "content",)
      
class CategoryTranslationOptions(TranslationOptions):
      fields = ("title",)

class ProductTranslationOptions(TranslationOptions):
      fields = ("title", "content",)

class ContactTranslationOptions(TranslationOptions):
      fields = ('name', 'email', 'message')
      
translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Contact, ContactTranslationOptions)