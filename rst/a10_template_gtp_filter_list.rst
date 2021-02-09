.. _a10_template_gtp_filter_list_module:


a10_template_gtp_filter_list -- Configures A10 template.gtp-filter-list
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure APN and IMSI filter list






Parameters
----------

  str_list (False, any, None)
    Field str_list


    selection_mode (optional, any, None)
      'mobilestation'= MS provided APN, subscription not verified; 'network'= Network provided APN, subscription not verified; 'verified'= MS or Network provided APN, subscription verified;


    imsi_selection (optional, any, None)
      Specify the IMSI number


    apn (optional, any, None)
      Specify the APN


    imsi (optional, any, None)
      Set the IMSI number



  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify name of the filter list


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

