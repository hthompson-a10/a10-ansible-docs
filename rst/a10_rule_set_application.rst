.. _a10_rule_set_application_module:


a10_rule_set_application -- Configures A10 rule.set.application
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field application






Parameters
----------

  oper (False, any, None)
    Field oper


    category_stat (optional, any, None)
      Field category_stat


    rule_list (optional, any, None)
      Field rule_list


    app_stat (optional, any, None)
      Field app_stat


    rule (optional, any, None)
      Field rule



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  rule_set_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


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

