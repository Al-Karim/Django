from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Edit
from .forms import EditForm
from django.contrib.auth import login
from django.views.generic.base import View
from django.contrib.auth import logout
import os
import pdfkit
path_wkhtmltopdf = r'\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def main_page(request): # создаем функцию для отображения нужной страницы
    return render(request, 'htmls/main_page.html')

def log_out1(request): # создаем функцию для отображения нужной страницы
    return render(request, 'htmls/log_out.html')

def sign_in(request):
    return render(request, 'htmls/sign_in.html')

def download(request):
    if request.method == 'POST':
        print(os.listdir())
        with open('accounts/templates/htmls/download_resume.html') as file:
            pdfkit.from_file(file, 'out.pdf')

    return render(request, 'htmls/download_resume.html')

# def register(request):
#     # form = UserCreationForm(request.POST)
#     # if form.is_valid():
#     #     user = form.save()
#     #     return render(request, 'htmls/sign_in.html')
#     #
#     #
#     # context = {'form': form}
#     return render(request, 'htmls/register.html')

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "htmls/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "htmls/sign_in.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return render(request, 'htmls/main_page.html')

def sug_edit(request):
    data = [i for i in Edit.objects.all()]
    username = request.user
    idx = -1
    print(username)
    for i in range(len(data)):
        if str(data[i]) == str(username):
            idx = i
            break
    if request.method == 'POST':
        if idx != -1:
            print(data[idx].get_value())
            form = EditForm(data[idx].get_value(), request.POST)
        else:
            form = EditForm(request.POST)
        return render(request, 'htmls/dispatch_ok.html')
    if idx != -1:
        form = EditForm(data[idx].get_value())
    else:
        form = EditForm(['', '', '', '', '', ''])
    context = {'form': form}

    return render(request, 'htmls/sug_edit.html', context)


