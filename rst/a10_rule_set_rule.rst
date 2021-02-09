.. _a10_rule_set_rule_module:


a10_rule_set_rule -- Configures A10 rule-set.rule
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure rule-set rule






Parameters
----------

  oper (False, any, None)
    Field oper


    status (optional, any, None)
      Field status


    denybytes (optional, any, None)
      Field denybytes


    activesessionother (optional, any, None)
      Field activesessionother


    activesessiontcp (optional, any, None)
      Field activesessiontcp


    permitbytes (optional, any, None)
      Field permitbytes


    sessiontcp (optional, any, None)
      Field sessiontcp


    sessionicmp (optional, any, None)
      Field sessionicmp


    last_hitcount_time (optional, any, None)
      Field last_hitcount_time


    resetpackets (optional, any, None)
      Field resetpackets


    sessiontotal (optional, any, None)
      Field sessiontotal


    activesessionsctp (optional, any, None)
      Field activesessionsctp


    totalpackets (optional, any, None)
      Field totalpackets


    activesessionudp (optional, any, None)
      Field activesessionudp


    sessionsctp (optional, any, None)
      Field sessionsctp


    name (optional, any, None)
      Rule name


    sessionother (optional, any, None)
      Field sessionother


    totalbytes (optional, any, None)
      Field totalbytes


    sessionudp (optional, any, None)
      Field sessionudp


    activesessionicmp (optional, any, None)
      Field activesessionicmp


    activesessiontotal (optional, any, None)
      Field activesessiontotal


    denypackets (optional, any, None)
      Field denypackets


    permitpackets (optional, any, None)
      Field permitpackets


    resetbytes (optional, any, None)
      Field resetbytes


    action (optional, any, None)
      Field action


    hitcount (optional, any, None)
      Field hitcount



  cgnv6_lsn_lid (False, any, None)
    LSN LID


  src_zone (False, any, None)
    Zone name


  src_zone_any (False, any, None)
    'any'= any;


  fw_log (False, any, None)
    Enable logging


  forward_listen_on_port (False, any, None)
    Listen on port


  track_application (False, any, None)
    Enable application statistic


  dst_zone (False, any, None)
    Zone name


  dst_zone_any (False, any, None)
    'any'= any;


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hit-count'= Hit counts; 'permit-bytes'= Permitted bytes counter; 'deny-bytes'= Denied bytes counter; 'reset-bytes'= Reset bytes counter; 'permit-packets'= Permitted packets counter; 'deny-packets'= Denied packets counter; 'reset-packets'= Reset packets counter; 'active-session-tcp'= Active TCP session counter; 'active-session-udp'= Active UDP session counter; 'active- session-icmp'= Active ICMP session counter; 'active-session-other'= Active other protocol session counter; 'session-tcp'= TCP session counter; 'session- udp'= UDP session counter; 'session-icmp'= ICMP session counter; 'session- other'= Other protocol session counter; 'active-session-sctp'= Active SCTP session counter; 'session-sctp'= SCTP session counter; 'hitcount-timestamp'= Last hit counts timestamp;



  src_ipv4_any (False, any, None)
    'any'= Any IPv4 address;


  log (False, any, None)
    Enable logging


  dst_ipv4_any (False, any, None)
    'any'= Any IPv4 address;


  policy (False, any, None)
    'cgnv6'= Apply CGNv6 policy; 'forward'= Forward packet;


  listen_on_port (False, any, None)
    Listen on port


  cgnv6_fixed_nat_log (False, any, None)
    Enable logging


  app_list (False, any, None)
    Field app_list


    protocol_tag (optional, any, None)
      'aaa'= Protocol/application used for AAA (Authentification, Authorization and Accounting) purposes.; 'adult-content'= Adult content.; 'advertising'= Advertising networks and applications.; 'analytics-and-statistics'= user- analytics and statistics.; 'anonymizers-and-proxies'= Traffic-anonymization protocol/application.; 'audio-chat'= Protocol/application used for Audio Chat.; 'basic'= Protocols required for basic classification, e.g., ARP, HTTP; 'blog'= Blogging platform.; 'cdn'= Protocol/application used for Content-Delivery Networks.; 'chat'= Protocol/application used for Text Chat.; 'classified-ads'= Protocol/application used for Classified ads.; 'cloud-based-services'= SaaS and/or PaaS cloud based services.; 'crowdfunding'= Service for funding a project or venture by raising small amounts of money from a large number of people.; 'cryptocurrency'= Cryptocurrency.; 'database'= Database-specific protocols.; 'disposable-email'= Disposable email accounts.; 'ebook-reader'= Services for e-book readers.; 'email'= Native email protocol.; 'enterprise'= Protocol/application used in an enterprise network.; 'file-management'= Protocol/application designed specifically for file management and exchange, e.g., Dropbox, SMB; 'file-transfer'= Protocol that offers file transferring as a functionality as a secondary feature. e.g., Skype, Whatsapp; 'forum'= Online forum.; 'gaming'= Protocol/application used by games.; 'instant-messaging-and- multimedia-conferencing'= Protocol/application used for Instant messaging or multiconferencing.; 'internet-of-things'= Internet Of Things protocol/application.; 'mobile'= Mobile-specific protocol/application.; 'map- service'= Digital Maps service.; 'multimedia-streaming'= Protocol/application used for multimedia streaming.; 'networking'= Protocol used for (inter) networking purpose.; 'news-portal'= Protocol/application used for News Portals.; 'peer-to-peer'= Protocol/application used for Peer-to-peer purposes.; 'remote-access'= Protocol/application used for remote access.; 'scada'= SCADA (Supervisory control and data acquisition) protocols, all generations.; 'social-networks'= Social networking application.; 'software-update'= Auto- update protocol.; 'standards-based'= Protocol issued from standardized bodies such as IETF, ITU, IEEE, ETSI, OIF.; 'transportation'= Transportation.; 'video- chat'= Protocol/application used for Video Chat.; 'voip'= Application used for Voice over IP.; 'vpn-tunnels'= Protocol/application used for VPN or tunneling purposes.; 'web'= Application based on HTTP/HTTPS.; 'web-e-commerce'= Protocol/application used for E-commerce websites.; 'web-search-engines'= Protocol/application used for Web search portals.; 'web-websites'= Protocol/application used for Company Websites.; 'webmails'= Web email application.; 'web-ext-adult'= Web Extension Adult; 'web-ext-auctions'= Web Extension Auctions; 'web-ext-blogs'= Web Extension Blogs; 'web-ext-business- and-economy'= Web Extension Business and Economy; 'web-ext-cdns'= Web Extension CDNs; 'web-ext-collaboration'= Web Extension Collaboration; 'web-ext-computer- and-internet-info'= Web Extension Computer and Internet Info; 'web-ext- computer-and-internet-security'= Web Extension Computer and Internet Security; 'web-ext-dating'= Web Extension Dating; 'web-ext-educational-institutions'= Web Extension Educational Institutions; 'web-ext-entertainment-and-arts'= Web Extension Entertainment and Arts; 'web-ext-fashion-and-beauty'= Web Extension Fashion and Beauty; 'web-ext-file-share'= Web Extension File Share; 'web-ext- financial-services'= Web Extension Financial Services; 'web-ext-gambling'= Web Extension Gambling; 'web-ext-games'= Web Extension Games; 'web-ext-government'= Web Extension Government; 'web-ext-health-and-medicine'= Web Extension Health and Medicine; 'web-ext-individual-stock-advice-and-tools'= Web Extension Individual Stock Advice and Tools; 'web-ext-internet-portals'= Web Extension Internet Portals; 'web-ext-job-search'= Web Extension Job Search; 'web-ext- local-information'= Web Extension Local Information; 'web-ext-malware'= Web Extension Malware; 'web-ext-motor-vehicles'= Web Extension Motor Vehicles; 'web-ext-music'= Web Extension Music; 'web-ext-news'= Web Extension News; 'web- ext-p2p'= Web Extension P2P; 'web-ext-parked-sites'= Web Extension Parked Sites; 'web-ext-proxy-avoid-and-anonymizers'= Web Extension Proxy Avoid and Anonymizers; 'web-ext-real-estate'= Web Extension Real Estate; 'web-ext- reference-and-research'= Web Extension Reference and Research; 'web-ext-search- engines'= Web Extension Search Engines; 'web-ext-shopping'= Web Extension Shopping; 'web-ext-social-network'= Web Extension Social Network; 'web-ext- society'= Web Extension Society; 'web-ext-software'= Web Extension Software; 'web-ext-sports'= Web Extension Sports; 'web-ext-streaming-media'= Web Extension Streaming Media; 'web-ext-training-and-tools'= Web Extension Training and Tools; 'web-ext-translation'= Web Extension Translation; 'web-ext-travel'= Web Extension Travel; 'web-ext-web-advertisements'= Web Extension Web Advertisements; 'web-ext-web-based-email'= Web Extension Web based Email; 'web- ext-web-hosting'= Web Extension Web Hosting; 'web-ext-web-service'= Web Extension Web Service;


    obj_grp_application (optional, any, None)
      Application object group


    protocol (optional, any, None)
      Specify application(s)



  source_list (False, any, None)
    Field source_list


    src_obj_network (optional, any, None)
      Network object


    src_ipv6_subnet (optional, any, None)
      IPv6 IP Address


    src_slb_server (optional, any, None)
      SLB Real server name


    src_ip_subnet (optional, any, None)
      IPv4 IP Address


    src_obj_grp_network (optional, any, None)
      Network object group



  rule_set_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  cgnv6_log (False, any, None)
    Enable logging


  application_any (False, any, None)
    'any'= any;


  dst_threat_list (False, any, None)
    Bind threat-list for destination IP based filtering


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Rule name


  dst_geoloc_list (False, any, None)
    Geolocation name list


  src_class_list (False, any, None)
    Match source IP against class-list


  reset_lid (False, any, None)
    Apply a Template LID


  service_any (False, any, None)
    'any'= any;


  src_geoloc_name (False, any, None)
    Single geolocation name


  dst_domain_list (False, any, None)
    Match destination IP against domain-list


  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_list (False, any, None)
    Field service_list


    icmp_code (optional, any, None)
      ICMP code number


    range_dst_port (optional, any, None)
      Port range (Starting Port Number)


    special_v6_code (optional, any, None)
      'any-code'= Any ICMPv6 code; 'addr-unreachable'= Code 3, address unreachable; 'admin-prohibited'= Code 1, admin prohibited; 'no-route'= Code 0, no route to destination; 'not-neighbour'= Code 2, not neighbor; 'port-unreachable'= Code 4, destination port unreachable;


    obj_grp_service (optional, any, None)
      service object group


    alg (optional, any, None)
      'FTP'= FTP; 'TFTP'= TFTP; 'SIP'= SIP; 'DNS'= DNS; 'PPTP'= PPTP; 'RTSP'= RTSP;


    lt_src_port (optional, any, None)
      Lower than the port number


    special_type (optional, any, None)
      'any-type'= Any ICMP type; 'echo-reply'= Type 0, echo reply; 'echo-request'= Type 8, echo request; 'info-reply'= Type 16, information reply; 'info-request'= Type 15, information request; 'mask-reply'= Type 18, address mask reply; 'mask- request'= Type 17, address mask request; 'parameter-problem'= Type 12, parameter problem; 'redirect'= Type 5, redirect message; 'source-quench'= Type 4, source quench; 'time-exceeded'= Type 11, time exceeded; 'timestamp'= Type 13, timestamp; 'timestamp-reply'= Type 14, timestamp reply; 'dest-unreachable'= Type 3, destination unreachable;


    icmpv6_type (optional, any, None)
      ICMPv6 type number


    sctp_template (optional, any, None)
      SCTP Template


    port_num_end_dst (optional, any, None)
      Ending Port Number


    range_src_port (optional, any, None)
      Port range (Starting Port Number)


    icmpv6_code (optional, any, None)
      ICMPv6 code number


    icmp_type (optional, any, None)
      ICMP type number


    lt_dst_port (optional, any, None)
      Lower than the port number


    eq_src_port (optional, any, None)
      Equal to the port number


    gtp_template (optional, any, None)
      Configure GTP template (GTP Template Name)


    icmp (optional, any, None)
      ICMP


    eq_dst_port (optional, any, None)
      Equal to the port number


    proto_id (optional, any, None)
      Protocol ID


    gt_src_port (optional, any, None)
      Greater than the port number


    special_v6_type (optional, any, None)
      'any-type'= Any ICMPv6 type; 'dest-unreachable'= Type 1, destination unreachable; 'echo-reply'= Type 129, echo reply; 'echo-request'= Type 128, echo request; 'packet-too-big'= Type 2, packet too big; 'param-prob'= Type 4, parameter problem; 'time-exceeded'= Type 3, time exceeded;


    icmpv6 (optional, any, None)
      ICMPv6


    protocols (optional, any, None)
      'tcp'= tcp; 'udp'= udp; 'sctp'= sctp;


    gt_dst_port (optional, any, None)
      Greater than the port number


    special_code (optional, any, None)
      'any-code'= Any ICMP code; 'frag-required'= Code 4, fragmentation required; 'host-unreachable'= Code 1, destination host unreachable; 'network- unreachable'= Code 0, destination network unreachable; 'port-unreachable'= Code 3, destination port unreachable; 'proto-unreachable'= Code 2, destination protocol unreachable; 'route-failed'= Code 5, source route failed;


    port_num_end_src (optional, any, None)
      Ending Port Number



  src_threat_list (False, any, None)
    Bind threat-list for source IP based filtering


  listen_on_port_lid (False, any, None)
    Apply a Template LID


  cgnv6_lsn_log (False, any, None)
    Enable logging


  src_geoloc_list (False, any, None)
    Geolocation name list


  dst_ipv6_any (False, any, None)
    'any'= Any IPv6 address;


  action (False, any, None)
    'permit'= permit; 'deny'= deny; 'reset'= reset;


  lid (False, any, None)
    Apply a Template LID


  dst_class_list (False, any, None)
    Match destination IP against class-list


  stats (False, any, None)
    Field stats


    deny_packets (optional, any, None)
      Denied packets counter


    permit_bytes (optional, any, None)
      Permitted bytes counter


    active_session_icmp (optional, any, None)
      Active ICMP session counter


    active_session_other (optional, any, None)
      Active other protocol session counter


    reset_packets (optional, any, None)
      Reset packets counter


    hitcount_timestamp (optional, any, None)
      Last hit counts timestamp


    name (optional, any, None)
      Rule name


    permit_packets (optional, any, None)
      Permitted packets counter


    session_sctp (optional, any, None)
      SCTP session counter


    session_tcp (optional, any, None)
      TCP session counter


    session_udp (optional, any, None)
      UDP session counter


    deny_bytes (optional, any, None)
      Denied bytes counter


    reset_bytes (optional, any, None)
      Reset bytes counter


    session_icmp (optional, any, None)
      ICMP session counter


    active_session_tcp (optional, any, None)
      Active TCP session counter


    hit_count (optional, any, None)
      Hit counts


    active_session_sctp (optional, any, None)
      Active SCTP session counter


    active_session_udp (optional, any, None)
      Active UDP session counter


    session_other (optional, any, None)
      Other protocol session counter



  dest_list (False, any, None)
    Field dest_list


    dst_ipv6_subnet (optional, any, None)
      IPv6 IP Address


    dst_slb_server (optional, any, None)
      SLB Real server name


    dst_slb_vserver (optional, any, None)
      SLB Virtual server name


    dst_obj_network (optional, any, None)
      Network object


    dst_ip_subnet (optional, any, None)
      IPv4 IP Address


    dst_obj_grp_network (optional, any, None)
      Network object group



  dst_geoloc_name (False, any, None)
    Single geolocation name


  state (True, any, None)
    State of the object to be created.


  reset_lidlog (False, any, None)
    Enable logging


  status (False, any, None)
    'enable'= Enable rule; 'disable'= Disable rule;


  lidlog (False, any, None)
    Enable logging


  src_geoloc_list_shared (False, any, None)
    Use Geolocation list from shared partition


  ip_version (False, any, None)
    'v4'= IPv4 rule; 'v6'= IPv6 rule;


  idle_timeout (False, any, None)
    TCP/UDP idle-timeout


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  move_rule (False, any, None)
    Field move_rule


    location (optional, any, None)
      'top'= top; 'before'= before; 'after'= after; 'bottom'= bottom;


    target_rule (optional, any, None)
      Field target_rule



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  remark (False, any, None)
    Rule entry comment (Notes for this rule)


  listen_on_port_lidlog (False, any, None)
    Enable logging


  cgnv6_policy (False, any, None)
    'lsn-lid'= Apply specified CGNv6 LSN LID; 'fixed-nat'= Apply CGNv6 Fixed NAT;


  src_ipv6_any (False, any, None)
    'any'= Any IPv6 address;


  fwlog (False, any, None)
    Enable logging


  dst_geoloc_list_shared (False, any, None)
    Use Geolocation list from shared partition


  user_tag (False, any, None)
    Customized tag


  forward_log (False, any, None)
    Enable logging









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

