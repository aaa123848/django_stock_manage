from django.shortcuts import render
from . import models
from django.shortcuts import redirect

from django.http import HttpResponse


# Create your views here.

def base(request):
    return render(request, 'stock/base.html')
   

def stock(request):
    if request.method =='POST':
        itemname = request.POST.get('itemname', None)
        itemspec = request.POST.get('itemspec', None)
        saftystock = request.POST.get('saftystock', '0')
        platform = request.POST.get('platform', None)
        total_import = request.POST.get('import', '0')
        total_output = request.POST.get('output', '0')
        stock = request.POST.get('stock', '0')

        if stock == '':
            stock = 0

        if total_output == '':
            total_output = 0
        if total_import == '':
            total_import = 0
        if saftystock == '':
            saftystock = 0

        try :    #前端已經擋住，這段不用
            int(saftystock)
            int(total_import)
            int(total_output)
            int(stock)
        except ValueError:
            message = '庫存安全量 總入庫數 總出庫數 現有庫存 需輸入數字 '
            return render(request, 'stock/stock.html', {'message':message}) 

        print(stock)  
        print(type(stock))
        print(type(int(float(stock))))
        saftystock = int(saftystock)
        total_import = int(total_import)
        total_output = int(total_output)
        stock = int(stock)
        print(type(saftystock), type(total_import), type(total_output), type(stock))
        
       

        itemname_exist = models.stock.objects.filter(itemname=itemname)
        if itemname_exist :
            itemspec_exist = models.stock.objects.filter(itemname=itemname, itemspec=itemspec)
            if  itemspec_exist :
                message = itemname+itemspec+'已經存在'
                return render(request, 'stock/stock.html', {'message':message}) 
              
                      
            else:                
                new_item = models.stock.objects.create(itemname=itemname, 
                                                        itemspec=itemspec, 
                                                        safty_stock=saftystock,
                                                        sell_platform=platform,
                                                        sum_import=total_import,
                                                        sum_output=total_output,
                                                        stock=stock,
                                                        )                                       
         
        else:
            new_item = models.stock.objects.create(itemname=itemname, 
                                                    itemspec=itemspec, 
                                                    safty_stock=saftystock,
                                                    sell_platform=platform,
                                                    sum_import=total_import,
                                                    sum_output=total_output,
                                                    stock=stock, 
                                                    )                                                                                           
        
    
    return render(request,'stock/stock.html')                                        
                                            


def stockimport(request):
    
    if request.method =='POST':
        itemname_c = request.POST.get('itemname_c', None)
        print (itemname_c, type(itemname_c))
        itemname = request.POST.get('itemname', None)
        itemspec = request.POST.get('itemspec', None)
        stockimport = request.POST.get('import', None)

        if itemname_c :
            itemname_c = itemname_c.split(',')
            print(itemname_c, type(itemname_c))
            stock_data = models.stock.objects.filter(itemname__contains = itemname_c[0])

            return render(request, 'stock/import.html', {'stock_data':stock_data, 'itemname_c':itemname_c[0], 'itemspec_c':itemname_c[1]},)
        elif itemname and itemspec and stockimport:
            stockimport = int(stockimport)

            itemname_exist = models.stock.objects.filter(itemname=itemname)
            if itemname_exist:
                try:
                    item_get = models.stock.objects.get(itemname=itemname, itemspec=itemspec)
                except :
                    message = '商品規格不存在'
                    return render(request, 'stock/import.html', {'message':message, 'stock_data':stock_data})
                #print(item_get, item_get.itemspec)
                new_stock = item_get.stock + stockimport
                new_import = item_get.sum_import+stockimport
                safty_stock = item_get.safty_stock
                #print('safty_stock:', safty_stock)
                sell_platform = item_get.sell_platform
                #print('sell_platform:', sell_platform)
                sum_output = item_get.sum_output
                item_get.delete()
                new_item = models.stock.objects.create(itemname=itemname, 
                                                    itemspec=itemspec, 
                                                    safty_stock=safty_stock,
                                                    sell_platform=sell_platform,
                                                    sum_import=new_import,
                                                    sum_output=sum_output,                      
                                                    stock=new_stock,)
                stock_data = models.stock.objects.filter(itemname__contains = itemname)
                return render(request, 'stock/import.html', {'stock_data':stock_data, 'itemname_c':itemname, 'itemspec_c':itemspec})
                                                    
            else:
                message = '商品名稱不存在'     
                return render(request, 'stock/import.html', {'message':message, 'stock_data':stock_data} )                                    
        else:    
            return render(request, 'stock/import.html')
    else:    
        return render(request, 'stock/import.html')

