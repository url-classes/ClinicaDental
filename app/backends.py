from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class UsuarioBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            usuario = Usuario.objects.get(nombre_usuario=username)
            if usuario.check_password(password):
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(idusuario=user_id)
        except Usuario.DoesNotExist:
            return None
