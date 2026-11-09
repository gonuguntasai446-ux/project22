
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee


# DISPLAY EMPLOYEES
def employee_list(request):
    employees = Employee.objects.all().order_by('ID')

    search = request.GET.get('search')

    if search:
        employees = employees.filter(NAME__icontains=search)

    return render(request, 'employee_list.html', {
        'employees': employees
    })
from django.shortcuts import render
from .models import Employee

def getall(request):
    emp = Employee.objects.all()

    return render(request, 'getall.html', {
        'emp': emp
    })

# ADD EMPLOYEE
def employee_add(request):
    if request.method == 'POST':
        Employee.objects.create(
            NAME=request.POST['NAME'],
            ROLE=request.POST['ROLE'],
            SALARY=request.POST['SALARY'],
            DATE_OF_JOIN=request.POST['DATE_OF_JOIN'],
            BONUS=request.POST['BONUS']
        )
        return redirect('employee_list')

    return render(request, 'employee_add.html')


# EDIT EMPLOYEE
def employee_edit(request, id):
    employee = get_object_or_404(Employee, ID=id)

    if request.method == 'POST':
        employee.NAME = request.POST['NAME']
        employee.ROLE = request.POST['ROLE']
        employee.SALARY = request.POST['SALARY']
        employee.DATE_OF_JOIN = request.POST['DATE_OF_JOIN']
        employee.BONUS = request.POST['BONUS']

        employee.save()
        return redirect('employee_list')

    return render(request, 'employee_edit.html', {
        'employee': employee
    })


# DELETE EMPLOYEE
def employee_delete(request, id):
    employee = get_object_or_404(Employee, ID=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employee_delete.html', {
        'employee': employee
    })
