.. _a10_sys_ut_template_udp_module:


a10_sys_ut_template_udp -- Configures A10 sys.ut.template.udp
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

UDP header






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  src_port_range (False, any, None)
    Field src_port_range


    src_port_end (optional, any, None)
      Src port end value


    src_port_start (optional, any, None)
      Source port value



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  template_name (optional, any, None)
    Key to identify parent object


  dest_port_value (False, any, None)
    Dest port value


  state (True, any, None)
    State of the object to be created.


  nat_pool (False, any, None)
    Nat pool port


  checksum (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  length (False, any, None)
    Total packet length starting at UDP header


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  dest_port (False, any, None)
    Dest port









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

