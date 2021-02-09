.. _a10_pki_scep_cert_module:


a10_pki_scep_cert -- Configures A10 pki.scep-cert
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SCEP Certificate enrollment object






Parameters
----------

  dn (False, any, None)
    Specify the Distinguished-Name to use while enrolling the certificate (Format= 'cn=user, dc=example, dc=com')


  secret_string (False, any, None)
    secret password


  interval (False, any, None)
    Interval time in seconds to poll when SCEP response is PENDING (default 5)


  renew_every (False, any, None)
    Specify periodic interval in which to renew the certificate


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  renew_before_value (False, any, None)
    Value of renewal period


  ansible_port (True, any, None)
    Port for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    Specify the password used to enroll the device's certificate


  renew_every_value (False, any, None)
    Value of renewal period


  max_polltime (False, any, None)
    Maximum time in seconds to poll when SCEP response is PENDING (default 180)


  key_length (False, any, None)
    '1024'= Key size 1024 bits; '2048'= Key size 2048 bits(default); '4096'= Key size 4096 bits; '8192'= Key size 8192 bits;


  name (True, any, None)
    Specify Certificate name to be enrolled


  subject_alternate_name (False, any, None)
    Field subject_alternate_name


    san_type (optional, any, None)
      'email'= Enter e-mail address of the subject; 'dns'= Enter hostname of the subject; 'ip'= Enter IP address of the subject;


    san_value (optional, any, None)
      Value of subject-alternate-name



  enroll (False, any, None)
    Initiates enrollment of device with the CA


  log_level (False, any, None)
    level for logging output of scepclient commands(default 1 and detailed 4)


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  url (False, any, None)
    Specify the Enrollment Agent's absolute URL (Format= http=//host/path)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  renew_before_type (False, any, None)
    'hour'= Number of hours before cert expiry; 'day'= Number of days before cert expiry; 'week'= Number of weeks before cert expiry; 'month'= Number of months before cert expiry(1 month=30 days);


  renew_every_type (False, any, None)
    'hour'= Periodic interval in hours; 'day'= Periodic interval in days; 'week'= Periodic interval in weeks; 'month'= Periodic interval in months(1 month=30 days);


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  minute (False, any, None)
    Periodic interval in minutes


  user_tag (False, any, None)
    Customized tag


  method (False, any, None)
    'GET'= GET request; 'POST'= POST request;


  renew_before (False, any, None)
    Specify interval before certificate expiry to renew the certificate









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

