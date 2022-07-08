from email import message
from faulthandler import disable
import imp
from datetime import datetime
from math import fabs
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from numpy import number
from platformdirs import user_cache_dir
from requests_toolbelt import user_agent
from stocks.forms import AddFabrics 
from .models import Fabrics,Items,Makers, Partycodes, Fabnames
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test


# add and show.
@user_passes_test(lambda u: u.is_superuser)
def addshow(request):
    if request.method == 'POST':
        ff = AddFabrics(request.POST)
        if ff.is_valid():
            pc=ff.cleaned_data['partycode']
            c=ff.cleaned_data['color']
            m=ff.cleaned_data['meter']
            f=ff.cleaned_data['fabric']
            mk=ff.cleaned_data['maker']
            reg=Fabrics(partycode=pc,color=c,meter=m,fabric=f,maker=mk)
            reg.save()
        ff = AddFabrics()
        return HttpResponseRedirect('/')
    else:
        ff = AddFabrics()
        fabs=Fabrics.objects.filter(cutting=0)
        makers=Makers.objects.all()
    return render(request, 'addshow.html',{'fabform':ff,'fabs':fabs,'makers':makers})

# delete
@user_passes_test(lambda u: u.is_superuser)
def deletedata(request, id):
    pi = Fabrics.objects.get(id=id)
    pi.delete()
    return HttpResponseRedirect('/')

# delete data individual
@user_passes_test(lambda u: u.is_superuser)
def deleteindi(request, maker, id):
    url =f'/addandshow/{maker}/'
    pi = Fabrics.objects.get(id=id)
    pi.delete()
    return HttpResponseRedirect(url)


# Update
@user_passes_test(lambda u: u.is_superuser)
def updatedata(request, id):
    if request.method == 'POST':
        pi = Fabrics.objects.get(pk=id)
        ff = AddFabrics(request.POST,instance=pi)
        if ff.is_valid():
            ff.save()
        return HttpResponseRedirect('/')
    else:
        pi = Fabrics.objects.get(pk=id)
        ff = AddFabrics(instance=pi)
        makers=Makers.objects.all()
    return render(request,'update.html',{'fabform':ff,'makers':makers})
    
# Update data individual
@user_passes_test(lambda u: u.is_superuser)
def updateindi(request,maker , id):
    url =f'/addandshow/{maker}/'
    if request.method == 'POST':
        pi = Fabrics.objects.get(pk=id)
        ff = AddFabrics(request.POST,instance=pi)
        if ff.is_valid():
            ff.save()
        return HttpResponseRedirect(url)
    else:
        pi = Fabrics.objects.get(pk=id)
        ff = AddFabrics(instance=pi)
        makers=Makers.objects.all()
    return render(request,'update.html',{'fabform':ff,'makers':makers})
    
# makers by admin
@user_passes_test(lambda u: u.is_superuser)
def maker(request,maker):
    url =f'/addandshow/{maker}/'
    if request.method == 'POST':
        ff = AddFabrics(request.POST, initial={'maker':maker})
        if ff.is_valid():
            pc=ff.cleaned_data['partycode']
            c=ff.cleaned_data['color']
            m=ff.cleaned_data['meter']
            f=ff.cleaned_data['fabric']
            reg=Fabrics(partycode=pc,color=c,meter=m,fabric=f,maker=maker)
            reg.save()
        ff = AddFabrics(initial={'maker':maker})
        return HttpResponseRedirect(url)
    else:
        ff = AddFabrics(initial={'maker':maker})
        fabs=Fabrics.objects.filter(Q(maker=maker)&Q(cutting=0))
        makers=Makers.objects.all()
    return render(request, 'maker.html',{'fabform':ff,'fabs':fabs,'mkr':maker,'makers':makers})



# query
@user_passes_test(lambda u: u.is_superuser)
def search(request):
    query = request.GET['query']
    if len(query)==0:
        fabs=Fabrics.objects.none()
    else:
        fabscolor = Fabrics.objects.filter(color__icontains=query)
        fabspartycode = Fabrics.objects.filter(partycode__icontains=query)
        fabsfabric = Fabrics.objects.filter(fabric__icontains=query)
        fabsmaker = Fabrics.objects.filter(maker__icontains=query)
        fabsitem = Fabrics.objects.filter(item__icontains=query)
        fabs = fabscolor.union(fabspartycode,fabsfabric,fabsmaker,fabsitem)
    makers=Makers.objects.all()
    return render(request,'search.html',{'fabs':fabs,'query':query,'makers':makers})


