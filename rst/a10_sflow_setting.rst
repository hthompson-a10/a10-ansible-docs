.. _a10_sflow_setting_module:


a10_sflow_setting -- Configures A10 sflow.setting
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure sFlow






Parameters
----------

  local_collection (False, any, None)
    Enable local sflow collection


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  counter_polling_interval (False, any, None)
    sFlow counter polling interval, default is 10


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  max_header (False, any, None)
    Configure maximum number of bytes that should be copied from a sampled packet (default= 128) (The maximum number of bytes (Default= 128))


  source_ip_use_mgmt (False, any, None)
    Use management interface's IP address for source IP of sFlow packets


  packet_sampling_rate (False, any, None)
    sFlow packet sampling rate, default is 1000


  state (True, any, None)
    State of the object to be created.


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

