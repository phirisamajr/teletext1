from django.shortcuts import render, get_object_or_404, redirect
from .forms import sarisfrm1tform, sarisfrm2tform, sarisfrm3tform, sarisfrm4tform, sarisfrm1form, sarisfrm2form, sarisfrm3form, sarisfrm4form, sarisstd1form, sarisstd2form, sarisstd3form, sarisstd4form, sarisstd5form, sarisstd6form, sarisstd7form, UserEditForm,  ProfileEditForm, PostForm, CommentForm, accform, FriendForm, CreateUserForm, Std1form, Std2form, Std3Form, Std4form, Std5form, Std6form, Std7form, FormOneform, FormTwoform, FormThreeform, FormFourform, FormOneTechform, FormTwoTechform, FormThreeTechform, FormFourTechform, EGM5form, staffform, forms, UserForm
from .models import *
from .models import Staff, Profile, Post, Comment, Friend, User, FormOne, FormTwo, FormThree, FormFour, FormOneTech, FormTwoTech, FormThreeTech, FormFourTech
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_usered, allowed_users, admin_only, access_permissions
from django.contrib.auth.models import Group
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model
from tablib import Dataset


User = get_user_model()





# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    friends = User.objects.exclude(id=request.user.id)
    context= {'friends':friends}
    return render(request, 'student_results/dashboard.html', context)

@login_required(login_url='login')
@admin_only
def apload_excel(request):
    if request.method == 'POST':
        std1_form = Std1form()
        dataset =Dataset()
        new_std1 = request.FILES['myfile']
        
        if not new_std1.name.endswith('xlsx'):
            messages.info(request, 'invalid file format')
            return render(request, 'apload_excel.html')

        imported_data = dataset.load(new_std1.read(), format='xlsx')
        for data in imported_data:
            value = Std1(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[14],
                data[15],
                data[16],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],
            )
            value.save()    
    context= {}
    return render(request, 'student_results/apload_excel.html', context)


@login_required(login_url='login')
def saris_page(request): 
    context= {}    
    return render(request, 'student_results/saris.html', context)


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)


    context= {'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'student_results/edit_profile.html', context)


@login_required(login_url='login')
def profile(request):
    context= {}
    return render(request, 'student_results/profile.html', context)


@login_required(login_url='login')
@admin_only
def PostPage(request):
    posts = Post.objects.filter(user=request.user).order_by('-created')
    args= {'posts':posts}
    return render(request, 'student_results/post.html', args)

@login_required(login_url='login')
def PostPageDetail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post).order_by('-created')
    
    if request.method =='POST':
        comment_form = CommentForm(request.POST or None)               
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post, user=request.user, content=content)
            comment.save()
            return redirect('PostPageDetail', post.id)
    else:
        comment_form = CommentForm()
    args= {'post':post, 'comments':comments, 'comment_form':comment_form,}
    return render(request, 'student_results/post_detail.html', args)



