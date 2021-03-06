from django.shortcuts import render,redirect
from django.http import JsonResponse
from  user.utils import login_required
from .models import CartModel
from common.common import cart_count_goods
# Create your views here.

@login_required
def cart(request):
    """购物车"""
    user_id = request.session['user_id']

    carts = CartModel.objects.filter(user_id=user_id)
    return render(request,'cart/cart.html',{'carts':carts,'title':'购物车'})

@login_required
def add(request,goods_id,count):
    user_id =request.session['user_id']
    # 查询购物车中是否已经有
    carts =CartModel.objects.filter(user_id=user_id,goods_id=goods_id)
    if len(carts)>=1:
        cart = carts[0]
        cart.count = cart.count + count

    else:
        cart=CartModel()
        cart.user_id=user_id
        cart.goods_id=goods_id
        cart.count=count
    cart.save()
    # 如果是Ajax请求则返回一段json否则转向购物车
    if request.is_ajax():
        cart_count=cart_count_goods(request,CartModel)
        return JsonResponse({'cart_count':cart_count})
    return redirect('/cart/')


@login_required
def  delete(request,cart_id):
    """从购物车中删除某商品"""
    cart = CartModel.objects.get(id=cart_id)
    cart.delete()
    # 后端尽量不传给前端bool类型的数据，后端不接受前端传来的bool类型
    return JsonResponse({'success':1})


@login_required
def update(request,cart_id,count):
    """更新购物车内商品的数量"""
    cart = CartModel.objects.get(id=cart_id)
    cart.count=count
    cart.save()
    return JsonResponse({'success':1})