# advance search
@user_passes_test(lambda u: u.is_superuser)
def advsearch(request):
    if request.method == 'POST':
        partycode = request.POST.get('partycode')
        color = request.POST['color']
        fabric = request.POST.get('fabname')
        maker = request.POST.get('maker')  
        item = request.POST.get('item')  
        completed = request.POST.get('completed')

        if partycode != None:
            fabspartycode = Fabrics.objects.filter(partycode=partycode)
        else:
            fabspartycode = Fabrics.objects.all()
        if color != "":
            fabscolor = Fabrics.objects.filter(color__icontains=color)
        else:
            fabscolor = Fabrics.objects.all()
        if fabric != None:
            fabsfabric = Fabrics.objects.filter(fabric=fabric)
        else:
            fabsfabric = Fabrics.objects.all()
        if maker != None:
            fabsmaker = Fabrics.objects.filter(maker=maker)
        else:
            fabsmaker = Fabrics.objects.all()
        if item != None:
            print(item)
            fabsitem = Fabrics.objects.filter(item=item)
            print(fabsitem)
        else:
            fabsitem = Fabrics.objects.all()
        if completed != None:
            fabscompleted = Fabrics.objects.filter(completed=completed)
        else:
            fabscompleted = Fabrics.objects.all()

        fabs = fabscolor.intersection(fabspartycode,fabsfabric,fabsmaker,fabsitem,fabscompleted)

    else:
        fabs=Fabrics.objects.all()
    makers=Makers.objects.all()
    items=Items.objects.all()
    partycodes=Partycodes.objects.all()
    fabnames=Fabnames.objects.all()
    return render(request,'advsearch.html',{'fabs':fabs,'makers':makers,'items':items,'partycodes':partycodes,'fabnames':fabnames})



# maker table
@login_required
def maker_table(request, maker):
    if request.user.first_name == maker:
        fabs=Fabrics.objects.filter(Q(maker=maker)&Q(completed=False))
        print(request.META.get('HTTP_USER_AGENT'))
        return render(request, 'maker_table.html',{'fabs':fabs,'mkr':maker})
    else:
        logout(request)
        return render(request,'login.html')
        

# maker edit
@login_required
def maker_edit(request,maker, id):
    if request.user.first_name == maker:
        url =f'/makertable/{maker}/'
        if request.method == 'POST':
            pi = Fabrics.objects.get(pk=id)
            getcut= request.POST.get('cutting')
            itm= request.POST.get('item')
            if getcut != '' and itm != None:
                if not pi.item:
                    pi.item = itm
                if not pi.cutting:
                    pi.cutting = getcut
                if not pi.cut_time:
                    pi.cut_time = datetime.now()
                pi.save()
            return HttpResponseRedirect(url)
        else:
            fabs = Fabrics.objects.get(pk=id)
            itms = Items.objects.filter(maker__maker=maker)
        return render(request, 'maker_edit.html',{'fabs':fabs,'itms':itms})
    else:
        logout(request)
        return render(request,'login.html')
        


# admin received
@user_passes_test(lambda u: u.is_superuser)
def admin_rec(request, maker):
    fabs=Fabrics.objects.filter(Q(maker=maker) & Q(hsb_clr=False) & ~Q(cutting=0))
    makers=Makers.objects.all()
    return render(request, 'admin_rec.html',{'fabs':fabs,'mkr':maker,'makers':makers})

# admin received edit
@user_passes_test(lambda u: u.is_superuser)
def admin_rec_edit(request,maker, id):
    url =f'/adminrec/{maker}/'
    if request.method == 'POST':
        pi = Fabrics.objects.get(pk=id)
        recpcs= request.POST.get('recpcs')
        grpcs= request.POST.get('grpcs')
        complt= request.POST.get('complt')
        if recpcs != "":
            pi.rec_pcs = recpcs
        if grpcs != "":
            pi.gr_pcs = grpcs
        if complt != None and pi.rec_pcs != "":
            pi.completed = True
        else:
            pi.completed = False
        pi.save()
        return HttpResponseRedirect(url)
    else:
        fabs = Fabrics.objects.get(pk=id)
    makers=Makers.objects.all()
    return render(request, 'admin_rec_edit.html',{'fabs':fabs,'mkr':maker,'makers':makers})


