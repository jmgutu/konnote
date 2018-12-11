from django.shortcuts import render, redirect

from staff.forms import StaffRegistrationForm, EditStaffForm
from budgets.models import Budget
from django.contrib.auth.models import User
from tasks.models import Task
from resources.models import Resource
from staff.models import Staff
import datetime
from django.contrib import auth, messages
from projects.models import Project
from activities.models import Activity
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required(login_url='/')
def calendar(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'custom-calendar.html', c)


# return HttpResponseRedirect('/', c)

@login_required(login_url='/')
def viewstaff(request):
    args = {}
    all_staff = Staff.objects.all()
    args['staff'] = all_staff
    return render(request, 'viewstaff.html', args)


@login_required(login_url='/')
def createstaff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            # Check to see if username exists
            # Cehck to see uif email exists
            user.save()

            s = Staff()
            s.user = user
            s.department = form.cleaned_data['department']
            s.no = form.cleaned_data['no']
            s.position = form.cleaned_data['position']
            s.role = form.cleaned_data['role']
            s.background = form.cleaned_data['background']
            s.save()
            return redirect('/staff/view/')
        else:
            args = {'form': form, 'email': 'test@email.com'}
            return render(request, 'createstaff.html', args)
    else:
        form = StaffRegistrationForm()
        args = {'form': form}
        return render(request, 'createstaff.html', args)


