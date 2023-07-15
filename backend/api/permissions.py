from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):    #django custom permissions

    def has_permission(self,request,view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request,view)        # if user is staff member invoke the has_permission of the parent class DjangoModelPermissions


    # def has_permission(self, request, view):
    #     user = request.user
    #     print("dfdnsk",user.get_all_permissions())
    #     if user.is_staff:
    #         print("fdjfls")
    #         if user.has_perm("products.add_product"):  #appname.verb_modelname      all in lower case
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #         return False
    #     return False

   