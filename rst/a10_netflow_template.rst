.. _a10_netflow_template_module:


a10_netflow_template -- Configures A10 netflow.template
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPFIX Custom Template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    IPFIX CUSTOM Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  information_element_blk (False, any, None)
    Field information_element_blk


    information_element (optional, any, None)
      'fwd-tuple-vnp-id'= Session forward tuple partition id (ID= 33028); 'rev-tuple- vnp-id'= Session reverse tuple partition id (ID= 33029); 'source-ipv4-address'= IPv4 source address in the IP packet header (ID= 8); 'dest-ipv4-address'= IPv4 destination address in the IP packet header (ID= 12); 'source-ipv6-address'= IPv6 source address in the IP packet header (ID= 27); 'dest-ipv6-address'= IPv6 destination address in the IP packet header (ID=28); 'post-nat-source- ipv4-address'= IPv4 natted source address (ID= 225); 'post-nat-dest- ipv4-address'= IPv4 natted destination address(ID= 226); 'post-nat-source- ipv6-address'= IPv6 natted source address (ID= 281); 'post-nat-dest- ipv6-address'= IPv6 natted destination address (ID= 282); 'source-port'= Source port identifier in the transport header (ID= 7); 'dest-port'= Destination port identifier in the transport header (ID= 11); 'post-nat-source-port'= L4 natted source port(ID= 227); 'post-nat-dest-port'= L4 natted destination port (ID= 228); 'fwd-tuple-type'= Session forward tuple type (ID= 33024); 'rev-tuple- type'= Session reverse tuple type (ID= 33025); 'ip-proto'= Value of the protocol number in the IP packet header (ID= 4); 'flow-direction'= Flow direction= 0=inbound(To an outside interface)/1=outbound(To an inside interface) (ID= 61); 'tcp-control-bits'= Cumulative of all the TCP flags seen for this flow (ID= 6); 'fwd-bytes'= Incoming bytes associated with an IP Flow (ID= 1); 'fwd-packets'= Incoming packets associated with an IP Flow (ID= 2); 'rev-bytes'= Delta bytes in reverse direction of bidirectional flow record (ID= 32769); 'rev-packets'= Delta packets in reverse direction of bidirectional flow record (ID= 32770); 'in-port'= Incoming interface port (ID= 10); 'out-port'= Outcoming interface port (ID= 14); 'in-interface'= Incoming interface name e.g. ethernet 0 (ID= 82); 'out-interface'= Outcoming interface name e.g. ethernet 0 (ID= 32850); 'port-range-start'= Port number identifying the start of a range of ports (ID= 361); 'port-range-end'= Port number identifying the end of a range of ports (ID= 362); 'port-range-step-size'= Step size in a port range (ID= 363); 'port-range-num-ports'= Number of ports in a port range (ID= 364); 'rule-name'= Rule Name (ID= 33034); 'rule-set-name'= Rule-Set Name (ID= 33035); 'fw-source-zone'= Firewall Source Zone Name (ID= 33036); 'fw-dest-zone'= Firewall Dest Zone Name (ID= 33037); 'application-id'= Application ID (ID= 95); 'radius-imsi'= Radius Attribute IMSI (ID= 455); 'radius-msisdn'= Radius Attribute MSISDN (ID= 456); 'radius-imei'= Radius Attribute IMEI (ID= 33030); 'radius-custom1'= Radius Attribute Custom 1 (ID= 33031); 'radius-custom2'= Radius Attribute Custom 2(ID= 33032); 'radius-custom3'= Radius Attribute Custom 3 (ID=33033); 'flow-start-msec'= The absolute timestamp of the first packet of the flow (ID= 152); 'flow-duration-msec'= Difference in time between the first observed packet of this flow and the last observed packet of this flow (4 bytes) (ID= 161); 'flow-duration-msec-64'= Difference in time between the first observed packet of this flow and the last observed packet of this flow (8 bytes) (ID= 33039); 'nat-event'= Indicates a NAT event (ID= 230); 'fw-event'= Indicates a FW session event(ID= 233); 'fw-deny-reset-event'= Indicates a FW deny/reset event (ID= 33038); 'cgn-flow-direction'= Flow direction= 0=inbound(To an outside interface)/1=outbound(To an inside interface)/2=hairpin(From an inside interface to an inside interface) (ID= 33040); 'fw-dest-fqdn'= Firewall matched fqdn(ID= 33041); 'flow-end-reason'= A10 flow end reason(ID= 33042); 'event-time-msec'= The absolute time in milliseconds of an event observation(ID= 323);



  ipfix_template_id (False, any, None)
    Custom IPFIX Template ID


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

