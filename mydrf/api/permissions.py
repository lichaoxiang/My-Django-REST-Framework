# from rest_framework import permissions
#
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     '''
#     自定义权限-只允许对象的所有者进行编辑/删除
#     此处 obj 表示 Snippet 对象
#     '''
#     def has_object_permission(self, request, view, obj):
#         # 读取的权限允许任何请求
#         # 所以我们总是允许 GET 、HEAD 、OPTIONS 请求
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # 只有对象的所有者才允许写权限
#         # 返回 True/False  True 代表有权限，False 代表无权限
#         return obj.owner == request.user







from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        '''
        系统级权限，不接受 obj 对象
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser