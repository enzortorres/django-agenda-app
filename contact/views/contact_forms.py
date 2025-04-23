from django.shortcuts import render, get_object_or_404, redirect

from contact.models import Contact

from django.db.models.functions import Concat
from django.db.models import Q, Value # (Q) serve para fazer consultas mais complexas, possibilitando utilizar operadores lógicos
# AND (&), OR (|), NOT (~)

from django.core.paginator import Paginator

from django.http import Http404

def create(request):
    context = {
        'site_title': 'Contacts - ',
    }
    
    return render(request, 'contact/create.html', context)