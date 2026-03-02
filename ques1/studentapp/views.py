from django.shortcuts import render

def student_view(request):
    result_text = ""
    percentage = ""
    
    if request.method == "POST":
        try:
            # Get data from form
            name = request.POST.get("name")
            dob = request.POST.get("dob")
            address = request.POST.get("address")
            contact = request.POST.get("contact")
            email = request.POST.get("email")
            
            # Get marks and convert to float
            eng = float(request.POST.get("english"))
            phy = float(request.POST.get("physics"))
            chem = float(request.POST.get("chemistry"))
            
            # Calculate Percentage (Assuming total is 300)
            total = eng + phy + chem
            perc = (total / 300) * 100
            percentage = f"{perc:.2f}%"
            
            # Format the details for the textarea
            result_text = f"Name: {name}\nDOB: {dob}\nAddress: {address}\nContact: {contact}\nEmail: {email}\n\nMarks:\nEnglish: {eng}\nPhysics: {phy}\nChemistry: {chem}"
            
        except (ValueError, TypeError):
            result_text = "Invalid Input! Please enter numbers for marks."

    return render(request, "studentapp/student.html", {
        "result_text": result_text, 
        "percentage": percentage
    })