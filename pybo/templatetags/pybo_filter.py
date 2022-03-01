from django import template

register = template.Library()

@register.filter
# @register.filter 에터네이션 적용시
# 템플릿에서 해당 함수를 필터로 사용할 수 있게 된다.
def sub(value, arg):
    return value - arg