@login_required(login_url='login')
@admin_only
def addpostpage(request, pk):
    user = User.objects.get(id=pk)
    form = PostForm(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PostPage')
    context= {'form':form}
    return render(request, 'student_results/postadd.html', context)



@login_required(login_url='login')
def SearchFriend(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = User.objects.filter(Q(email__iexact=srch))  
            if match:
                return render(request, 'student_results/searchfriends.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/searchfriends/')                     
    return render(request, "student_results/searchfriends.html")

@login_required(login_url='login')
def FriendPage(request):
    user = User.objects.all()
    user = Friend.objects.all()
    form = FriendForm(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    friend = Friend.objects.get(user=request.user)
    friends = friend.friends.all()
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FriendPage')
    args= {'form':form, 'friends':friends, 'friend':friend}
    return render(request, 'student_results/friends.html', args)

@login_required(login_url='login')
@admin_only
def techschool_page(request):
    friends = User.objects.exclude(id=request.user.id)
    args = {
        'friends':friends
        } 
    return render(request, 'student_results/tschools_form.html', args)

@login_required(login_url='login')
@admin_only
def plevel_page(request):
    friends = User.objects.exclude(id=request.user.id)
    args = {
        'friends':friends
        } 
    return render(request, 'student_results/plevel_form.html', args)

@login_required(login_url='login')
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
       Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('FriendPage')

@login_required(login_url='login')
@admin_only
def secondary_page(request): 
    context= {}    
    return render(request, 'student_results/slevel.html', context)

@login_required(login_url='login')
@admin_only
def egm5_list(request):   
    egm5s = request.user.egm5_set.all()
    total_results = egm5s.count()
    passed = egm5s.filter(discriptions='Passed').count()
    failed = egm5s.filter(discriptions='Failed').count()
    context= {'egm5s':egm5s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/egmfive.html', context)

@login_required(login_url='login')
@admin_only
def EGM5Page(request, pk):
    user = User.objects.get(id=pk)
    form = EGM5form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = EGM5form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('egm5_list')

    context= {'form':form}
    return render(request, 'student_results/egmfiveadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteEGM5(request, pk):
	egm5 = EGM5.objects.get(id=pk)
	if request.method == "POST":
		egm5.delete()
		return redirect('egm5_list')

	context = {'item':egm5}
	return render(request, 'student_results/deletef5egm.html', context)

@login_required(login_url='login')
@admin_only
def updateEGM5(request, pk):    
    egm5 = EGM5.objects.get(id=pk)
    form = EGM5form(instance=egm5)
    if request.method == 'POST':
        form = EGM5form(request.POST, instance=egm5)
        if form.is_valid():
            form.save()
            return redirect('egm5_list')
    context= {'form':form}
    return render(request, 'student_results/egmfiveadd.html', context)



@login_required(login_url='login')
@admin_only
def formfourtech_list(request):   
    formfourtechs = request.user.formfourtech_set.all()
    total_results = formfourtechs.count()
    passed = formfourtechs.filter(discriptions='Passed').count()
    failed = formfourtechs.filter(discriptions='Failed').count()
    context= {'formfourtechs':formfourtechs, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formfourtech.html', context)

@login_required(login_url='login')
@admin_only
def FormfourTechPage(request, pk):
    user = User.objects.get(id=pk)
    form = FormFourTechform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormFourTechform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formfourtech_list')

    context= {'form':form}
    return render(request, 'student_results/formfourtechadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormFourTech(request, pk):
	formfourtech = FormFourTech.objects.get(id=pk)
	if request.method == "POST":
		formfourtech.delete()
		return redirect('formfourtech_list')

	context = {'item':formfourtech}
	return render(request, 'student_results/deletef4t.html', context)

@login_required(login_url='login')
@admin_only
def updateFormFourTech(request, pk):    
    formfourtech = FormFourTech.objects.get(id=pk)
    form = FormFourTechform(instance=formfourtech)
    if request.method == 'POST':
        form = FormFourTechform(request.POST, instance=formfourtech)
        if form.is_valid():
            form.save()
            return redirect('formfourtech_list')
    context= {'form':form}
    return render(request, 'student_results/formfourtechadd.html', context)

@login_required(login_url='login')
@admin_only
def formthreetech_list(request):   
    formthreetechs = request.user.formthreetech_set.all()
    total_results = formthreetechs.count()
    passed = formthreetechs.filter(discriptions='Passed').count()
    failed = formthreetechs.filter(discriptions='Failed').count()
    context= {'formthreetechs':formthreetechs, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formthreetech.html', context)

@login_required(login_url='login')
@admin_only
def FormthreeTechPage(request, pk):
    user = User.objects.get(id=pk)
    form = FormThreeTechform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormThreeTechform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formthreetech_list')

    context= {'form':form}
    return render(request, 'student_results/formthreetechadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormThreeTech(request, pk):
	formthreetech = FormThreeTech.objects.get(id=pk)
	if request.method == "POST":
		formthreetech.delete()
		return redirect('formthreetech_list')

	context = {'item':formthreetech}
	return render(request, 'student_results/deletef3t.html', context)

@login_required(login_url='login')
@admin_only
def updateFormThreeTech(request, pk):    
    formthreetech = FormThreeTech.objects.get(id=pk)
    form = FormThreeTechform(instance=formthreetech)
    if request.method == 'POST':
        form = FormThreeTechform(request.POST, instance=formthreetech)
        if form.is_valid():
            form.save()
            return redirect('formthreetech_list')
    context= {'form':form}
    return render(request, 'student_results/formthreetechadd.html', context)


@login_required(login_url='login')
@admin_only
def formtwotech_list(request):   
    formtwotechs = request.user.formtwotech_set.all()
    total_results = formtwotechs.count()
    passed = formtwotechs.filter(discriptions='Passed').count()
    failed = formtwotechs.filter(discriptions='Failed').count()
    context= {'formtwotechs':formtwotechs, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formtwotech.html', context)

@login_required(login_url='login')
@admin_only
def FormtwoTechPage(request, pk):
    user = User.objects.get(id=pk)
    form = FormTwoTechform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormTwoTechform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formtwotech_list')

    context= {'form':form}
    return render(request, 'student_results/formtwotechadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormTwoTech(request, pk):
	formtwotech = FormTwoTech.objects.get(id=pk)
	if request.method == "POST":
		formtwotech.delete()
		return redirect('formtwotech_list')

	context = {'item':formtwotech}
	return render(request, 'student_results/deletef2t.html', context)

@login_required(login_url='login')
@admin_only
def updateFormTwoTech(request, pk):    
    formtwotech = FormTwoTech.objects.get(id=pk)
    form = FormTwoTechform(instance=formtwotech)
    if request.method == 'POST':
        form = FormTwoTechform(request.POST, instance=formtwotech)
        if form.is_valid():
            form.save()
            return redirect('formtwotech_list')
    context= {'form':form}
    return render(request, 'student_results/formtwotechadd.html', context)

@login_required(login_url='login')
@admin_only
def formonetech_list(request):   
    formonetechs = request.user.formonetech_set.all()
    total_results = formonetechs.count()
    passed = formonetechs.filter(discriptions='Passed').count()
    failed = formonetechs.filter(discriptions='Failed').count()
    context= {'formonetechs':formonetechs, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formonetech.html', context)

@login_required(login_url='login')
@admin_only
def FormoneTechPage(request, pk):
    user = User.objects.get(id=pk)
    form = FormOneTechform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormOneTechform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formonetech_list')

    context= {'form':form}
    return render(request, 'student_results/formonetechadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormOneTech(request, pk):
	formonetech = FormOneTech.objects.get(id=pk)
	if request.method == "POST":
		formonetech.delete()
		return redirect('formonetech_list')

	context = {'item':formonetech}
	return render(request, 'student_results/deletef1t.html', context)

@login_required(login_url='login')
@admin_only
def updateFormOneTech(request, pk):    
    formonetech = FormOneTech.objects.get(id=pk)
    form = FormOneTechform(instance=formonetech)
    if request.method == 'POST':
        form = FormOneTechform(request.POST, instance=formonetech)
        if form.is_valid():
            form.save()
            return redirect('formonetech_list')
    context= {'form':form}
    return render(request, 'student_results/formonetechadd.html', context)

@login_required(login_url='login')
@admin_only
def formfour_list(request):   
    formfours = request.user.formfour_set.all()
    total_results = formfours.count()
    passed = formfours.filter(discriptions='Passed').count()
    failed = formfours.filter(discriptions='Failed').count()
    context= {'formfours':formfours, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formfour.html', context)

@login_required(login_url='login')
@admin_only
def FormfourPage(request, pk):
    user = User.objects.get(id=pk)
    form = FormFourform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormFourform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formfour_list')

    context= {'form':form}
    return render(request, 'student_results/formfouradd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormFour(request, pk):
	formfour = FormFour.objects.get(id=pk)
	if request.method == "POST":
		formfour.delete()
		return redirect('formfour_list')

	context = {'item':formfour}
	return render(request, 'student_results/deletef4.html', context)

@login_required(login_url='login')
@admin_only
def updateFormFour(request, pk):    
    formfour = FormFour.objects.get(id=pk)
    form = FormFourform(instance=formfour)
    if request.method == 'POST':
        form = FormFourform(request.POST, instance=formfour)
        if form.is_valid():
            form.save()
            return redirect('formfour_list')
    context= {'form':form}
    return render(request, 'student_results/formfouradd.html', context)

@login_required(login_url='login')
@admin_only
def formthree_list(request):   
    formthrees = request.user.formthree_set.all()
    total_results = formthrees.count()
    passed = formthrees.filter(discriptions='Passed').count()
    failed = formthrees.filter(discriptions='Failed').count()
    context= {'formthrees':formthrees, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formthree.html', context)

@login_required(login_url='login')
@admin_only
def FormthreePage(request, pk):
    user = User.objects.get(id=pk)
    form = FormThreeform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormThreeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formthree_list')

    context= {'form':form}
    return render(request, 'student_results/formthreeadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormThree(request, pk):
	formthree = FormThree.objects.get(id=pk)
	if request.method == "POST":
		formthree.delete()
		return redirect('formthree_list')

	context = {'item':formthree}
	return render(request, 'student_results/deletef3.html', context)

@login_required(login_url='login')
@admin_only
def updateFormThree(request, pk):    
    formthree = FormThree.objects.get(id=pk)
    form = FormThreeform(instance=formthree)
    if request.method == 'POST':
        form = FormThreeform(request.POST, instance=formthree)
        if form.is_valid():
            form.save()
            return redirect('formthree_list')
    context= {'form':form}
    return render(request, 'student_results/formthreeadd.html', context)

@login_required(login_url='login')
@admin_only
def formtwo_list(request):   
    formtwos = request.user.formtwo_set.all()
    total_results = formtwos.count()
    passed = formtwos.filter(discriptions='Passed').count()
    failed = formtwos.filter(discriptions='Failed').count()
    context= {'formtwos':formtwos, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formtwo.html', context)


def FormtwoPage(request, pk):
    user = User.objects.get(id=pk)
    form = FormTwoform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormTwoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formtwo_list')

    context= {'form':form}
    return render(request, 'student_results/formtwoadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormTwo(request, pk):
	formtwo = FormTwo.objects.get(id=pk)
	if request.method == "POST":
		formtwo.delete()
		return redirect('formtwo_list')

	context = {'item':formtwo}
	return render(request, 'student_results/deletef2.html', context)

@login_required(login_url='login')
@admin_only
def updateFormTwo(request, pk):    
    formtwo = FormTwo.objects.get(id=pk)
    form = FormTwoform(instance=formtwo)
    if request.method == 'POST':
        form = FormTwoform(request.POST, instance=formtwo)
        if form.is_valid():
            form.save()
            return redirect('formtwo_list')
    context= {'form':form}
    return render(request, 'student_results/formtwoadd.html', context)

@login_required(login_url='login')
@admin_only
def formone_list(request):   
    formones = request.user.formone_set.all()
    total_results = formones.count()
    passed = formones.filter(discriptions='Passed').count()
    failed = formones.filter(discriptions='Failed').count()
    context= {'formones':formones, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/formone.html', context)

@login_required(login_url='login')
@admin_only
def FormonePage(request, pk):
    user = User.objects.get(id=pk)
    form = FormOneform(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = FormOneform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formone_list')

    context= {'form':form}
    return render(request, 'student_results/formoneadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteFormOne(request, pk):
	formone = FormOne.objects.get(id=pk)
	if request.method == "POST":
		formone.delete()
		return redirect('formone_list')

	context = {'item':formone}
	return render(request, 'student_results/deletef1.html', context)

@login_required(login_url='login')
@admin_only
def updateFormOne(request, pk):    
    formone = FormOne.objects.get(id=pk)
    form = FormOneform(instance=formone)
    if request.method == 'POST':
        form = FormOneform(request.POST, instance=formone)
        if form.is_valid():
            form.save()
            return redirect('formone_list')
    context= {'form':form}
    return render(request, 'student_results/formoneadd.html', context)

@login_required(login_url='login')
@admin_only
def std1_list(request):   
    std1s = request.user.std1_set.all()
    total_results = std1s.count()
    passed = std1s.filter(discriptions='Passed').count()
    failed = std1s.filter(discriptions='Failed').count()
    context= {'std1s':std1s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/standardone.html', context)

@login_required(login_url='login')
@admin_only
def std1Page(request, pk):
    user = User.objects.get(id=pk)
    form = Std1form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = Std1form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std1_list')

    context= {'form':form}
    return render(request, 'student_results/standardoneadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteStd1(request, pk):
	std1 = Std1.objects.get(id=pk)
	if request.method == "POST":
		std1.delete()
		return redirect('std1_list')

	context = {'item':std1}
	return render(request, 'student_results/delete1.html', context)

@login_required(login_url='login')
@admin_only
def updateStd1(request, pk):    
    std1 = Std1.objects.get(id=pk)
    form = Std1form(instance=std1)
    if request.method == 'POST':
        form = Std1form(request.POST, instance=std1)
        if form.is_valid():
            form.save()
            return redirect('std1_list')
    context= {'form':form}
    return render(request, 'student_results/standardoneadd.html', context)


@login_required(login_url='login')
@admin_only
def std2_list(request):   
    std2s = request.user.std2_set.all()
    total_results = std2s.count()
    passed = std2s.filter(discriptions='Passed').count()
    failed = std2s.filter(discriptions='Failed').count()
    context= {'std2s':std2s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/standardtwo.html', context)

@login_required(login_url='login')
@admin_only
def std2Page(request, pk):
    user = User.objects.get(id=pk)
    form = Std2form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = Std2form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std2_list')

    context= {'form':form}
    return render(request, 'student_results/standardtwoadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteStd2(request, pk):
	std2 = Std2.objects.get(id=pk)
	if request.method == "POST":
		std2.delete()
		return redirect('std2_list')

	context = {'item':std2}
	return render(request, 'student_results/delete2.html', context)

@login_required(login_url='login')
@admin_only
def updateStd2(request, pk):    
    std2 = Std2.objects.get(id=pk)
    form = Std2form(instance=std2)
    if request.method == 'POST':
        form = Std2form(request.POST, instance=std2)
        if form.is_valid():
            form.save()
            return redirect('std2_list')
    context= {'form':form}
    return render(request, 'student_results/standardtwoadd.html', context)



@login_required(login_url='login')
@admin_only
def deleteStd3(request, pk):
	std3 = Std3.objects.get(id=pk)
	if request.method == "POST":
		std3.delete()
		return redirect('std3_list')

	context = {'item':std3}
	return render(request, 'student_results/delete.html', context)

@login_required(login_url='login')
@admin_only
def updateStd3(request, pk):    
    std3 = Std3.objects.get(id=pk)
    form = Std3Form(instance=std3)
    if request.method == 'POST':
        form = Std3Form(request.POST, instance=std3)
        if form.is_valid():
            form.save()
            return redirect('std3_list')
    context= {'form':form}
    return render(request, 'student_results/standardthreeadd.html', context)


@login_required(login_url='login')
@admin_only
def std3Page(request, pk):
    user = User.objects.get(id=pk)
    form = Std3Form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = Std3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std3_list')

    context= {'form':form}
    return render(request, 'student_results/standardthreeadd.html', context)

@login_required(login_url='login')
@admin_only
def std3_list(request):   
    std3s = request.user.std3_set.all()
    total_results = std3s.count()
    passed = std3s.filter(discriptions='Passed').count()
    failed = std3s.filter(discriptions='Failed').count()
    context= {'std3s':std3s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/standardthree.html', context)

@login_required(login_url='login')
@admin_only
def std3_delete(request, pk):
    std3 = Std3.objects.get(pk=id)
    std3.delete()
    return redirect("/list")

@login_required(login_url='login')
@admin_only
def std4_list(request):   
    std4s = request.user.std4_set.all()
    total_results = std4s.count()
    passed = std4s.filter(discriptions='Passed').count()
    failed = std4s.filter(discriptions='Failed').count()
    context= {'std4s':std4s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/standardfour.html', context)


@login_required(login_url='login')
@admin_only
def std4Page(request, pk):
    user = User.objects.get(id=pk)
    form = Std4form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = Std4form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std4_list')

    context= {'form':form}
    return render(request, 'student_results/standardfouradd.html', context)

@login_required(login_url='login')
@admin_only
def deleteStd4(request, pk):
	std4 = Std4.objects.get(id=pk)
	if request.method == "POST":
		std4.delete()
		return redirect('std4_list')

	context = {'item':std4}
	return render(request, 'student_results/delete4.html', context)

@login_required(login_url='login')
@admin_only
def updateStd4(request, pk):    
    std4 = Std4.objects.get(id=pk)
    form = Std4form(instance=std4)
    if request.method == 'POST':
        form = Std4form(request.POST, instance=std4)
        if form.is_valid():
            form.save()
            return redirect('std4_list')
    context= {'form':form}
    return render(request, 'student_results/standardfouradd.html', context)


@login_required(login_url='login')
@admin_only
def std5_list(request):   
    std5s = request.user.std5_set.all()
    total_results = std5s.count()
    passed = std5s.filter(discriptions='Passed').count()
    failed = std5s.filter(discriptions='Failed').count()
    context= {'std5s':std5s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/standardfive.html', context)


@login_required(login_url='login')
@admin_only
def std5Page(request, pk):
    user = User.objects.get(id=pk)
    form = Std5form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = Std5form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std5_list')

    context= {'form':form}
    return render(request, 'student_results/standardfiveadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteStd5(request, pk):
	std5 = Std5.objects.get(id=pk)
	if request.method == "POST":
		std5.delete()
		return redirect('std5_list')

	context = {'item':std5}
	return render(request, 'student_results/delete5.html', context)

@login_required(login_url='login')
@admin_only
def updateStd5(request, pk):    
    std5 = Std5.objects.get(id=pk)
    form = Std5form(instance=std5)
    if request.method == 'POST':
        form = Std5form(request.POST, instance=std5)
        if form.is_valid():
            form.save()
            return redirect('std5_list')
    context= {'form':form}
    return render(request, 'student_results/standardfiveadd.html', context)


@login_required(login_url='login')
@admin_only
def std6_list(request):   
    std6s = request.user.std6_set.all()
    total_results = std6s.count()
    passed = std6s.filter(discriptions='Passed').count()
    failed = std6s.filter(discriptions='Failed').count()
    context= {'std6s':std6s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/standardsix.html', context)

@login_required(login_url='login')
@admin_only
def std6Page(request, pk):
    user = User.objects.get(id=pk)
    form = Std6form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = Std6form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std6_list')

    context= {'form':form}
    return render(request, 'student_results/standardsixadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteStd6(request, pk):
	std6 = Std6.objects.get(id=pk)
	if request.method == "POST":
		std6.delete()
		return redirect('std6_list')

	context = {'item':std6}
	return render(request, 'student_results/delete6.html', context)

@login_required(login_url='login')
@admin_only
def updateStd6(request, pk):    
    std6 = Std6.objects.get(id=pk)
    form = Std6form(instance=std6)
    if request.method == 'POST':
        form = Std6form(request.POST, instance=std6)
        if form.is_valid():
            form.save()
            return redirect('std6_list')
    context= {'form':form}
    return render(request, 'student_results/standardsixadd.html', context)

@login_required(login_url='login')
@admin_only
def std7_list(request):   
    std7s = request.user.std7_set.all()
    total_results = std7s.count()
    passed = std7s.filter(discriptions='Passed').count()
    failed = std7s.filter(discriptions='Failed').count()
    context= {'std7s':std7s, 'total_results':total_results, 'passed':passed, 'failed':failed}
    return render(request, 'student_results/standardseven.html', context)

@login_required(login_url='login')
@admin_only
def std7Page(request, pk):
    user = User.objects.get(id=pk)
    form = Std7form(initial={'user':user})
    form.fields['user'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = Std7form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std7_list')

    context= {'form':form}
    return render(request, 'student_results/standardsevenadd.html', context)

@login_required(login_url='login')
@admin_only
def deleteStd7(request, pk):
	std7 = Std7.objects.get(id=pk)
	if request.method == "POST":
		std7.delete()
		return redirect('std7_list')
	context = {'item':std7}
	return render(request, 'student_results/delete7.html', context)

@login_required(login_url='login')
@admin_only
def updateStd7(request, pk):    
    std7 = Std7.objects.get(id=pk)
    form = Std7form(instance=std7)
    if request.method == 'POST':
        form = Std7form(request.POST, instance=std7)
        if form.is_valid():
            form.save()
            return redirect('std7_list')
    context= {'form':form}
    return render(request, 'student_results/standardsevenadd.html', context)

@login_required(login_url='login')
def sarisfrm4t(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormFourTech.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm4t.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm4t/')                    
    return render(request, "student_results/sarisfrm4t.html")


@login_required(login_url='login')
def sarisfrm3t(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormThreeTech.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm3t.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm3t/')                    
    return render(request, "student_results/sarisfrm3t.html")


@login_required(login_url='login')
def sarisfrm2t(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormTwoTech.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm2t.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm2t/')                    
    return render(request, "student_results/sarisfrm2t.html")


@login_required(login_url='login')
def sarisfrm1t(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormOneTech.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm1t.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm1t/')                    
    return render(request, "student_results/sarisfrm1t.html")


@login_required(login_url='login')
def sarisfrm4(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormFour.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm4.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm4/')                    
    return render(request, "student_results/sarisfrm4.html")


@login_required(login_url='login')
def sarisfrm3(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormThree.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm3.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm3/')                    
    return render(request, "student_results/sarisfrm3.html")


@login_required(login_url='login')
def sarisfrm2(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormTwo.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm2.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm2/')                    
    return render(request, "student_results/sarisfrm2.html")


@login_required(login_url='login')
def sarisfrm1(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = FormOne.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisfrm1.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisfrm1/')                    
    return render(request, "student_results/sarisfrm1.html")


@login_required(login_url='login')
def sarisstd1(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Std1.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisstd1.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisstd1/')                    
    return render(request, "student_results/sarisstd1.html")

@login_required(login_url='login')
def sarisstd2(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Std2.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisstd2.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisstd2/')                    
    return render(request, "student_results/sarisstd2.html")


@login_required(login_url='login')
def sarisstd3(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Std3.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisstd3.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisstd3/')                    
    return render(request, "student_results/sarisstd3.html")

@login_required(login_url='login')
def sarisstd4(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Std4.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisstd4.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisstd4/')                    
    return render(request, "student_results/sarisstd4.html")

@login_required(login_url='login')
def sarisstd5(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Std5.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisstd5.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisstd5/')                    
    return render(request, "student_results/sarisstd5.html")

@login_required(login_url='login')
def sarisstd6(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Std6.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisstd6.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisstd6/')                    
    return render(request, "student_results/sarisstd6.html")

@login_required(login_url='login')
def sarisstd7(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Std7.objects.filter(Q(candidate_NO__iexact=srch))  
            if match:
                return render(request, 'student_results/sarisstd7.html', {'sr':match}) 
            else:
                messages.error(request, 'Hakuna Matokeo')
        else:
            return HttpResponseRedirect('/sarisstd7/')                    
    return render(request, "student_results/sarisstd7.html")

@unauthenticated_usered
def loginPage(request):     
    if request.user.is_authenticated:
        return redirect('home')
    else:            
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Email or Password is Incorrect')
        context = {}              
        return render(request, 'student_results/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userPage(request):
    posts = Post.objects.filter(user__friend__user=request.user).order_by('-created')    
    context = {'posts':posts}
    return render(request, 'student_results/user.html', context)

@login_required(login_url='login')
def aboutPage(request):
    context = {}
    return render(request, 'student_results/about.html', context)

@login_required(login_url='login')
def donationPage(request):
    context = {}
    return render(request, 'student_results/donate.html', context)


@login_required(login_url='login')
@admin_only
def updatePost(request, pk):    
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('PostPage')
    context= {'form':form}
    return render(request, 'student_results/postadd.html', context)


@login_required(login_url='login')
@admin_only
def deletePost(request, pk):
	post = Post.objects.get(id=pk)
	if request.method == "POST":
		post.delete()
		return redirect('PostPage')

	context = {'item':post}
	return render(request, 'student_results/deletepost.html', context)

def primaryregisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name = 'primary')
            user.groups.add(group)            
            messages.success(request, 'Account was created for  ' + email)
            return redirect('login')
    context = {'form':form}
    return render(request, 'student_results/plevelregister.html', context)

def secondaryregisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name = 'secondary')
            user.groups.add(group)            
            messages.success(request, 'Account was created for  ' + email)
            return redirect('login')
    context = {'form':form}
    return render(request, 'student_results/olevel_register.html', context)

def techschoolregisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name = 'techschool')
            user.groups.add(group)            
            messages.success(request, 'Account was created for  ' + email)
            return redirect('login')
    context = {'form':form}
    return render(request, 'student_results/techschoolregister.html', context)



@unauthenticated_usered   
def signupPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)            
            messages.success(request, 'Account was created for  ' + email)
            return redirect('login')
    context = {'form':form}

    return render(request, 'student_results/signup.html', context)

       