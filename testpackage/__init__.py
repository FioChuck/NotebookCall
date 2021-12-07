# from testpackage.funcitons.utils import local_vars
# dbx_token = local_vars()[0]

import os

from testpackage.funcitons.dbx_notebook import DbxApi
from testpackage.funcitons.utils import local_vars

dbx_token = os.environ.get('DBXTOKEN')

conn1 = DbxApi(dbx_token, 'local_call')

print(conn1.notebook('/dbxRest'))