@login_required(login_url='/')
def editstaff(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    if request.method == 'POST':
        form = EditStaffForm(request.POST)
        if form.is_valid():

            staff.user.first_name = form.cleaned_data['first_name']
            staff.user.last_name = form.cleaned_data['last_name']
            staff.user.email = form.cleaned_data['email']
            staff.user.username = form.cleaned_data['username']
            staff.user.save()

            # staff.user = form.cleaned_data['user']
            staff.department = form.cleaned_data['department']
            staff.no = form.cleaned_data['no']
            staff.position = form.cleaned_data['position']
            staff.role = form.cleaned_data['role']
            staff.background = form.cleaned_data['background']

            staff.save()
            return redirect('/staff/view/')
        else:
            form = EditStaffForm(
                initial={
                    'first_name': staff.user.first_name,
                    'last_name': staff.user.last_name,
                    'username': staff.user.username,
                    'email': staff.user.email,
                    'no': staff.no,
                    'position': staff.position,
                    'department': staff.department,
                    'role': staff.role,
                    'background': staff.background,
                    'staffid': staff.id,
                })
            args = {'form': form}
            return render(request, 'editstaff.html', args)
    else:
        form = EditStaffForm(
            initial={
                'first_name': staff.user.first_name,
                'last_name': staff.user.last_name,
                'username': staff.user.username,
                'email': staff.user.email,
                'no': staff.no,
                'position': staff.position,
                'department': staff.department,
                'role': staff.role,
                'background': staff.background,
                'staffid': staff.id,
            })
        args = {'form': form}
        return render(request, 'editstaff.html', args)


@login_required(login_url='/')
def updatestaff(request):
    form = EditStaffForm(request.POST)
    if request.method == 'POST':
        staff = Staff.objects.get(pk=request.POST['staffid'])
        if form.is_valid():
            staff.user.first_name = form.cleaned_data['first_name']
            staff.user.last_name = form.cleaned_data['last_name']
            staff.user.email = form.cleaned_data['email']
            staff.user.username = form.cleaned_data['username']
            staff.user.save()

            staff.department = form.cleaned_data['department']
            staff.no = form.cleaned_data['no']
            staff.position = form.cleaned_data['position']
            staff.role = form.cleaned_data['role']
            staff.background = form.cleaned_data['background']
            staff.save()
            messages.success(request,
                             '<i class="fa fa-info-circle" aria-hidden="true"></i>&nbsp<b>Record Saved.</b>&nbspYou have successfully saved the Department.',
                             extra_tags="alert alert-success alert-dismissible fade show")
            return redirect('/staff/view/')
        else:
            form = EditStaffForm(
                initial={
                    'first_name': staff.user.first_name,
                    'last_name': staff.user.last_name,
                    'username': staff.user.username,
                    'email': staff.user.email,
                    'no': staff.no,
                    'position': staff.position,
                    'department': staff.department,
                    'role': staff.role,
                    'background': staff.background,
                    'staffid': staff.id,
                })
            args = {'form': form}
            return render(request, 'editstaff.html', args)
    else:
        messages.error(request,
                       '<i class="fa  fa-exclamation-triangle" aria-hidden="true"></i>&nbsp<b>No Data.</b>.&nbspThere seems to be no data in the form. Please try again.',
                       extra_tags="alert alert-success alert-dismissible fade show safe")
        return redirect('/staff/view/')


@login_required(login_url='/')
def deletestaff(request, staff_id):
    try:
        staff = Staff.objects.get(pk=staff_id)
    except ObjectDoesNotExist:
        staff = None
    if staff == None:
        messages.error(request,
                       '<i class="fa  fa-exclamation-triangle" aria-hidden="true"></i>&nbsp<b>No Such Record</b>.&nbspThat Record Does not exist.',
                       extra_tags="alert alert-danger alert-dismissible fade show safe")
        return redirect('/staff/view/')
    staff.delete()
    messages.error(request,
                   '<i class="fa  fa-exclamation-triangle" aria-hidden="true"></i>&nbsp<b>Record Deleted.</b>.&nbspThe Record has been successfully deleted.',
                   extra_tags="alert alert-success alert-dismissible fade show safe")
    return redirect('/staff/view/')

# b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
# b.save()
# b.name = "New Beatles"
# b.save()


# from blog.models import Blog, Entry
# entry = Entry.objects.get(pk=1)
# cheese_blog = Blog.objects.get(name="Cheddar Talk")
# entry.blog = cheese_blog
# entry.save()

# john = Author.objects.create(name="John")
# paul = Author.objects.create(name="Paul")
# george = Author.objects.create(name="George")
# ringo = Author.objects.create(name="Ringo")
# entry.authors.add(john, paul, george, ringo)

# Managers are accessible only via model classes, rather than from model instances, to enforce a separation between "table-level" operations and "record-level" operations.

# Blog.objects
# <django.db.models.manager.Manager object at ...>
# b = Blog(name='Foo', tagline='Bar')
# b.objects
# Traceback:
#    ...
# AttributeError: "Manager isn't accessible via Blog instances."

# All Objects
# all_entries = Entry.objects.all()


# filter(**kwargs)
#    Returns a new QuerySet containing objects that match the given lookup parameters.
# exclude(**kwargs)
#    Returns a new QuerySet containing objects that do not match the given lookup parameters. 


# Chaining Filters
#   Entry.objects.filter(
# ...     headline__startswith='What'
# ... ).exclude(
# ...     pub_date__gte=datetime.date.today()
# ... ).filter(
# ...     pub_date__gte=datetime.date(2005, 1, 30)
# ... )

# Retrieving a single object with get()
# one_entry = Entry.objects.get(pk=1)

# Note that there is a difference between using get(), and using filter() with a slice of [0]. If there are no results that match the query, get() will raise a DoesNotExist exception.

# Similarly, Django will complain if more than one item matches the get() query. In this case, it will raise MultipleObjectsReturned, which again is an attribute of the model class itself.

# Limit to 5
# Entry.objects.all()[:5]

# To retrieve a single object rather than a list (e.g. SELECT foo FROM bar LIMIT 1), use a simple index instead of a slice. For example, this returns the first Entry in the database, after ordering entries alphabetically by headline:


# Entry.objects.order_by('headline')[0]  >> Raises index error if empty

# Entry.objects.order_by('headline')[0:1].get() >> Raises DoesNotExist if no objects match the given criteria

# Field Lookups
# Entry.objects.filter(pub_date__lte='2006-01-01')

# Entry.objects.get(headline__contains='Lennon')

# Entry.objects.filter(blog__name='Beatles Blog')

# Blog.objects.filter(entry__authors__name__isnull=True)

# Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True) >> will return Blog objects that have an empty name on the author and also those which have an empty author on the entry. If you don't want those latter objects

# Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)

# Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)

# Filters can reference fields on the model

# if you want to compare the value of a model field with another field on the same model?
# from django.db.models import F
#  Entry.objects.filter(n_comments__gt=F('n_pingbacks'))

# An F() object represents the value of a model field or annotated column. It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.

# To find all the blog entries with more than twice as many comments as pingbacks, we modify the query:
# Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)

# To find all the entries where the rating of the entry is less than the sum of the pingback count and comment count
#  Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))

#  Entry.objects.filter(headline__contains='%')

# inefficient use
# >>> print([e.headline for e in Entry.objects.all()])
# >>> print([e.pub_date for e in Entry.objects.all()])


# more efficient as only one evaluation is done
# queryset = Entry.objects.all()
# print([p.headline for p in queryset]) # Evaluate the query set.
# print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation.


#  When evaluating only part of the queryset, the cache is checked, but if it is not populated then the items returned by the subsequent query are not cached. Specifically, this means that limiting the queryset using an array slice or an index will not populate the cache.

# Stopped here : https://docs.djangoproject.com/en/2.0/ref/models/querysets/
# Validations