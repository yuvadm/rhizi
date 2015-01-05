"""
Rhizi kernel, home to core operation login
"""
import db_controller
import logging
import traceback
from db_op import DBO_attr_diff_commit
from db_op import DBO_topo_diff_commit

log = logging.getLogger('rhizi')

class RZ_Kernel(object):

    def diff_commit__topo(self, db_ctl, topo_diff):
        """
        commit a graph topology diff - this is a common pathway for:
           - RESP API calls
           - socket.io calls
           - future interfaces
        """
        op = DBO_topo_diff_commit(topo_diff)
        try:
            op_ret = db_ctl.exec_op(op)
            return op_ret
        except Exception as e:
            log.error(e.message)
            log.error(traceback.print_exc())
            raise e

    def diff_commit__attr(self, db_ctl, attr_diff):
        op = DBO_attr_diff_commit(attr_diff)
        try:
            op_ret = db_ctl.exec_op(op)
            return op_ret
        except Exception as e:
            log.error(e.message)
            log.error(traceback.print_exc())
            raise e