.. _a10_slb_template_logging_module:


a10_slb_template_logging -- Configures A10 slb.template.logging
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logging template






Parameters
----------

  tcp_proxy (False, any, None)
    TCP Proxy Template Name


  pool_shared (False, any, None)
    Specify NAT pool or pool group


  ansible_username (True, any, None)
    Username for AXAPI authentication


  auto (False, any, None)
    'auto'= Configure auto NAT for logging, default is auto enabled;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  keep_end (False, any, None)
    Number of unmasked characters at the end (default= 0)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  keep_start (False, any, None)
    Number of unmasked characters at the beginning (default= 0)


  template_tcp_proxy_shared (False, any, None)
    TCP Proxy Template name


  ansible_host (True, any, None)
    Host for AXAPI authentication


  pool (False, any, None)
    Specify NAT pool or pool group


  shared_partition_tcp_proxy_template (False, any, None)
    Reference a TCP Proxy template from shared partition


  service_group (False, any, None)
    Bind a Service Group to the logging template (Service Group Name)


  local_logging (False, any, None)
    1 to enable local logging (1 to enable local logging, default 0)


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  format (False, any, None)
    Specify a format string for web logging (format string(less than 250 characters) for web logging)


  mask (False, any, None)
    Character to mask the matched pattern (default= X)


  pcre_mask (False, any, None)
    Mask matched PCRE pattern in the log


  name (True, any, None)
    Logging Template Name


  shared_partition_pool (False, any, None)
    Reference a NAT pool or pool group from shared partition


  state (True, any, None)
    State of the object to be created.


  user_tag (False, any, None)
    Customized tag









Examples
--------

.. code-block:: yaml+jinja

    





Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- A10 Networks 2018

