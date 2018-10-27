from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models
import json

ret={"status":True,"data":None,"error":None}

def business(request):
    v=models.Business.objects.all()
    v2=models.Business.objects.all().values('id','caption')
    v3=models.Business.objects.all().values_list('id','caption')



    return  render(request,'business.html',{'v':v,'v2':v2,'v3':v3})


def login(request):
    return  HttpResponse('login')

def host(request):
    obj=models.Host.objects.all()
    obj4=models.Business.objects.all()
    obj2 = models.Host.objects.all().values('hostname','ip','port','b__caption')
    obj3 = models.Host.objects.all().values_list('hostname','ip','port','b__caption')
    # print(obj2)
    return render(request,'host.html',{'obj':obj,'obj2':obj2,'obj3':obj3,'obj4':obj4})

def test(request):
    pass

def test_ajax(request):
    h=request.GET.get("hostname")
    i=request.GET.get("ip")
    port=request.GET.get("port")
    print(h,i,port)
    return HttpResponse('ok')

def dele(request):
    i=request.POST.get('id')
    # print('---->',i)
    models.Host.objects.filter(nid=i).delete()
    return HttpResponse('ok')

def test_edit(request):
    h=request.POST.get('hostname')
    i=request.POST.get('ip')
    p=request.POST.get('port')
    s=request.POST.get('a')
    d=request.POST.get('id')


    models.Host.objects.filter(nid=d).update(hostname=h,ip=i,port=p,b_id=s)
    return HttpResponse('ok')

def app(request):
    if request.method=='GET':
        obj=models.Application.objects.all()
        obj2=models.Host.objects.all()
        return render(request,'app.html',{"obj":obj,"obj2":obj2})

    elif request.method=='POST':
        try:
            a=request.POST.get('app_name')
            e=request.POST.getlist('edit_sel')
            print(a,e)
            a_obj=models.Application.objects.create(name=a)
            if a_obj:
                a_obj.r.add(*e)
            else:
                ret['status']=False
        except Exception as e:
            ret['error']=e
            ret['status'] = False
        return HttpResponse(json.dumps(ret))
def deleter(request):
    if request.method=='POST':
        try:
            a_id=request.POST.get('aid')
            print(a_id)
            a=models.Application.objects.filter(id=a_id).delete()
            # print(a)
            if a:
                pass
            else:
                ret['status'] = False
        except Exception as e:
            ret['error']=e
            ret['status'] = False
        return HttpResponse(json.dumps(ret))

def edit(request):
    if request.method == 'POST':
        e=request.POST.get('edit_name')
        s=request.POST.getlist('edit_sel')
        aid=request.POST.get('aid')
        a_obj=models.Application.objects.filter(id=aid).first()
        # print(a_obj)
        a_obj.r.set(s)
        models.Application.objects.filter(id=aid).update(name=e)


        return HttpResponse(json.dumps(ret))