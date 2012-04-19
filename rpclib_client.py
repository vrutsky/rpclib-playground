#!/usr/bin/env python
# encoding: utf8
#
# Copyright © Burak Arslan <burak at arskom dot com dot tr>,
#             Arskom Ltd. http://www.arskom.com.tr
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    3. Neither the name of the owner nor the names of its contributors may be
#       used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from rpclib.client.http import HttpClient

from binary_http import application

c = HttpClient('http://localhost:7789/', application)

# This doesn't work:
#
#Traceback (most recent call last):
#  File "./rpclib_client.py", line 50, in <module>
#    print c.service.get(file_name="/tmp/some_big_file")
#  File "/home/bob/.local/lib/python2.7/site-packages/rpclib-2.7.0_beta-py2.7.egg/rpclib/client/http.py", line 43, in __call__
#    self.get_out_string(self.ctx) # sets ctx.out_string
#  File "/home/bob/.local/lib/python2.7/site-packages/rpclib-2.7.0_beta-py2.7.egg/rpclib/client/_base.py", line 106, in get_out_string
#    self.app.out_protocol.serialize(ctx, self.app.out_protocol.REQUEST)
#  File "/home/bob/.local/lib/python2.7/site-packages/rpclib-2.7.0_beta-py2.7.egg/rpclib/protocol/http.py", line 300, in serialize
#    assert message in (self.RESPONSE,)
#AssertionError
print c.service.get(file_name="/tmp/some_big_file")


"""
u = c.factory.create("User")

u.user_name = 'dave'
u.first_name = 'david'
u.last_name = 'smith'
u.email = 'david.smith@example.com'
u.permissions = []

permission = c.factory.create("Permission")
permission.application = 'table'
permission.operation = 'write'
u.permissions.append(permission)

permission = c.factory.create("Permission")
permission.application = 'table'
permission.operation = 'read'
u.permissions.append(permission)

print u

retval = c.service.add_user(u)
print retval

print c.service.get_user(retval)
print c.service.get_all_user()
"""
