from django import template

register = template.Library()

@register.simple_tag
def has_permission(user, permission_codename):
    return user.has_perm(permission_codename) or user.is_superuser