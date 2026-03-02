from django.shortcuts import render, redirect

CAR_MANUFACTURERS = [
    'Toyota',
    'Honda',
    'Ford',
    'BMW',
    'Mercedes-Benz',
    'Audi',
    'Volkswagen',
    'Hyundai',
    'Kia',
    'Chevrolet',
    'Nissan',
    'Suzuki',
]

def car_form(request):
    if request.method == 'POST':
        manufacturer = request.POST.get('manufacturer')
        model = request.POST.get('model')
        return redirect(f'/car/result/?manufacturer={manufacturer}&model={model}')
    return render(request, 'carapp/form.html', {'manufacturers': CAR_MANUFACTURERS})

def car_result(request):
    manufacturer = request.GET.get('manufacturer')
    model = request.GET.get('model')
    return render(request, 'carapp/result.html', {
        'manufacturer': manufacturer,
        'model': model,
    })
