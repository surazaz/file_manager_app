from django.contrib import admin
# from pinax.document import *
from pinax.documents.models import *
# from django.apps import apps
# print(apps)
# models=pinax.documents.models.get_models()
# print(models)
# admin.site.register(models)


admin.site.register(Folder)
admin.site.register(UserStorage)
admin.site.register(DocumentSharedUser)
admin.site.register(FolderSharedUser)
# admin.site.register(MemberSharedUser)
admin.site.register(Document)

# Register your models here.
