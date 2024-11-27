from django.views import generic
from django.urls import reverse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Fill

class IndexViews(generic.ListView):
    model = Fill  
    template_name = "Fill/index.html"
    context_object_name = 'Fill'



def post_view(request):
    if request.method == 'POST':
        form, created = Fill.objects.get_or_create(name=request.POST.get('fill', ''))

        if not created: 
            form.valor= float(request.POST.get('valor'))
            form.cota_qtd= int(request.POST.get('cota'))
            form.dividendos=float(request.POST.get('dividy'))
           

        if created: 
            form.valor= float(request.POST.get('valor'))
            form.cota_qtd= int(request.POST.get('cota'))
            form.dividendos=float(request.POST.get('dividy'))

        form.save()
       
        return redirect(reverse('Fill:form_list')) 

    context = {'Fill': Fill.objects.all()} 
    return render(request, 'Fill/teste.html', context)
    