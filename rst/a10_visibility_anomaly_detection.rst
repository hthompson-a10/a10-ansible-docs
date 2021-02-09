.. _a10_visibility_anomaly_detection_module:


a10_visibility_anomaly_detection -- Configures A10 visibility.anomaly-detection
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Anomaly detection parameters






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  logging (False, any, None)
    'per-entity'= Enable per entity logging; 'per-metric'= Enable per metric logging with threshold details; 'disable'= Disable anomaly notifications (Default);


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sensitivity (False, any, None)
    'high'= Highly sensitive anomaly detection. Can lead to false positives; 'low'= Low sensitivity anomaly detection. Can cause delay in detection and might not detect certain attacks. (default);


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  feature_status (False, any, None)
    'enable'= Enable anomaly-detection; 'disable'= Disable anomaly detection (default);


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

