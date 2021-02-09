.. _a10_slb_dns_module:


a10_slb_dns -- Configures A10 slb.dns
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS Packet Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'slb_req'= No. of requests; 'slb_resp'= No. of responses; 'slb_no_resp'= No. of resource failures; 'slb_req_rexmit'= No. of request retransmits; 'slb_resp_no_match'= No. of requests with no response; 'slb_no_resource'= No. of resource failures; 'nat_req'= (NAT) No. of requests; 'nat_resp'= (NAT) No. of responses; 'nat_no_resp'= (NAT) No. of resource failures; 'nat_req_rexmit'= (NAT) No. of request retransmits; 'nat_resp_no_match'= (NAT) No. of requests with no response; 'nat_no_resource'= (NAT) No. of resource failures; 'nat_xid_reused'= (NAT) No. of requests reusing a transaction id;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    slb_no_resource (optional, any, None)
      No. of resource failures


    nat_resp (optional, any, None)
      (NAT) No. of responses


    slb_resp_no_match (optional, any, None)
      No. of requests with no response


    nat_xid_reused (optional, any, None)
      (NAT) No. of requests reusing a transaction id


    slb_req (optional, any, None)
      No. of requests


    slb_no_resp (optional, any, None)
      No. of resource failures


    nat_req (optional, any, None)
      (NAT) No. of requests


    slb_req_rexmit (optional, any, None)
      No. of request retransmits


    nat_no_resource (optional, any, None)
      (NAT) No. of resource failures


    nat_no_resp (optional, any, None)
      (NAT) No. of resource failures


    nat_req_rexmit (optional, any, None)
      (NAT) No. of request retransmits


    nat_resp_no_match (optional, any, None)
      (NAT) No. of requests with no response


    slb_resp (optional, any, None)
      No. of responses



  uuid (False, any, None)
    uuid of the object


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

