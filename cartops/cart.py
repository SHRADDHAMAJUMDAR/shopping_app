from store.models import Product, UserProfile


class Cart:
    def __init__(self,request):
        self.session=request.session
        self.request=request
        #if a session already exists then grab the session parameter
        cart=self.session.get('session_key')
        #if the user is new then no session key exists so create a new empty session key
        if 'session_key' not in request.session:

            cart=self.session['session_key']={}
    
        #make the cart available on all pages of the site- with the help of context processor
        self.cart=cart


    def add_item(self,prod_id,prod_qty):
        prod_id=str(prod_id)
        if prod_id in self.cart:
            pass
        else:
            self.cart[prod_id]=int(prod_qty)
        self.session.modified=True

        if self.request.user.is_authenticated:
            currentuser=UserProfile.objects.filter(user__id=self.request.user.id)
            strcart=str(self.cart)
            strcart=strcart.replace("\'","\"")
            currentuser.update(oldcart=strcart)

#overwrite the default len() to find no. of items in the cart
    def __len__(self):
       # return len(self.cart)
        q=0
        for key  in self.cart:
            q=q+self.cart[key]
        return q
    
    def getprodlist(self):
        prodids=self.cart.keys()  #get the list of prodyct ids
        prodlist=Product.objects.filter(p_id__in=prodids)
        return prodlist
    
    def getprodqty(self):
        return self.cart
    
    def totalprice(self):
        prodids=self.cart.keys()  #get the list of prodyct ids
        prodlist=Product.objects.filter(p_id__in=prodids)
        cost=0
        for p in prodlist:
            prc=p.saleprice if p.on_sale else p.p_price
            cost+=prc*self.cart[str(p.p_id)]
        return cost
    
    def updateprodqty(self,prodid,pqty):
        prodid=str(prodid)
        self.cart[prodid]=int(pqty)
        self.session.modified=True

        if self.request.user.is_authenticated:
            currentuser=UserProfile.objects.filter(user__id=self.request.user.id)
            strcart=str(self.cart)
            strcart=strcart.replace("\'","\"")
            currentuser.update(oldcart=strcart)


    def delcart(self,prodid):
        prodid=str(prodid)
        if prodid in self.cart:
          del self.cart[prodid]
        self.session.modified=True

        if self.request.user.is_authenticated:
            currentuser=UserProfile.objects.filter(user__id=self.request.user.id)
            strcart=str(self.cart)
            strcart=strcart.replace("\'","\"")
            currentuser.update(oldcart=strcart)

    
    def updatecartfromdb(self,prodid,pqty):
        self.cart[str(prodid)]=int(pqty)
        self.session.modified=True


        if self.request.user.is_authenticated:
            currentuser=UserProfile.objects.filter(user__id=self.request.user.id)
            strcart=str(self.cart)
            strcart=strcart.replace("\'","\"")
            currentuser.update(oldcart=strcart)

        
    
