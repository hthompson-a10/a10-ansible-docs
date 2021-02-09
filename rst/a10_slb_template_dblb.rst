.. _a10_slb_template_dblb_module:


a10_slb_template_dblb -- Configures A10 slb.template.dblb
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DBLB template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    DBLB template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  class_list (False, any, None)
    Specify user/password string class list (Class list name)


  state (True, any, None)
    State of the object to be created.


  calc_sha1 (False, any, None)
    Field calc_sha1


    sha1_value (optional, any, None)
      Cleartext password



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  server_version (False, any, None)
    'MSSQL2008'= MSSQL server 2008 or 2008 R2; 'MSSQL2012'= MSSQL server 2012; 'MySQL'= MySQL server (any version);


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

