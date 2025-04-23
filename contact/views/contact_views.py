from django.shortcuts import render, get_object_or_404, redirect

from contact.models import Contact

from django.db.models.functions import Concat
from django.db.models import Q, Value # (Q) serve para fazer consultas mais complexas, possibilitando utilizar operadores lógicos
# AND (&), OR (|), NOT (~)

from django.core.paginator import Paginator

from django.http import Http404

def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('id') \
    
    paginator = Paginator(contacts, 10) # Pega 10 contatos por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contacts - ',
    }
    
    return render(request, 'contact/index.html', context)

def search(request):
    search_value = request.GET.get('query', '').strip()
    selected_filters = request.GET.getlist("filter")
    
    # Se digitar nada no input ele retorna para a home
    if search_value == '':
        return redirect('contact:index')
    
    # Filtra somente os contatos com show=True
    contacts = Contact.objects.filter(show=True)
    
    # Adiciona o campo full_name como uma concatenação de first_name e last_name
    contacts = contacts.annotate(full_name = Concat('first_name', Value(' '), 'last_name'))
    
    queries = Q()
    if "id" in selected_filters and search_value.isdigit():
        queries |= Q(id__exact=search_value)
    if "first_name" in selected_filters:
        queries |= Q(first_name__icontains=search_value)
    if "last_name" in selected_filters:
        queries |= Q(last_name__icontains=search_value)
    if "phone" in selected_filters:
        queries |= Q(phone__icontains=search_value)
    if "email" in selected_filters:
        queries |= Q(email__icontains=search_value)
    
    if not selected_filters:
        # Cria as queries para os campos selecionados
        queries  =  Q(first_name__icontains=search_value) | \
                    Q(last_name__icontains=search_value) | \
                    Q(phone__icontains=search_value) | \
                    Q(full_name__icontains=search_value) | \
                    Q(email__icontains=search_value)
        
        # Caso o usuário escreveu um número no input, ele também busca pelo id
        if search_value.isdigit():
            queries |= Q(id__exact=search_value) # Retorna somente quando o id for EXATO

    contacts = contacts \
        .filter(queries) \
        .order_by('id') \

    paginator = Paginator(contacts, 10) # Pega 10 contatos por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
        'selected_filters': selected_filters,
    }
    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404
    
    # Os dois fazem a mesma coisa ^v
    
    single_contact = get_object_or_404( # Isso chama somente contatos onde a pk é igual o contact_id e o show é True
        Contact,
        pk=contact_id,
        show=True,
    )
    
    title_name = f"{single_contact.first_name} {single_contact.last_name}"
    
    context = {
        'contact': single_contact,
        'site_title': title_name,
    }
    
    return render(request, 'contact/contact.html', context)