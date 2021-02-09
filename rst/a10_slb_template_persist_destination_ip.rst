.. _a10_slb_template_persist_destination_ip_module:


a10_slb_template_persist_destination_ip -- Configures A10 slb.template.persist.destination-ip
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Destination IP persistence






Parameters
----------

  netmask6 (False, any, None)
    IPV6 subnet mask


  match_type (False, any, None)
    Persistence type


  hash_persist (False, any, None)
    Use hash value of destination IP address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  netmask (False, any, None)
    IP subnet mask


  dont_honor_conn_rules (False, any, None)
    Do not observe connection rate rules


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  scan_all_members (False, any, None)
    Persist with SCAN of all members


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  service_group (False, any, None)
    Persist within the same service group


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Destination IP persistence template name


  user_tag (False, any, None)
    Customized tag


  server (False, any, None)
    Persist to the same server, default is port


  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    Persistence timeout (in minutes)


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

