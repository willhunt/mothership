from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.authtoken.models import Token
from .forms import UserForm


def index(request):
    return HttpResponse("<h1>How did you get here?</h1>")


class UserFormView(View):
    # Choose form blueprint
    form_class = UserForm # Use form created in forms.py
    template_name = 'userControl/registration_form_MDL.html'

    # Display blank form for new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Create user object from form but not saved to database
            user = form.save(commit=False)
            # Clean and normalise data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #Returns user object if credentials are correct
            user = authenticate(username=username, password=password)
            # Check if user is in database
            if user is not None:
                # Check user is not banned/disabled
                if user.is_active:
                    login(request,user)
                    # Redirect to homepage after succesful login
                    return redirect('main:index')

        return render(request, self.template_name, {'form': form})


class UserUpdateView(UpdateView):
    # Automatically will render <modelname>_form.html
    model = User
    form_class = UserForm
    template_name = 'userControl/registration_form.html'

    def get_object(self, queryset=None):
        # Hook to ensure object is owned by request.user
        object = super(UserUpdateView, self).get_object()
        if not object == self.request.user:
            raise Http404
        return object


class UserDeleteView(DeleteView):
    model= User
    success_url = reverse_lazy('main:index')

    def get_object(self, queryset=None):
        # Hook to ensure object is owned by request.user
        object = super(UserDeleteView, self).get_object()
        if not object == self.request.user:
            raise Http404
        return object


def user_login(request):
    template_name = 'userControl/login.html'

    # Display blank form for new user
    if request.method == 'GET':
        return render(request, template_name)

    # Process form data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # Check if user is in database
        if user is not None:
            # Check user is not banned/disabled
            if user.is_active:
                login(request,user)
                # Redirect to homepage after succesful login
                return redirect('main:index')
        else:
            error_message = 'Username or password not recognised'
            return render(request, template_name, {'error_message': error_message})



def user_logout(request):
    logout(request)
    return redirect('main:index')


class UserDetailView(DetailView):
    ''' View showing user accoutn information '''
    #model = User
    template_name = 'userControl/user_detail.html'
    # Override get method to allow username in url
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        # Call base implementation first tp get context
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # Get current user
        user = User.objects.filter(username=self.kwargs.get("username"))
        # Add in a QuerySet of API tokens
        context['api_tokens'] = Token.objects.filter(user=user)
        return context


class CreateApiTokenView(View):

    def post(self, request, *args, **kwargs):
        # Check for existing user token and delete
        if Token.objects.filter(user=request.user):
            Token.objects.filter(user=request.user).delete()
        Token.objects.create(user=request.user)
        redirect_url = reverse('userControl:user-detail', kwargs={'username': request.user.username})
        return HttpResponseRedirect(redirect_url)




