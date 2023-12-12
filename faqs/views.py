from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FAQ, FAQCategoria
from .forms import FAQForm, CategoriaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def faq_categorias(request):
    categorias = FAQCategoria.objects.all()
    form = CategoriaForm()  
    return render(request, 'faq_categorias.html', {'categorias': categorias, 'form': form})

@login_required
def faq_list(request, categoria_id):
    categoria = FAQCategoria.objects.get(pk=categoria_id)
    faqs = FAQ.objects.filter(categoria=categoria)
    form = FAQForm()

    page = request.GET.get('page', 1)
    paginator = Paginator(faqs, 3)  

    try:
        faqs_paginated = paginator.page(page)
    except PageNotAnInteger:
        faqs_paginated = paginator.page(1)
    except EmptyPage:
        faqs_paginated = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()
            return redirect('faq_list', categoria_id=categoria_id)

    return render(
        request,
        'faq_list.html',
        {'categoria': categoria, 'faqs': faqs_paginated, 'form': form}
    )

def enviar_pergunta(request, categoria_id):
    if request.method == 'POST':
        pergunta = request.POST.get('pergunta')
        categoria = FAQCategoria.objects.get(pk=categoria_id)
        FAQ.objects.create(pergunta=pergunta, categoria=categoria)

    return redirect('faq_list', categoria_id=categoria_id)


def enviar_resposta(request, faq_id):
    if request.method == 'POST' and request.user.is_staff:
        resposta = request.POST.get('resposta')
        faq = FAQ.objects.get(pk=faq_id)
        faq.resposta = resposta
        faq.save()

    return redirect('faq_list', categoria_id=faq.categoria.id)

@login_required
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_categorias')  
        