# Reject cutting
@user_passes_test(lambda u: u.is_superuser)
def reject_cutting(request, maker, id):
    url=f'/adminrec/{maker}'
    fabs = Fabrics.objects.get(pk=id)
    fabs.cutting = 0
    fabs.item = ''
    fabs.save()
    return HttpResponseRedirect(url)


# Hisab
@user_passes_test(lambda u: u.is_superuser)
def hsbclr(request, maker):
    makers=Makers.objects.all()
    if request.method == 'POST':
        frm= request.POST.get('from')
        to= request.POST.get('to')
        if frm != "" and to != "":
            fab1=Fabrics.objects.filter(Q(id__gte=frm) & Q(id__lte=to))
            fab2=Fabrics.objects.filter(Q(maker=maker) & Q(completed=True) & Q(hsb_clr=False))
            fabs=fab1.intersection(fab2)

            itms = Items.objects.all()
            lst=[]
            dict1={}
            k=0
            ttl=0
            for i in itms:
                for j in fabs:
                    if i.item == j.item:
                        k += j.rec_pcs
                if k != 0:
                    dict1['itm']=i.item
                    dict1['rate']=i.rate
                    dict1['quantity']=k
                    dict1['val']=(i.rate)*k
                    ttl += dict1['val']
                    lst.append(dict1.copy())
                    k=0
            return render(request, 'hsbclr.html',{'fabs':fabs,'mkr':maker,'lst':lst,'ttl':ttl,'frm':frm,'to':to,'makers':makers})
        else:
            fabs=Fabrics.objects.filter(Q(maker=maker) & Q(completed=True) & Q(hsb_clr=False))
            return render(request, 'hsbclr.html',{'fabs':fabs,'mkr':maker,'makers':makers})
    else:
        fabs=Fabrics.objects.filter(Q(maker=maker) & Q(completed=True) & Q(hsb_clr=False))
        return render(request, 'hsbclr.html',{'fabs':fabs,'mkr':maker,'makers':makers})



# clrr
@user_passes_test(lambda u: u.is_superuser)
def clrr(request, maker, frm, to):
    url =f'/hsbclr/{maker}/'
    fab1=Fabrics.objects.filter(Q(id__gte=frm) & Q(id__lte=to))
    fab2=Fabrics.objects.filter(Q(maker=maker) & Q(completed=True))
    fabs=fab1.intersection(fab2)
    for i in fabs:
        i.hsb_clr = True
        i.save()
    print(frm)
    print(to)
    return HttpResponseRedirect(url)

# clear stock
@user_passes_test(lambda u: u.is_superuser)
def clrstk(request):
    fabs = Fabrics.objects.filter(hsb_clr=True)
    makers=Makers.objects.all()
    return render(request, 'clrstk.html',{'fabs':fabs,'makers':makers})


# item edit
@user_passes_test(lambda u: u.is_superuser)
def itemedit(request):
    if request.method == 'POST':
        nm = request.POST.get('itemname')
        rt = request.POST.get('itemrate')
        reg = Items(item=nm,rate=rt)
        reg.save()
    itms = Items.objects.all()
    makers=Makers.objects.all()
    return render(request, 'itemedit.html',{'itms':itms,'makers':makers})

# item update
@user_passes_test(lambda u: u.is_superuser)
def itemupdate(request,id):
    if request.method == 'POST':
        reg = Items.objects.get(id=id)
        nm = request.POST.get('itemname')
        rt = request.POST.get('itemrate')
        reg.item = nm
        reg.rate = rt
        reg.save()
        return HttpResponseRedirect('/itemedit/')
    itms = Items.objects.get(id=id)
    makers=Makers.objects.all()
    return render(request, 'itemupdate.html',{'itms':itms,'makers':makers})


# item delete
@user_passes_test(lambda u: u.is_superuser)
def itemdelete(request,id):
    itms = Items.objects.get(id=id)
    itms.delete()
    return HttpResponseRedirect('/')


# login
def ulogin(request):
    if request.method=='POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                if request.user.first_name == 'nisar':
                    return HttpResponseRedirect('/')
                else:
                    nm = request.user.first_name
                    url2= f'/makertable/{nm}/'
                    print(url2)
                    return HttpResponseRedirect(url2)
    return render(request,'login.html')


# logout
@login_required
def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

