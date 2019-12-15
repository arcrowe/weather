from django.shortcuts import render


def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json"
                               "&zipCode=10014&distance=25&API_KEY=118F0276-37E4-4610-8D87-3703C76505E6")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error.."

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
