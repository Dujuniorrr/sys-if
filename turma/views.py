from django.shortcuts import render
from turma.models import Turma, Avaliacao, TurmaAluno
from aluno.models import Aluno
from django.contrib.auth.decorators import login_required

# views para turma
@login_required
def cadastrar_turma(request):
   
    context = Turma.cadastrar(request) #Durval - aqui eu chamo a função de cadastro de turma, a ordem de negócio se encontra lá
        
    return render(request, 'cadastrar_turma.html', context)

@login_required
def editar_turma(request, id):
   
    context = Turma.editar(request, id) #Durval - aqui eu chamo a função de editar turma, a ordem de negócio se encontra lá
        
    return render(request, 'editar_turma.html', context)

@login_required
def deletar_turma(request, id):
   
    context = Turma.deletar(request, id) #Durval - aqui eu chamo a função de deletar turma, a ordem de negócio se encontra lá
        
    return render(request, 'deletar_turma.html', context)

@login_required
def dashboard_turma(request):
    
     turmas_cadastradas = Turma.objects.all()
    
     context ={
        'turmas_cadastradas': turmas_cadastradas,
     }

     return render(request, 'turma_dashboard.html', context)
 
#----------------------------------------------------------

# views para avaliacao
@login_required
def lancar_avaliacao(request):
   
    context = Avaliacao.lancar(request) #Durval - aqui eu chamo a função de cadastro de avaliacao, a ordem de negócio se encontra lá
        
    return render(request, 'lancar_avaliacao.html', context)

@login_required
def editar_avaliacao(request, id):
   
    context = Avaliacao.editar(request, id) #Durval - aqui eu chamo a função de editar avaliacao, a ordem de negócio se encontra lá
        
    return render(request, 'editar_avaliacao.html', context)

@login_required
def deletar_avaliacao(request, id):
   
    context = Avaliacao.deletar(request, id) #Durval - aqui eu chamo a função de deletar avaliacao, a ordem de negócio se encontra lá
        
    return render(request, 'deletar_avaliacao.html', context)

@login_required
def dashboard_avaliacao(request):
    
     avaliacoes_lancadas = Avaliacao.objects.all()
    
     context ={
        'avaliacoes_lancadas': avaliacoes_lancadas,
     }

     return render(request, 'avaliacao_dashboard.html', context)

@login_required
def alocar_aluno(request):
    context = TurmaAluno.alocar_aluno(request)

    return render(request, 'alocar_aluno.html', context)

@login_required
def ver_alunos(request, id):

    turma = Turma.objects.get(id = id)

    alunos_alocados = TurmaAluno.objects.filter(id_turma = id)

    context = {
        'alunos_alocados': alunos_alocados,
    }

    context ['turma'] = turma

    return render(request, 'ver_alunos.html', context)

@login_required
def retirar_alunos(request, id, idt):

    context = TurmaAluno.retirar_alunos(request, id, idt)

    return render(request,'retirar_alunos.html', context)

    
 