from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .scraper import scrape_aliexpress

@csrf_exempt
def parse_product(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            url = body.get('url')
            if not url:
                return JsonResponse({'error': 'URL is required'}, status=400)
            result = scrape_aliexpress(url)
            return JsonResponse(result[0] if result else {'error': 'No data'}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)