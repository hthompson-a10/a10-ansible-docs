.. _a10_slb_template_persist_ssl_sid_module:


a10_slb_template_persist_ssl_sid -- Configures A10 slb.template.persist.ssl-sid
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SSL session ID  persistence






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    SSL session ID persistence template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  dont_honor_conn_rules (False, any, None)
    Do not observe connection rate rules


  timeout (False, any, None)
    Persistence timeout (in minutes)


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

