# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Student

def student(request):
    all_student = Student.objects.all()
    # 查询数据库所有

    age_13 = Student.objects.filter(age=13)
    # 查询age=13的学生

    id_2 = Student.objects.get(id=3)
    # 注意到get 获取的数据必须只有一条

    order_by_age = Student.objects.order_by('age')
    # 按照age进行排序

    and_find = Student.objects.order_by('-age').filter(name='张三')
    # 按照age反序，然后并且找到name是张三的

    limit = Student.objects.order_by('age')[:2]
    # 限制返回条数索引到2

    sql = """
        select * from 
            student_student
        where
            id = 1
    """
    sql_data = Student.objects.raw(sql)
    return render_to_response('student.html', locals())


def addData(request):
    '''
        插入数据
    '''
    #student = Student(
    #    name = 'lod six',
    #    age = 38,
    #   gender = '男',
    #   grader = '六年级一班'
    #)
    #Student.save()
    student = Student()
    student.name = 'lod six'
    student.age = 38
    student.gender = '男'
    student.grade = '六年级一班'
    student.save()

    return render_to_response('student.html', locals())

# Create your views here.


def upData(request):
    # 单条修改
    # student_id_1 = Student.objects.get(id = 1)
    # tudent_id_1.name = 'san'
    # student_id_1.save()
    # return render_to_response('student.html', locals())
    student_age_38 = Student.objects.filter(age=38)
    student_age_38.update(name = 'domn')
    return render_to_response('student.html', locals())

def delData(request):
    student_id_2 = Student.objects.get(id=2)
    student_id_2.delete()
    return render_to_response('student.html', locals())