.. _a10_netflow_common_module:


a10_netflow_common -- Configures A10 netflow.common
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NetFlow/IPFIX common settings






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


  max_packet_queue_time (False, any, None)
    Configure netflow packet queue time (Max packet queue time(*20ms). Default=50( *20ms = 1s)))


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  reset_time_on_flow_record (False, any, None)
    Reset session start time to current time on each flow timeout export for long- lasting session (default= disabled).


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