def stockoutput (request):

    if request.method =='POST':
        itemname_c = request.POST.get('itemname_c', None)
        itemname = request.POST.get('itemname', None)
        itemspec = request.POST.get('itemspec', None)
        stockoutput = request.POST.get('output', None)
        
        print(itemname_c)
        if itemname_c :
            print('in item_C')
            itemname_c = itemname_c.split(',')
            stock_data = models.stock.objects.filter(itemname=itemname_c[0], itemspec=itemname_c[1])
            print(stock_data)
            return render (request, 'stock/output.html', {'stock_data':stock_data, 'itemname': itemname_c[0], 'itemspec':itemname_c[1]} )

        elif itemname :
            stockoutput = int(stockoutput)
            itemname_exist = models.stock.objects.filter(itemname=itemname)
            if itemname_exist:
                try :
                    item_get = models.stock.objects.get(itemname=itemname, itemspec=itemspec)
                except:
                    message = '商品規格不存在'
                    return render(request, 'stock/output.html', {'message':message} )
                new_stock = item_get.stock - stockoutput
                sum_import = item_get.sum_import
                safty_stock = item_get.safty_stock
                sell_platform = item_get.sell_platform
                new_output = item_get.sum_output+stockoutput
                item_get.delete()
                new_item = models.stock.objects.create(itemname=itemname, 
                                                    itemspec=itemspec, 
                                                    safty_stock=safty_stock,
                                                    sell_platform=sell_platform,
                                                    sum_import=sum_import,
                                                    sum_output=new_output,
                                                    stock=new_stock,)
                stock_data = models.stock.objects.filter(itemname=itemname, itemspec=itemname)
                return render(request, 'stock/output.html', {'stock_data':stock_data, 'itemname':itemname, 'itemspec':itemspec})
            else:
                message = '商品名稱不存在'     
                return render(request, 'stock/output.html', {'message':message})      
    print('wrong')
    return render(request, 'stock/output.html')   




def stocksheet(request):
    request.session['stock_name']=[]
    if request.method =='POST':
        
        itemname = request.POST.get('itemname', None)
        itemspec = request.POST.get('itemspec', None)
        itemname = itemname.strip()
        itemspec = itemspec.strip()
        itemname_exist = models.stock.objects.filter(itemname__contains=itemname)
        if itemname_exist:
            print(itemname_exist)
            itemspec_exist = models.stock.objects.filter(itemspec__contains=itemspec)
            if itemspec_exist:
                
                stock_data = models.stock.objects.filter(itemname__contains=itemname, itemspec__contains=itemspec, )
                #stock_data_get = models.stock.objects.get(itemname=itemname, itemspec=itemspec, )
                #print(stock_data_get.itemname)

                request.session['stock_name'] = itemname
            
                return render(request, 'stock/stocksheet.html',{'stock_data':stock_data})
            else:
                stock_data = models.stock.objects.filter(itemname__contains=itemname )
                
               
                

                request.session['stock_name'] = itemname
                
                return render(request, 'stock/stocksheet.html', {'stock_data':stock_data} )
        else:
            message_stock = '商品不存在'
            
            stock_data = models.stock.objects.all()
            
            return render(request, 'stock/stocksheet.html', {'message_stock':message_stock,  'stock_data':stock_data} )

  
    else:
        stock_data = models.stock.objects.all()
    
    # table = stockTable(models.stock.objects.all())
    # RequestConfig(request).configure(table)


    
    return render(request, 'stock/stocksheet.html',{'stock_data':stock_data} )                                            
                                            



def revise(request):

    if request.method == 'POST':
        itemname_c = request.POST.get('itemname_c', None)
        itemname = request.POST.get('itemname', None)
        itemspec = request.POST.get('itemspec', None)
        saftystock = request.POST.get('saftystock', '0')
        platform = request.POST.get('platform', None)
        total_import = request.POST.get('import', '0')
        total_output = request.POST.get('output', '0')
        stock = request.POST.get('stock', '0') 
        print(itemname_c)
        print(itemname, itemspec)

        if itemname_c:      
            itemname_c = itemname_c.split(',')
            print(itemname_c)        
            stock_data = models.stock.objects.filter(itemname = itemname_c[0], itemspec = itemname_c[1])
            return render(request, 'stock/revise.html', {'stock_data':stock_data, 'itemname':itemname_c[0], 'itemspec':itemname_c[1]})
        elif itemname:
            print('elif in')
            try :
                item_get = models.stock.objects.get(itemname=itemname, itemspec=itemspec)
            except:
                message = '商品不存在'
                return render (request, 'stock/revise.html', {'message':message, 'stock_data':stock_data, 'itemname':itemname, 'itemspec':itemspec})

            item_get.delete()
            new_item = models.stock.objects.create(itemname=itemname, 
                                                itemspec=itemspec, 
                                                safty_stock=saftystock,
                                                sell_platform=platform,
                                                sum_import=total_import,
                                                sum_output=total_output,
                                                stock=stock,)
            stock_data = models.stock.objects.filter(itemname = itemname, itemspec = itemspec)
            return render (request, 'stock/revise.html', {'stock_data':stock_data, 'itemname':itemname, 'itemspec':itemspec})

        return render (request, 'stock/revise.html', {'stock_data':stock_data, 'itemname':itemname, 'itemspec':itemspec})
   
    return render(request, 'stock/stocksheet.html')
                                            
                                     
    