from django.http import HttpResponseRedirect


def is_CCO(function):
    def wrap(request, *args, **kwargs):

        logged_in_user = request.user
        id 

        if logged_in_user.designation.name == "CCO":
                return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def is_base_staff_status(function):
    def wrap(request, *args, **kwargs):

        logged_in_user = request.user
        id 

        if logged_in_user.designation.name == "CCO":
                return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/")

       

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap