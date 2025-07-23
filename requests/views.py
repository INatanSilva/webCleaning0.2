from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Request
import json
import logging

logger = logging.getLogger(__name__)

# Create your views here.

@csrf_exempt
def create_request(request):
    logger.info(f"Acessou create_request com método {request.method}")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome = data.get('nome')
            numero_contato = data.get('numero_contato')
            tipo_limpeza = data.get('tipo_limpeza')
            logger.debug(f"Dados recebidos: nome={nome}, numero_contato={numero_contato}, tipo_limpeza={tipo_limpeza}")
            if not (nome and numero_contato and tipo_limpeza):
                logger.warning("Campos obrigatórios faltando na requisição.")
                return JsonResponse({'error': 'Todos os campos são obrigatórios.'}, status=400)
            req = Request.objects.create(
                nome=nome,
                numero_contato=numero_contato,
                tipo_limpeza=tipo_limpeza
            )
            logger.info(f"Request criado com id {req.id}")
            return JsonResponse({'success': True, 'id': req.id})
        except Exception as e:
            logger.error(f"Erro ao criar request: {e}")
            return JsonResponse({'error': str(e)}, status=400)
    logger.warning("Método não permitido em create_request.")
    return JsonResponse({'error': 'Método não permitido.'}, status=405)

def home(request):
    logger.info("Acessou a home view")
    return render(request, 'requests/home.html')
