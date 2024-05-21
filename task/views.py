from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Usuario,Cliente,Processo
from django.contrib.auth import get_user_model

# APAGAR DEF LOGIN

def autenticar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print('autenticado')
            return redirect(reverse('processos')) # MUDEI COLOCAR HOME
        else:
            messages.error(request, "Email ou senha incorretos.")
            return render(request, 'tasks/index.html')

    return render(request, 'tasks/index.html')

def cadastrar_usuario(request):
    return render(request,'tasks/cadastro.html')


def adicionar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')

        if password != confirmar_senha:
            return render(request, 'tasks/cadastro.html')

        Usuario = get_user_model()
        try:
            novo_usuario = Usuario.objects.create_user(
                email=email, nome=nome, password=password)
            return redirect('login')
        except Exception as e:
            return render(request, 'tasks/cadastro.html')
    else:
       return render(request, 'tasks/cadastro.html')


def cliente(request):
    return render(request, 'tasks/cliente.html')


def adicionar_cliente(request):
    if request.method == 'POST':
        print("Método POST recebido.")
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        data_nascimento = request.POST.get('data_nascimento')
        contato = request.POST.get('contato')
        email = request.POST.get('email')
        genero = request.POST.get('genero')
        whatsapp = request.POST.get('whatsapp')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero_casa = request.POST.get('numero_casa')
        bairro = request.POST.get('bairro')

        # Verificação e conversão do campo numero_casa
        try:
            numero_casa = int(numero_casa)
        except (ValueError, TypeError):
            print("Número da casa inválido.")
            return render(request, 'tasks/processos.html')

        try:
            novo_cliente = Cliente(
                nome=nome,
                cpf=cpf,
                rg=rg,
                data_nascimento=data_nascimento,
                contato=contato,
                email=email,
                genero=genero,
                whatsapp=whatsapp,
                cep=cep,
                logradouro=logradouro,
                numero_casa=numero_casa,
                bairro=bairro
            )
            novo_cliente.save()
            print("Deu certo")
            # Substitua 'success_page' pelo nome correto da URL de sucesso
            return redirect('logar')

        except Exception as e:
            print("Algo deu errado:", e)
            return render(request, 'tasks/cliente.html')

    else:
        print("Nem tentou")
        return render(request, 'tasks/cliente.html')
    
def adicionar_processo(request):
    if request.method == 'POST':
        numero_processo = request.POST.get('numero_processo')
        autor = request.POST.get('autor')
        reu = request.POST.get('reu')
        instancia = request.POST.get('instancia')
        forum = request.POST.get('forum')
        valor_da_causa = request.POST.get('valor_da_causa')
        assunto = request.POST.get('assunto')
        cliente_cpf = request.POST.get('cliente')

        cliente = Cliente.objects.get(cpf=cliente_cpf)

        processo = Processo(
            numero_processo=numero_processo,
            autor=autor,
            reu=reu,
            instancia=instancia,
            forum=forum,
            valor_da_causa=valor_da_causa,
            assunto=assunto,
            cliente=cliente
        )
        processo.save()
    
    
    
def processo(request):
    return render(request, 'tasks/processos.html')


def tarefas(request):
    return render(request, 'tasks/tarefas.html')

    return render(request, 'tasks/tarefas.html')
