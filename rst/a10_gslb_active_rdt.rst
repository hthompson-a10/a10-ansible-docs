.. _a10_gslb_active_rdt_module:


a10_gslb_active_rdt -- Configures A10 gslb.active-rdt
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Active RDT Options






Parameters
----------

  domain (False, any, None)
    Specify Query Domain (Specify Domain Name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  track (False, any, None)
    Specify Tracking Time, unit= second, default is 60


  sleep (False, any, None)
    Specify Sleep Time when query fail, unit= second, default is 3


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  icmp (False, any, None)
    Using ICMP


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Specify local port to send probe packet, default is 0 (no port)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  retry (False, any, None)
    Specify Retry Count, default is 3


  uuid (False, any, None)
    uuid of the object


  interval (False, any, None)
    Specify Query Interval, unit= second, default is 1


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    Specify Query Timeout, unit= msec, default is 3000


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

