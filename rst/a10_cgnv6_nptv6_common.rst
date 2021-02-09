.. _a10_cgnv6_nptv6_common_module:


a10_cgnv6_nptv6_common -- Configures A10 cgnv6.nptv6.common
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NPTv6 common settings






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  send_icmpv6_on_error (False, any, None)
    'disable'= Disable to send ICMPv6 when error discovered;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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

