from django.shortcuts import render, HttpResponsePermanentRedirect, reverse, \
    HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from .models import Category, Products
from .forms import PrForm, PrInitForm
from django.core.paginator import Paginator


def index(request):
    category = Category.objects.order_by('name')
    dic = {'categ': category}
    return render(request, 'Market/index.html', dic)


def add(request):
    if request.method == 'POST':
        prf = PrForm(request.POST)
        if prf.is_valid():
            ret_name = prf.cleaned_data['categ']
            c = Category.objects.get(name=ret_name)
            prf.save()
            return HttpResponseRedirect(reverse('market:index') + c.eng_name)
    else:
        prf = PrForm()
        content = {'form': prf}
        return render(request, 'Market/add.html', content)


def delete(request):
    if request.method == 'POST':
        ids = request.POST.get('num')
        Products.objects.filter(id=ids).delete()
        return HttpResponsePermanentRedirect(reverse('market:index'))
    else:
        return render(request, 'Market/delete.html')


def prod_table(request, cat_name, ):
    try:
        cat_list = Category.objects.get(eng_name=cat_name)
        pr_list = cat_list.products_set.order_by('name')
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    else:
        paginator = Paginator(pr_list, 10)
        # print(paginator.num_pages)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        # paginator
        if request.method == 'GET':
            # steic pag
            # steic pag
            form_list = [
                PrInitForm(prefix=str(pg.id), initial={'name': pg.name, 'cost': pg.cost, 'ids': pg.id,
                                                       'outdate': pg.outdate, 'count': pg.count})
                for pg in page.object_list]
            dic = {'prod': form_list, 'page': page, 'rg': range(1, paginator.num_pages + 1)}
            return render(request, 'Market/prod.html', dic)
        else:
            # paginatorn khanes durs kverces idnern kpoxes informacian karas klass sarqes
            for pg in page.object_list:
                prod = Products.objects.get(pk=request.POST.get('{}-ids'.format(pg.id)))
                prod.name = request.POST.get('{}-name'.format(pg.id))
                prod.cost = request.POST.get('{}-cost'.format(pg.id))
                prod.count = request.POST.get('{}-count'.format(pg.id))
                prod.outdate = request.POST.get('{}-outdate'.format(pg.id))
                prod.save()

            return HttpResponseRedirect(request.path_info)
