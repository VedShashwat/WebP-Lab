from django.shortcuts import render

# Question 1: Arithmetic Operations
def arithmetic_view(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            op = request.POST.get("operation")
            
            if op == "add":
                result = num1 + num2
            elif op == "sub":
                result = num1 - num2
            elif op == "mul":
                result = num1 * num2
            elif op == "div":
                result = num1 / num2
        except:
            result = "Invalid Input"
            
    return render(request, "lab_app/arithmetic.html", {"result": result})



def magazine_view(request):
    context = {}
    if request.method == "POST":
        context['title'] = request.POST.get('title')
        context['bg_color'] = request.POST.get('bg_color')
        context['font_color'] = request.POST.get('font_color')
        context['font_size'] = request.POST.get('font_size')
        context['font_family'] = request.POST.get('font_family')
        
    return render(request, "lab_app/magazine.html", context)