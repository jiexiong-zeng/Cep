from django.template import Context, loader 
from django.http import HttpResponse 
from MySocialNetwork.models import User, UserLink
 
def index(request): 
  user_list = User.objects.all() 
  t = loader.get_template('MySocialNetwork/index.html') 
  c = Context({ 'user_list': user_list, }) 
  return HttpResponse(t.render(c)) 
 
def followers(request,username): 
  followers = UserLink.objects.filter(to_user__username = username) #UserLink.to_user.user
  t = loader.get_template('MySocialNetwork/followers.html') 
  c = Context({ 'followers': followers, }) 
  return HttpResponse(t.render(c))  

def following(request,username): 
  following = UserLink.objects.filter(from_user__username = username)
  t = loader.get_template('MySocialNetwork/following.html') 
  c = Context({ 'following': following, }) 
  return HttpResponse(t.render(c))  