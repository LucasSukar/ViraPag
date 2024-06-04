from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import Categoria
from mainapp import admin
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Cria dados de teste para Cypress: Professor, Turma, Disciplina e Aluno'
    def handle(self, *args, **kwargs):
        try:
            categoria1 = Categoria.objects.create(nome='teste 1')
            categoria2 = Categoria.objects.create(nome='teste 2')

            self.stdout.write(self.style.SUCCESS('Categorias criadas'))
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Erro de integridade, os seguintes dados ja existem no banco de dados: {str(e)}'))