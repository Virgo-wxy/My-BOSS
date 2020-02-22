from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render
# 连接mongodb
from pymongo import MongoClient

cli = MongoClient('localhost', 27017)
db = cli.boss
Liepin = db.liepin
Liepin_overseas = db.liepin_overseas
Company_detail = db.company_detail
Liepin_community = db.liepin_community


'''首页'''
def index(request):
    return render_to_response('MyBoss/index.html')


'''全部职位'''
def liepin(request):
    result = Company_detail.find()
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:
        book_list.append(x)

    # 将数据按照规定每页显示 15 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})


'''地点'''
def local_bj(request):
    result = Company_detail.find({'site': {'$regex': ".*北京.*"}})
    count = result.count
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})
def local_sh(request):
    result = Company_detail.find({'site': {'$regex': ".*上海.*"}})
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})
def local_gz(request):
    result = Company_detail.find({'site': {'$regex': '.*广州.*'}})
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})
def local_sz(request):
    result = Company_detail.find({'site': {'$regex': '深圳.*'}})
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})


'''学历'''
def condition_bx(request):
    result = Company_detail.find({'release_time': {'$regex': ".*不限.*"}})
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})
def condition_dz(request):
    result = Company_detail.find({'release_time': {'$regex': ".*大专.*"}})
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})
def condition_bk(request):
    result = Company_detail.find({'release_time': {'$regex': ".*本科.*"}})
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})
def condition_ss(request):
    result = Company_detail.find({'release_time': {'$regex': ".*硕士.*"}})
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/liepin.html', {'books': books,'count':count})


'''海外招聘'''
def liepin_overseas(request):
    image = Liepin_overseas.find()
    return render_to_response('MyBoss/liepin_overseas.html', {'image': image})


'''公司详情'''
def company_detail(request):
    result = Liepin.find()
    count = result.count()
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    for x in result:  # 一共 25 本书
        book_list.append(x)

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 15)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    return render(request, 'MyBoss/company_position.html', {'books': books,'count':count})


'''社区'''
def liepin_community(request):
    result = Liepin_community.find()
    return render_to_response('MyBoss/liepin_community.html', {'result': result})

def test(request):
    result1 = Company_detail.find({'site': {'$regex': ".*北京.*"}}).count()
    result2 = Company_detail.find({'site': {'$regex': ".*上海.*"}}).count()
    result3 = Company_detail.find({'site': {'$regex': ".*广州.*"}}).count()
    result4 = Company_detail.find({'site': {'$regex': ".*深圳.*"}}).count()
    return render(request,'MyBoss/test.html',{'result1': result1,'result2': result2,'result3': result3,'result4': result4,})


def test2(request):
    result1 = Company_detail.find({'release_time': {'$regex': ".*不限.*"}}).count()
    result2 = Company_detail.find({'release_time': {'$regex': ".*大专.*"}}).count()
    result3 = Company_detail.find({'release_time': {'$regex': ".*本科.*"}}).count()
    result4 = Company_detail.find({'release_time': {'$regex': ".*硕士.*"}}).count()
    return render(request,'MyBoss/test2.html',{'result1': result1,'result2': result2,'result3': result3,'result4': result4,})
