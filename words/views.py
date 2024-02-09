import json

from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from words.forms import WordForm
from words.models import Author , Word
from main.function import generate_form_errors

@login_required(login_url="/users/login/")
def create_word(request):
    if request.method == "POST":
        form = WordForm(request.POST,request.FILES)
        if form.is_valid():
            if not Author.objects.filter(user = request.user).exists():
                author = Author.objects.create(user=request.user,name=request.user.username)
            else:
                author = request.user.author

            instance = form.save(commit=False)
            instance.author = author
            instance.save()

            response_data = {
                "title" : "Successfully submitted",
                "message" : "Successfully submitted",
                "status" : "success",
                "redirect" : "yes",
                "redirect_url" : "/"
            }

           
        else:
            error_message = generate_form_errors(form)
            response_data = {
                "title" : "form validation error",
                "message" : str(error_message),
                "status" : "error",
                "stable" : "yes"
            }

        return HttpResponse(json.dumps(response_data),content_type="application/json")
        
    else:
        form = WordForm()
        context = {
                "title": "Create word",
                "form": form,
        }
        return render(request, "words/create.html", context=context)
    

def search(request):
    query = request.GET.get('q', '').strip()
    if query:
        results = Word.objects.filter(word__istartswith=query)
        no_results = not results.exists()
        return render(request, 'web/index.html', {'results': results, 'query': query, 'no_results': no_results})
    else:
        return render(request, 'web/index.html', {'results': None, 'query': '', 'no_results': False})

