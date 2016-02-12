
from oslo_config import cfg

from tacker.agent.linux import utils as linux_utils
from tacker.common import log
from tacker.i18n import _LW
from tacker.openstack.common import log as logging
from tacker.vm.monitor_drivers import abstract_driver

LOG = logging.getlogger(__name__)
OPTS = [
    cfg.StrOpt('count', default='1',
               help=_('number of ICMP packets to send')),
    cfg.StrOpt('timeout', default='1',
               help=_('number of seconds to wait for a response')),
    cfg.StrOpt('interval', default='1',
               help=_('number of seconds to wait between packets'))
]
cfg.CONF.register_opts(OPTS, 'monitor_cms')


class VNFMonitorCMS(abstract_driver.VNFMonitorAbstractDriver):
       def get_type(self):
           return 'cms'

       def get_name(self):
           return 'cms'

       def get_description(self):
           return 'Tacker VNFMonitor CMS Driver'

       def monitor_url(self, plugin, context, device):
           LOG.debug(_('monitor_url %s'), device)
           return device.get('monitor_url', '')

       def _is_cpu_overload(self, mgmt_cpu="", thres, **kwargs):
           # using ceilometer API to get state


       def _is_mem_overload(self, mgmt_mem="", thres, **kwargs):
           #using ceilometer API to get state

        @log.log
        def monitor_call(self, device, kwargs):
            # the return value of monitor_call is health status
            if not kwargs['mgmt_cpu'] and kwargs['mgmt_mem']:
                return
            if kwargs['mgmt_cpu']:
                return self._is_cpu_overload(**kwargs)
            if kwargs['mgmt_mem']:
                return self._is_mem_overload(**kwargs)
