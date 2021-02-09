.. _a10_slb_ac_class_list_module:


a10_slb_ac_class_list -- Configures A10 slb.ac-class-list
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Aho-Corasic add remove config






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ac_list (False, any, None)
    Field ac_list


    action (optional, any, None)
      'add'= Add the entry; 'delete'= Delete the entry;


    ac_key_string (optional, any, None)
      Specify key string


    ac_match_type (optional, any, None)
      'contains'= String contains another string; 'ends-with'= String ends with another string; 'equals'= String equals another string; 'starts-with'= String starts with another string;


    ac_key_value (optional, any, None)
      Specify value string



  name (True, any, None)
    Specify name of the class list


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

