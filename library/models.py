from django.db import models

# Create your models here.

class Book_management(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=20,default="none")
    isbn = models.IntegerField()
    availability_status = models.CharField(max_length = 15)
    def __str__(self):
        return self.title    
    
class Patron_management(models.Model):
    name = models.CharField(max_length=55)
    contact_info = models.CharField(max_length=200)
    membership_details = models.CharField(max_length=20,default="normal") 
    def __str__(self):
        return f'Patron name : {self.name}'
    
    
class Borrowing(models.Model):
    title = models.ForeignKey(Book_management,on_delete=models.CASCADE)
    name = models.ForeignKey(Patron_management , on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    def __str__(self):
        return f'Patron name : {self.name} => Book : {self.title}'
