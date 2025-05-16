from django import template
from django.http import HttpResponseForbidden

register = template.Library()

@register.filter(name='has_permiso')
def has_permiso(user, permiso_requerido):
    if not user.is_authenticated:
        return False
    
    # Si es superusuario, tiene todos los permisos
    if user.is_superuser:
        return True
    
    # Verificar permisos del tipo_usuario
    if hasattr(user, 'tipo_usuario_idtipo_usuario') and user.tipo_usuario_idtipo_usuario.permisos:
        permisos_usuario = [p.strip() for p in user.tipo_usuario_idtipo_usuario.permisos.split(',')]
        return permiso_requerido in permisos_usuario
    
    return False