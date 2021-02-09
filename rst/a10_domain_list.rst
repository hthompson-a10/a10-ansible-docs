.. _a10_domain_list_module:


a10_domain_list -- Configures A10 domain-list
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure domain list






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Name of the domain list


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  domain_name_list (False, any, None)
    Field domain_name_list


    interval (optional, any, None)
      DNS query interval (in minute, default is 10)


    domain_name (optional, any, None)
      Domain name to be added to this domain list



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

