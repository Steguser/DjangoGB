from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import json
# Create your views here.


def main_view(request):
    # # template = Template(
    # #     'Hello {{ name }}'
    # # )
    # # context = Context({
    # #     'name': 'Anton'
    # # })
    # #
    #
    # template = get_template('main/index.html')
    #
    # context = {
    #     'title': 'This is a main page',
    #     'subtitle': 'First django page',
    #     'username': request.user
    # }
    #
    # response_string = template.render(context)
    #
    # # return render(request, 'main/index.html')

    with open('data.json', 'r') as file:
        products = json.load(file)

    response_string = render_to_string(
        'main/index.html',
        {
            'title': 'This is a main page',
            'subtitle': 'First django page',
            # 'username': request.user,
            'username': 'anton',
            'products': products.get('products') or [],
            'is_active': True
        }
    )

    return HttpResponse(response_string)


def contacts_view(request):
    return render(request,
                  'main/contacts.html',
                  {
                      'contacts': [
                          '88000056550',
                          '88009908991',
                          '88000056550',
                          '88009908991',
                          '88000056550',
                          '88009908991',
                          '88000056550',
                          '88009908991',
                          '88000056550',
                          '88009908991',
                          '88000056550',
                          '88009908991',
                          '88003235565'
                      ]
                  }
                  )


def about_view(request):

    return render(request,
                  'main/about.html',
                  {
                      'text': 'Творческая доминанта, на первый взгляд, переворачивает сокращенный фотон.'
                  }
                  )
