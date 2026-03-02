from django.shortcuts import render, redirect

SUBJECTS = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'English', 'History']

def first_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')

        # Store data in Django session
        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject

        return redirect('/session/secondpage/')

    return render(request, 'sessionapp/firstPage.html', {'subjects': SUBJECTS})

def second_page(request):
    # Retrieve data from session
    name = request.session.get('name', 'N/A')
    roll = request.session.get('roll', 'N/A')
    subject = request.session.get('subject', 'N/A')

    return render(request, 'sessionapp/secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject,
    })
