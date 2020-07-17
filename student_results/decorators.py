from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthenticated_usered(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):    
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':        
            return redirect('userPage')
        if group == 'primary':
            return view_func(request, *args, **kwargs)
        if group == 'secondary':
            return view_func(request, *args, **kwargs)
        if group == 'techschool':
            return view_func(request, *args, **kwargs)
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function


def access_permissions(permission):
    """ django‐rest‐framework permission decorator for custom methods """
    def decorator(drf_custom_method):
        def _decorator(self, *args, **kwargs):
            usered_permission = str(kwargs['id'])+permission
            if self.request.usered.has_perm(usered_permission):
                return drf_custom_method(self, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return _decorator
    return decorator   