from django.shortcuts import render,get_object_or_404,redirect

from crudapp.models import Item


# Create your views here.

#CRUD

# CREATE
def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name,description=description)
        return redirect('item_list')
    return render(request,'item_list.html')

# READ
def item_list(request):
    items = Item.objects.all()
    return render(request,'item_list.html',{'items':items})

# UPDATE
def update_item(request,pk):
    item = get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        Item.name=request.POST.get('name')
        Item.description=request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request,'item_form.html',{'item':item})

# DELETE
def delete_item(request,pk):
    item = get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request,'item_confirm_delete.html',{'item':item})