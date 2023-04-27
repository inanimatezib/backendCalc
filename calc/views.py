import math

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Formula, Usuario
from .forms import FormulaForm

def index(request):
    return render(request, 'index.html')
def write(request):
    if request.method == 'POST':
        form = FormulaForm(request.POST)

        if form.is_valid():
            formula = form.save()
            a = formula.x1
            b = formula.x2
            c = formula.x3
            delta = formula.delta
            res1 = formula.res1
            res2 = formula.res2
            resdelta = pow(b, 2) - 4 * a * c
            formula.delta = resdelta
            if resdelta < 0:
                return HttpResponse('error')
            else:
                calc1 = (-abs(b) + math.sqrt(resdelta)) / 2 * a
                calc2 = (-abs(b) - math.sqrt(resdelta)) / 2 * a
                formula.res1 = calc1
                formula.res2 = calc2
                formula = form.save()
                context = {
                    'delta': formula.delta,
                    'res1': formula.res1,
                    'res2': formula.res2,
                }
                return render(request, 'thanks.html', context=context)
        else:
            context = {
                'form': form
            }
            return render(request, 'base.html', context=context)
    else:
        form = FormulaForm()
        context = {
            'form': form
        }
        return render(request, 'base.html', context=context)


