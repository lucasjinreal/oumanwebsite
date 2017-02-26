from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from business.forms import BusinessContactForm


# Create your views here.
def businesscontact(request):
    if request.method == 'POST':
        form = BusinessContactForm(request.POST)
        if form.is_valid():
            business_contact = form.save()
            contact_name = form.cleaned_data['contact_name']
            contact_name = intelligent_judge(contact_name)
            contact_occupation = form.cleaned_data['contact_occupation']
            return render(request, 'contact_success.html', {'results': contact_name + contact_occupation})
        else:
            form = BusinessContactForm()
    return HttpResponse("系统不支持内置表单提交，请在浏览器中打开。")


def intelligent_judge(contact_name_):
    """
    this method will return a welcome string depend on different person
    :param contact_name_:
    :return:
    """
    my_relations = {
        '李安': '人工智能系统检测到您是CEO大人的女朋友，他问你今天晚上一起洗澡吗？',
        '安安': '人工智能系统检测到您是CEO大人的女朋友，他问你今天晚上一起洗澡吗？',
        '金宽': '人工智能系统检测到您是CEO大人的弟弟，他怀疑你那里有问题，为毛乱填写？',
        '金发松': '人工智能系统检测到您是CEO大人的弟弟，他怀疑你那里有问题，为毛乱填写？',
        '张瀚': '人工智能系统检测到您是CEO大人的好兄弟，本系统将可以向你透露128位车展超模的微信号',
        '张天': '人工智能系统检测到您是CEO大人的好兄弟，本系统将可以向你透露128位车展超模的微信号',
        '赵景洲': '人工智能系统检测到您是CEO大人的好兄弟，本系统将可以向你透露128位车展超模的微信号',
        '黄致远': '人工智能系统检测到您是欧曼科技成员，系统求求你们不要给前端后台的兄弟们添乱了',
        '梁俊杰': '人工智能系统检测到您是欧曼科技成员，系统求求你们不要给前端后台的兄弟们添乱了',
        '石晴蔚': '人工智能系统检测到您是欧曼科技成员，系统求求你们不要给前端后台的兄弟们添乱了',
        '蔡云伟': '人工智能系统检测到您是欧曼科技成员，系统求求你们不要给前端后台的兄弟们添乱了',
        '向松': '人工智能系统检测到您是欧曼科技成员，系统求求你们不要给前端后台的兄弟们添乱了',
        '蔡云晖': '人工智能系统检测到您是欧曼科技成员，系统求求你们不要给前端后台的兄弟们添乱了',
        '张倩倩': '人工智能系统检测到您是CEO大人的女朋友，他问你今天晚上一起洗澡吗？',
    }
    if contact_name_ in my_relations:
        return my_relations[contact_name_]
    elif not contact_name_:
        return "default"
    else:
        return contact_name_

