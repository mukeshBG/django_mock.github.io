from django.shortcuts import render
from library.models import Patron_management,Book_management,Borrowing


def borrowing_details(request,Borrowing_id):
    name=Patron_management.objects.get(id=Borrowing_id)
    book=Book_management.objects.get(id=Borrowing_id)
    
    context={
        "Book_Name":book,
        "Patron_name":name,
        "Due_date":str(book.return_date),
    }
    return render(request,"library/details_view.html",context)
    