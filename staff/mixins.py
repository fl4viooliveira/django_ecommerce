from typing import Union

from django.http import (HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.shortcuts import redirect


class StaffUserMixin(object):
    def dispatch(self, request, *args, **kwargs) -> Union[HttpResponsePermanentRedirect, HttpResponseRedirect]:
        if not request.user.is_staff:
            return redirect("home")
        return super(StaffUserMixin, self).dispatch(request, *args, **kwargs)


__all__ = ('StaffUserMixin',)
