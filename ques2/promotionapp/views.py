from django.shortcuts import render
from datetime import date, datetime

def promotion_view(request):
    eligibility_msg = ""
    
    if request.method == "POST":
        try:
            # Get date string from form (format YYYY-MM-DD)
            doj_str = request.POST.get("doj")
            
            # Convert string to date object
            doj = datetime.strptime(doj_str, "%Y-%m-%d").date()
            today = date.today()
            
            # Calculate experience in years (roughly days / 365)
            delta = today - doj
            years_experience = delta.days / 365.25
            
            if years_experience > 5:
                eligibility_msg = "YES"
            else:
                eligibility_msg = "NO"
                
        except (ValueError, TypeError, AttributeError):
            eligibility_msg = "Error! Please enter a valid date."

    return render(request, "promotionapp/promotion.html", {"message": eligibility_msg})