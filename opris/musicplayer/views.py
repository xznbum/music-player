from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.
def index(request):
    return render_to_response("index.html",
            context_instance=RequestContext(request))


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # TODO: !!!!!!!!
            # user.save()
            # newuser = auth.authenticate(username=newuser_form.clean_username(), password=newuser_form.clean_password2())
            # auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = form
    return render_to_response('registration/register.html', args, RequestContext(request))