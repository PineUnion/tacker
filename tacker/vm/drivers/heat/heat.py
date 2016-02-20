# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2015 Intel Corporation.
# All Rights Reserved.
#
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys
import time

from heatclient import exc as heatException
from oslo_config import cfg
from toscaparser.utils import yamlparser
import yaml

from tacker.common import clients
from tacker.common import log
from tacker.extensions import vnfm
from tacker.openstack.common import jsonutils
from tacker.openstack.common import log as logging
from tacker.vm.drivers import abstract_driver


LOG = logging.getLogger(__name__)
CONF = cfg.CONF
OPTS = [
    cfg.IntOpt('stack_retries',
               default=60,
               help=_("Number of attempts to retry for stack"
                      "creation/deletion")),
    cfg.IntOpt('stack_retry_wait',
               default=5,
               help=_("Wait time between two successive stack"
                      "create/delete retries")),
]
CONF.register_opts(OPTS, group='tacker_heat')
STACK_RETRIES = cfg.CONF.tacker_heat.stack_retries
STACK_RETRY_WAIT = cfg.CONF.tacker_heat.stack_retry_wait

HEAT_TEMPLATE_BASE = """
heat_template_version: 2013-05-23
"""


class DeviceHeat(abstract_driver.DeviceAbstractDriver):

    """Heat driver of hosting device."""

    def __init__(self):
        super(DeviceHeat, self).__init__()

    def get_type(self):
        return 'heat'

    def get_name(self):
        return 'heat'

    def get_description(self):
        return 'Heat infra driver'

    @log.log
    def create_device_template_pre(self, plugin, context, device_template):  #update (name, template_name), description, service_type
        device_template_dict = device_template['device_template']
        vnfd_yaml = device_template_dict['attributes'].get('vnfd')
        if vnfd_yaml is None:
            return

        vnfd_dict = yaml.load(vnfd_yaml)
        KEY_LIST = (('name', 'template_name'), ('description', 'description'))

        device_template_dict.update(    #meaning: if key is empty in device_template_dict
            dict((key, vnfd_dict[vnfd_key]) for (key, vnfd_key) in KEY_LIST
                 if ((key not in device_template_dict or      # key is empty
                      device_template_dict[key] == '') and    # value is empty
                     vnfd_key in vnfd_dict and                # key is available
                     vnfd_dict[vnfd_key] != '')))             # value is available

        service_types = vnfd_dict.get('service_properties', {}).get('type', [])                #type=['firewall', 'nat']
        if service_types:
            device_template_dict.setdefault('service_types', []).extend(
                [{'service_type': service_type}              # service_types includes values like that 'service_type': service_type
                 for service_type in service_types])
        for vdu in vnfd_dict.get('vdus', {}).values():
            mgmt_driver = vdu.get('mgmt_driver')
            if mgmt_driver:
                device_template_dict['mgmt_driver'] = mgmt_driver
        LOG.debug(_('device_template %s'), device_template)

    @log.log
    def _update_params(self, original, paramvalues, match=False):
                    failure_policy == 'overload':    self._update_params(value, paramvalues[key], False)
                    else:
                        LOG.debug('Key missing Value: %s', key)
                        raise vnfm.InputValuesMissing(key=key)


    failure_policy == 'overload':
(vdu_id, vdu_dict,
                                                         properties,
                                                         template_dict)
  # My code is here - shayne
                if ''
_process_vdu_network_interfaces
_process_vdu_ceilometer_alam
