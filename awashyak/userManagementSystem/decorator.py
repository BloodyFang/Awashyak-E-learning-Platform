
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

# This method helps to kicks authenticates users out of a view which are not allowed
# to visit who are authenticated.
def login_excluded(redirect_to):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper
        