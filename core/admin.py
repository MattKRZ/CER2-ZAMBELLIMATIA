from django.contrib import admin
from .models import Entidades, Comunicado

class PublicadoYModificado(admin.ModelAdmin):
    readonly_fields = ('publicado_por', 'modificado_por', 'entidad',)
    
    def save_model(self, request, obj, form, change):
        usuario = request.user
        if not obj.publicado_por:
            obj.publicado_por = usuario
        obj.modificado_por = usuario

        entidades = Entidades.objects.filter(admin=usuario).first()
        obj.entidad = entidades
        super(PublicadoYModificado, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        query = super(PublicadoYModificado, self).get_queryset(request)
        if not request.user.is_superuser:
            query = query.filter(publicado_por = request.user)
        return query

admin.site.register(Entidades)
admin.site.register(Comunicado, PublicadoYModificado)