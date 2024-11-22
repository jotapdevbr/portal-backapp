from rest_framework import viewsets, status
from .models import Link, Programa, Manual
from .serializers import LinkSerializer, ProgramaSerializer, ManualSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

class ManualViewSet(viewsets.ModelViewSet):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer

@csrf_exempt
def create_link(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body) 
            # Verifica se os campos necessários estão no corpo da requisição
            if 'nome' not in data or 'url' not in data or 'departamento' not in data or 'descricao' not in data:
                return JsonResponse({"error": "Campos faltando"}, status=400)
            
            # Cria o link
            Link.objects.create(
                nome=data['nome'],
                url=data['url'],
                departamento=data['departamento'],
                descricao=data['descricao']
            )
        
            
            return JsonResponse({"message": "Link criado com sucesso!"})
        except json.JSONDecodeError as e:
            return JsonResponse({"error": f"Erro ao decodificar o JSON: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Erro interno: {str(e)}"}, status=400)
    return JsonResponse({"error": "Método não permitido"}, status=405)


            
@csrf_exempt
def create_programa(request):
    if request.method == "POST":
        try:
            nome = request.POST.get('nome')
            descricao = request.POST.get('descricao', '')
            link_download = request.POST.get('link_download', '')
            departamento = request.POST.get('departamento')
            arquivo = request.FILES.get('arquivo', None)

            if not nome or not departamento:
                return JsonResponse({"error": "Campos obrigatórios estão faltando"}, status=400)

            Programa.objects.create(
                nome=nome,
                descricao=descricao,
                link_download=link_download,
                departamento=departamento,
                arquivo=arquivo,
            )

            return JsonResponse({"message": "Programa adicionado com sucesso!"})
        except Exception as e:
            return JsonResponse({"error": f"Erro interno: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método não permitido"}, status=405)

@csrf_exempt
def create_manual(request):
    if request.method == "POST":
        try:
            nome = request.POST.get('nome')
            descricao = request.POST.get('descricao', '')
            link_download = request.POST.get('link_download', '')
            departamento = request.POST.get('departamento')
            arquivo = request.FILES.get('arquivo', None)

            if not nome or not departamento:
                return JsonResponse({"error": "Campos obrigatórios estão faltando"}, status=400)

            Manual.objects.create(
                nome=nome,
                descricao=descricao,
                link_download=link_download,
                departamento=departamento,
                arquivo=arquivo,
            )

            return JsonResponse({"message": "Manual adicionado com sucesso!"})
        except Exception as e:
            return JsonResponse({"error": f"Erro interno: {str(e)}"}, status=500)

    return JsonResponse
