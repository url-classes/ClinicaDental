from django.http import HttpResponseForbidden
from functools import wraps

def user_has_permisos(permisos_requeridos):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("No estás autenticado.")
            
            tipo_usuario = request.user.tipo_usuario_idtipo_usuario
            
            if tipo_usuario and tipo_usuario.permisos:
                permisos_usuario_lista = [permiso.strip() for permiso in tipo_usuario.permisos.split(',')]
                if all(permiso.strip() in permisos_usuario_lista for permiso in permisos_requeridos):
                    return view_func(request, *args, **kwargs)
            
            return HttpResponseForbidden("No tienes permiso para acceder a esta sección.")
        return _wrapped_view
    return decorator
