from django.http import HttpResponse
from django.shortcuts import render
import requests


def home(request):
  #USING APIS
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  data = response.json()
  result = data['message']

  return render(request, 'templates/index.html', {'result': result})


#defining dog_view
def dog_view(request):
  result = None  # Initialize result variable
  if request.method == 'GET':
    # Logic for handling GET request
    return render(request, 'index.html', {'result': result})
  # Render the form template
  elif request.method == 'POST':
    # Process the form data and interact with the Dog API
    breed = request.POST.get('breed')
    response = requests.get(
        f'https://dog.ceo/api/breeds/image/random?breed_id={breed}')
    if response.status_code == 200:
      data = response.json()
      image_url = data[0]['url']
      return render(request, 'dog_result.html', {'image_url': image_url})
    else:
      return render(
          request, 'error.html')  # Render error template if API request fails.


# adopt_dog
def adopt_dog(request):
  result = None
  if request.method == 'GET':
    return render(request, 'templates/index.html', {'result': result})
  elif request.method == 'POST':
    breed = request.POST.get('breed')
    response = requests.get(
        f'https://dog.ceo/api/breeds/image/random?breed_id={breed}')
    if response.status_code == 200:
      data = response.json()
      # Performing actions related to adopting a dog
      return HttpResponse(b"Dog adoption successful!")
    else:
      return render(
          request, 'error.html')  # Render error template if API request fails.
