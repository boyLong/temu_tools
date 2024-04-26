ja3_configs = [
    {
      "ip": "141.164.52.100:23641",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_GREASE (0xAAAA)",
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "TLS_GREASE (0x9a9a)"
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "extensionEncryptedClientHello (boringssl) (65037)",
            "data": "0000010001ce0020b32add585045418bb827b3035a2a138d98a041ca62b79ed382aa0f59fb75b24200b09fdf2a3aba7b09e6839fea7e7d6639bac6a03b525fc17b753b29d1a48b542fd3ee4ab9bc746b38855d97c9cc61da2e3a11c0a389c63706b22b31933cc2fc59a21707fb85dad0d7910c4d4a97ce4d98768555d5a0529d9b1184ae816f274810e79b1807ff2850f8b9181864ebf25380c25f446e4823282570416c77f972e313378018c6311e3df1070688b866cccf69fad5bfa327afc81a9623cfdd407f07fb8a7916806bfbdd799de2de9197b35ef923"
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512"
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS_GREASE (0x3a3a)",
              "TLS 1.3",
              "TLS 1.2"
            ]
          },
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "TLS_GREASE (0xbaba)",
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)"
            ]
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "TLS_GREASE (0xbaba)": "00"
              },
              {
                "X25519 (29)": "cbfea5295917098bb6a58e9f6ba62f1889681025518bc60d8ca38c203320a816"
              }
            ]
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "application_settings (17513)",
            "protocols": [
              "h2"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "TLS_GREASE (0x0a0a)"
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,18-65037-27-13-45-43-0-10-35-5-23-51-65281-17513-11-16,29-23-24,0",
        "ja3_hash": "b4fb3730a7bdf8223b41c5e8dd021404",
        "ja4": "t13d1516h2_8daaf6152771_b1ff8ab2d16f",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "8ad9325e12f531d2983b78860de7b0ec",
        "client_random": "4a7b30a49d7749a58b5fa241fad272f9ed3608db3570828286c64c78e0cedb16",
        "session_id": "1b8d77172e9f56e3998fa955fd1a0ad40ac0423e5e4be24d5ed635fa9fe4fe75"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "ENABLE_PUSH = 0",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 445,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"Windows\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br, zstd",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 23641,
        "ip": {
          "id": 52732,
          "ttl": 54,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "141.164.52.100"
        },
        "tcp": {
          "ack": 2046008190,
          "checksum": 58381,
          "seq": 3739640074,
          "window": 83
        }
      }
    },
    {
        "ip": "141.164.52.100:28825",
        "http_version": "h2",
        "method": "GET",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "tls": {
            "ciphers": [
                "TLS_GREASE (0x7A7A)",
                "TLS_AES_128_GCM_SHA256",
                "TLS_AES_256_GCM_SHA384",
                "TLS_CHACHA20_POLY1305_SHA256",
                "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
                "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
                "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
                "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
                "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
                "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
                "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
                "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
                "TLS_RSA_WITH_AES_128_GCM_SHA256",
                "TLS_RSA_WITH_AES_256_GCM_SHA384",
                "TLS_RSA_WITH_AES_128_CBC_SHA",
                "TLS_RSA_WITH_AES_256_CBC_SHA"
            ],
            "extensions": [
                {
                    "name": "TLS_GREASE (0x2a2a)"
                },
                {
                    "name": "status_request (5)",
                    "status_request": {
                        "certificate_status_type": "OSCP (1)",
                        "responder_id_list_length": 0,
                        "request_extensions_length": 0
                    }
                },
                {
                    "name": "session_ticket (35)",
                    "data": ""
                },
                {
                    "name": "psk_key_exchange_modes (45)",
                    "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
                },
                {
                    "name": "supported_versions (43)",
                    "versions": [
                        "TLS_GREASE (0x8a8a)",
                        "TLS 1.3",
                        "TLS 1.2"
                    ]
                },
                {
                    "name": "ec_point_formats (11)",
                    "elliptic_curves_point_formats": [
                        "0x00"
                    ]
                },
                {
                    "name": "extensionEncryptedClientHello (boringssl) (65037)",
                    "data": "0000010001d60020e07f6335b9cdb0d729792f66408c43565911d45b72c67b74579c6c04956fbb3500b07772024e3147f071c19df5e421ef0231ae24dc06320e35e12b2a6a221f3ee0b46a630a1f55e2dca907baf1662e377a6a564a8d00a39f308946cda74deda4f4eb6bf938dbbb34b4bcb6b24b9c5d4bdde8a6374bb7939b62cf8c34ad80a534691f44c91fe33b7742699a351959591e36ffa8b5aae5fac3a960ba8e66107d33d19a58ff3389b669cf9c068be019309da23ea0e839ad36622114e65a31b1e3fcc99e79ef428f3ad1851172dc224f5ce1f59d"
                },
                {
                    "name": "server_name (0)",
                    "server_name": "tls.peet.ws"
                },
                {
                    "name": "key_share (51)",
                    "shared_keys": [
                        {
                            "TLS_GREASE (0x7a7a)": "00"
                        },
                        {
                            "X25519 (29)": "d9c661d5cfdc34abb2b9ed29608f19b9f3125298ceb0e33e49662c9961b8ec26"
                        }
                    ]
                },
                {
                    "name": "signed_certificate_timestamp (18)"
                },
                {
                    "name": "extensionRenegotiationInfo (boringssl) (65281)",
                    "data": "00"
                },
                {
                    "name": "application_layer_protocol_negotiation (16)",
                    "protocols": [
                        "h2",
                        "http/1.1"
                    ]
                },
                {
                    "name": "supported_groups (10)",
                    "supported_groups": [
                        "TLS_GREASE (0x7a7a)",
                        "X25519 (29)",
                        "P-256 (23)",
                        "P-384 (24)"
                    ]
                },
                {
                    "name": "extended_master_secret (23)",
                    "master_secret_data": "",
                    "extended_master_secret_data": ""
                },
                {
                    "name": "application_settings (17513)",
                    "protocols": [
                        "h2"
                    ]
                },
                {
                    "name": "signature_algorithms (13)",
                    "signature_algorithms": [
                        "ecdsa_secp256r1_sha256",
                        "rsa_pss_rsae_sha256",
                        "rsa_pkcs1_sha256",
                        "ecdsa_secp384r1_sha384",
                        "rsa_pss_rsae_sha384",
                        "rsa_pkcs1_sha384",
                        "rsa_pss_rsae_sha512",
                        "rsa_pkcs1_sha512"
                    ]
                },
                {
                    "name": "compress_certificate (27)",
                    "algorithms": [
                        "brotli (2)"
                    ]
                },
                {
                    "name": "TLS_GREASE (0x3a3a)"
                }
            ],
            "tls_version_record": "771",
            "tls_version_negotiated": "772",
            "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,5-35-45-43-11-65037-0-51-18-65281-16-10-23-17513-13-27,29-23-24,0",
            "ja3_hash": "d8ed43771952efd737ace8b655141c2b",
            "ja4": "t13d1516h2_8daaf6152771_b1ff8ab2d16f",
            "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
            "peetprint_hash": "8ad9325e12f531d2983b78860de7b0ec",
            "client_random": "2c6e2f7582b5744bcea77974ab9f064faa2978e53ea73b0323dcd2c6b923e133",
            "session_id": "ecd57acc8c24efc7e0bd97cc8f33af55c9f5127187f6c7be445baf35c062c49b"
        },
        "http2": {
            "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
            "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
            "sent_frames": [
                {
                    "frame_type": "SETTINGS",
                    "length": 24,
                    "settings": [
                        "HEADER_TABLE_SIZE = 65536",
                        "ENABLE_PUSH = 0",
                        "INITIAL_WINDOW_SIZE = 6291456",
                        "MAX_HEADER_LIST_SIZE = 262144"
                    ]
                },
                {
                    "frame_type": "WINDOW_UPDATE",
                    "length": 4,
                    "increment": 15663105
                },
                {
                    "frame_type": "HEADERS",
                    "stream_id": 1,
                    "length": 482,
                    "headers": [
                        ":method: GET",
                        ":authority: tls.peet.ws",
                        ":scheme: https",
                        ":path: /api/all",
                        "sec-ch-ua: \\\"Microsoft Edge\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
                        "sec-ch-ua-mobile: ?0",
                        "sec-ch-ua-platform: \\\"Windows\\",
                        "upgrade-insecure-requests: 1",
                        "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
                        "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "sec-fetch-site: none",
                        "sec-fetch-mode: navigate",
                        "sec-fetch-user: ?1",
                        "sec-fetch-dest: document",
                        "accept-encoding: gzip, deflate, br, zstd",
                        "accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
                    ],
                    "flags": [
                        "EndStream (0x1)",
                        "EndHeaders (0x4)",
                        "Priority (0x20)"
                    ],
                    "priority": {
                        "weight": 256,
                        "depends_on": 0,
                        "exclusive": 1
                    }
                }
            ]
        },
        "tcpip": {
            "cap_length": 66,
            "dst_port": 443,
            "src_port": 28825,
            "ip": {
                "id": 51068,
                "ttl": 54,
                "ip_version": 4,
                "dst_ip": "205.185.123.167",
                "src_ip": "141.164.52.100"
            },
            "tcp": {
                "ack": 728859184,
                "checksum": 42390,
                "seq": 94047335,
                "window": 83
            }
        }
    },
    {
      "ip": "141.164.52.100:19911",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/111",
      "tls": {
        "ciphers": [
          "TLS_GREASE (0xFAFA)",
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "TLS_GREASE (0x9a9a)"
          },
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "TLS_GREASE (0x4a4a)",
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512"
            ]
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "TLS_GREASE (0x4a4a)": "00"
              },
              {
                "X25519 (29)": "87ac92ab718e95655b5989377b37f9e9d1dbce7e23e4b381bd1a8572f146c417"
              }
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS_GREASE (0xdada)",
              "TLS 1.3",
              "TLS 1.2"
            ]
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "application_settings (17513)",
            "protocols": [
              "h2"
            ]
          },
          {
            "name": "TLS_GREASE (0x0a0a)"
          },
          {
            "name": "padding (21)",
            "padding_data_length": 408
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-21,29-23-24,0",
        "ja3_hash": "cd08e31494f9531f560d64c695473da9",
        "ja4": "t13d1516h2_8daaf6152771_5fb3489db586",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-21-23-27-35-43-45-5-51-65281-GREASE-GREASE",
        "peetprint_hash": "22a4f858cc83b9144c829ca411948a88",
        "client_random": "72ab3704baf815735a197714939e02c4989b5cb6b8cc0fbd7579d4ce469ac9d0",
        "session_id": "d679799792133cd4599d61caf46eae5918a575b03df13e343ae244b6c902959b"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,2:0,3:1000,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "46cedabdca2073198a42fa10ca4494d0",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 30,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "ENABLE_PUSH = 0",
              "MAX_CONCURRENT_STREAMS = 1000",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 443,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Chromium\\\";v=\\\"9\\\", \\\"Not?A_Brand\\\";v=\\\"8\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"Windows\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/111",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 19911,
        "ip": {
          "id": 26579,
          "ttl": 54,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "141.164.52.100"
        },
        "tcp": {
          "ack": 2130212721,
          "checksum": 37408,
          "seq": 3824687627,
          "window": 81
        }
      }
    },
    {
      "ip": "141.164.52.100:16105",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_GREASE (0xEAEA)",
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "TLS_GREASE (0xeaea)"
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "TLS_GREASE (0x3a3a)",
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)"
            ]
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "application_settings (17513)",
            "protocols": [
              "h2"
            ]
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "TLS_GREASE (0x3a3a)": "00"
              },
              {
                "X25519 (29)": "ec571e2229c3e594a521fa692a5d8877676650d8f06558d9e88eade13e6b837e"
              }
            ]
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS_GREASE (0xdada)",
              "TLS 1.3",
              "TLS 1.2"
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "extensionEncryptedClientHello (boringssl) (65037)",
            "data": "00000100019300209775db8603f53c5d97547b75f710fb586eaabf3e78fa9092e2207080bca650790090812d0ff8ba2944c052e3738e81689034bbed4057b4ea895403293ba9de048baec9edd7fe4fd4270a6c4c1dab858bab6538dbf114c31b9c83d81e07e349b3e3d63493c843fc341ce4d652483c0b244b1eacd222c1137b179efa4a87477c12140e2733513ca4f7bc9588ecd4059dc904aa231b53b5b6af2f14b305acb6b0dface7fecfe6495dfdc49351c1b20fb7263ec3"
          },
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "TLS_GREASE (0x2a2a)"
          },
          {
            "name": "padding (21)",
            "padding_data_length": 28
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,16-65281-10-35-17513-51-5-13-11-43-45-27-18-65037-0-23-21,29-23-24,0",
        "ja3_hash": "38866db8749fe7159cfc3667a2044ad6",
        "ja4": "t13d1517h2_8daaf6152771_39ff608a2b00",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-21-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "96b72764e015fb524fd8d005deb7209d",
        "client_random": "60443a49b4ed0bacb12f5c1ab790d1520eaa65f2e907e47f55849782a99cd216",
        "session_id": "8ad0382d81d608cb5a2897d5752b35bc14891ae60c65e6530cfae8a4ef16c166"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "ENABLE_PUSH = 0",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 445,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"Windows\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br, zstd",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 16105,
        "ip": {
          "id": 64019,
          "ttl": 54,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "141.164.52.100"
        },
        "tcp": {
          "ack": 3277666179,
          "checksum": 42241,
          "seq": 105110497,
          "window": 83
        }
      }
    },
    {
      "ip": "103.85.172.132:51740",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_GREASE (0x9A9A)",
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "TLS_GREASE (0x4a4a)"
          },
          {
            "name": "extensionEncryptedClientHello (boringssl) (65037)",
            "data": "0000010001cc0020350e96118d7a7302d1a00f92ce35478659ac77322c1aec52c3f3782c5524c62c0090c99d96f382ff6f8e32dc41308c46de477b68550b56ba85e99b104b0ece3b752f406c8ed8a64b4cf3f921ba4cfabca778f37e53bacb73c526ba175c3810926defb05980d64a0e82e57018f7e286c5e3cf0639b7d4d3230142a863c0bf91c676bf64b9043fcb962706c60b2c25f8ea3737c6e7fdc65525498621a5e799a931a021da14a66bfa72498ec7666aafba737868"
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "TLS_GREASE (0x0a0a)": "00"
              },
              {
                "X25519 (29)": "5faf5145cd17e0d89a33d0d3dcc7480d19f55c4e6e805a5dbed4742f8eafc736"
              }
            ]
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "TLS_GREASE (0x0a0a)",
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)"
            ]
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS_GREASE (0x1a1a)",
              "TLS 1.3",
              "TLS 1.2"
            ]
          },
          {
            "name": "application_settings (17513)",
            "protocols": [
              "h2"
            ]
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512"
            ]
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "TLS_GREASE (0x7a7a)"
          },
          {
            "name": "padding (21)",
            "padding_data_length": 28
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,65037-51-10-23-11-27-43-17513-16-45-35-0-65281-13-5-18-21,29-23-24,0",
        "ja3_hash": "b9ca227f51626186e863c34d45e39aa2",
        "ja4": "t13d1517h2_8daaf6152771_39ff608a2b00",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-21-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "96b72764e015fb524fd8d005deb7209d",
        "client_random": "cdc7ec43b5812c3169dbdbde02f0fbe4b2b0dec231a1b2ed9c6ea1c7f2c70016",
        "session_id": "d6c2259973e508a7571d92b6b5d2ebe8820da7571c880cef3f93daf6553ae57a"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "ENABLE_PUSH = 0",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 455,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"123\\\", \\\"Not:A-Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"123\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"macOS\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br, zstd",
              "accept-language: zh-CN,zh;q=0.9,en;q=0.8"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 583,
        "dst_port": 443,
        "src_port": 51740,
        "ip": {
          "ttl": 47,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "103.85.172.132"
        },
        "tcp": {
          "ack": 138335670,
          "checksum": 61864,
          "seq": 3443107417,
          "window": 2060
        }
      }
    },
    {
      "ip": "103.85.172.132:52325",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_AES_128_GCM_SHA256",
          "TLS_AES_256_GCM_SHA384",
          "TLS_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "X25519 (29)",
              "P-256 (23)",
              "P-384 (24)",
              "ffdhe3072 (257)"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "session_ticket (35)",
            "data": ""
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "rsa_pss_rsae_sha256",
              "rsa_pkcs1_sha256",
              "ecdsa_secp384r1_sha384",
              "rsa_pss_rsae_sha384",
              "rsa_pkcs1_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pkcs1_sha512",
              "rsa_pkcs1_sha1",
              "0x1010"
            ]
          },
          {
            "name": "signed_certificate_timestamp (18)"
          },
          {
            "name": "key_share (51)",
            "shared_keys": [
              {
                "X25519 (29)": "69588996c111f35109f3b7402043c4b6aab3ffd32a83f86299d053117d9bf26f"
              }
            ]
          },
          {
            "name": "psk_key_exchange_modes (45)",
            "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS 1.3",
              "TLS 1.2",
              "TLS 1.1",
              "TLS 1.0"
            ]
          },
          {
            "name": "compress_certificate (27)",
            "algorithms": [
              "brotli (2)"
            ]
          },
          {
            "name": "padding (21)",
            "padding_data_length": 122
          },
          {
            "name": "pre_shared_key (41)",
            "data": "00770071c9c8bf05f0a62843dc750d4020783270f04dc8c0a9a35ab06827cfea4dda539c6a3b42e5151030ea09459b51cebc90a53aa093081f3667fefc9393ff81874e7a7ea06c624f1dac946957d503692154d66b8ade5eef40850fdca141fc54d2342d0e8d13e39c5671f02510a2f1248e2aca1ac67a1c4a002120c508b629e6aa0280e3bc9e36ccca4698861ffa261bebe12de4bbe0e471f55abb"
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53-10,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-21-41,29-23-24-257,0",
        "ja3_hash": "19c8cf31d7e69a1956e3bc4c96693bce",
        "ja4": "t13d1616h2_46e7e9700bed_b0b0b1c1b67b",
        "peetprint": "772-771-770-769|2-1.1|29-23-24-257|1027-2052-1025-1283-2053-1281-2054-1537-513-4112|1|2|4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53-10|0-10-11-13-16-18-21-23-27-35-41-43-45-5-51-65281",
        "peetprint_hash": "8e3499602cab6f7da6c6a5bf07789690",
        "client_random": "9696c68eaa96f5764e1a100d8309f6fccd8d34a6a097da110718427e6190749c",
        "session_id": "7458565e3e74fd0f9173674f51cfb1040fba703b77a1a58e9db9340da18a28ca"
      },
      "http2": {
        "akamai_fingerprint": "1:65536,3:1000,4:6291456|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "0671021d33b7fb9f0728b3e8f0ee1089",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 18,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "MAX_CONCURRENT_STREAMS = 1000",
              "INITIAL_WINDOW_SIZE = 6291456"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 307,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "accept-encoding: gzip, deflate, br",
              "accept-language: zh-CN,zh;q=0.9,en;q=0.8"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)",
              "Priority (0x20)"
            ],
            "priority": {
              "weight": 256,
              "depends_on": 0,
              "exclusive": 1
            }
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 52325,
        "ip": {
          "ttl": 47,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "103.85.172.132"
        },
        "tcp": {
          "ack": 1350460121,
          "checksum": 64235,
          "seq": 2255574087,
          "window": 2054
        }
      }
    },
    {
      "ip": "49.157.47.219:25733",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "P-256 (23)",
              "P-384 (24)",
              "P-521 (25)"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "ecdsa_secp384r1_sha384",
              "ecdsa_secp521r1_sha512",
              "rsa_pss_rsae_sha256",
              "rsa_pss_rsae_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pss_pss_sha256",
              "rsa_pss_pss_sha384",
              "rsa_pss_pss_sha512",
              "rsa_pkcs1_sha256",
              "rsa_pkcs1_sha384",
              "rsa_pkcs1_sha512",
              "0x402",
              "0x303",
              "0x301",
              "0x302",
              "ecdsa_sha1",
              "rsa_pkcs1_sha1",
              "0x202"
            ]
          },
          {
            "name": "signature_algorithms_cert (50)",
            "data": "00260403050306030804080508060809080a080b0401050106010402030303010302020302010202"
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "status_request_v2 (17)",
            "data": "000702000400000000"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS 1.2"
            ]
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "771",
        "ja3": "771,49195-49199-49196-49200-49171-49172-156-157-47-53,0-5-10-11-13-50-16-17-23-43-65281,23-24-25,0",
        "ja3_hash": "25caec08e73f3efac7cfd90ccb3a3849",
        "ja4": "t12d1011h2_75366a718a82_f1763c68ef9b",
        "peetprint": "771|2-1.1|23-24-25|1027-1283-1539-2052-2053-2054-2057-2058-2059-1025-1281-1537-1026-771-769-770-515-513-514|0||49195-49199-49196-49200-49171-49172-156-157-47-53|0-10-11-13-16-17-23-43-5-50-65281",
        "peetprint_hash": "ec56fe83bccdadd977cab849582adad8",
        "client_random": "4f14a26d7ccebb39583aac4c62c03deb6f34ec96e0d1d18a00029eecf6321b97",
        "session_id": ""
      },
      "http2": {
        "akamai_fingerprint": "1:65536,3:1000,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "7ad845f20fc17cc8088a0d9312b17da1",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "MAX_CONCURRENT_STREAMS = 1000",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 436,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\"Google Chrome\\\";v=\\\"105\\\", \\\"Not)A;Brand\\\";v=\\\"8\\\", \\\"Chromium\\\";v=\\\"105\\",
              "sec-ch-ua-mobile: ?0",
              "sec-ch-ua-platform: \\\"Windows\\",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)"
            ]
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 25733,
        "ip": {
          "id": 52408,
          "ttl": 55,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "49.157.47.219"
        },
        "tcp": {
          "ack": 1770676555,
          "checksum": 60742,
          "seq": 2717094645,
          "window": 83
        }
      }
    },
    {
      "ip": "49.157.47.219:11745",
      "http_version": "h2",
      "method": "GET",
      "user_agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
      "tls": {
        "ciphers": [
          "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
          "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
          "TLS_RSA_WITH_AES_128_GCM_SHA256",
          "TLS_RSA_WITH_AES_256_GCM_SHA384",
          "TLS_RSA_WITH_AES_128_CBC_SHA",
          "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
          {
            "name": "server_name (0)",
            "server_name": "tls.peet.ws"
          },
          {
            "name": "status_request (5)",
            "status_request": {
              "certificate_status_type": "OSCP (1)",
              "responder_id_list_length": 0,
              "request_extensions_length": 0
            }
          },
          {
            "name": "supported_groups (10)",
            "supported_groups": [
              "P-256 (23)",
              "P-384 (24)",
              "P-521 (25)"
            ]
          },
          {
            "name": "ec_point_formats (11)",
            "elliptic_curves_point_formats": [
              "0x00"
            ]
          },
          {
            "name": "signature_algorithms (13)",
            "signature_algorithms": [
              "ecdsa_secp256r1_sha256",
              "ecdsa_secp384r1_sha384",
              "ecdsa_secp521r1_sha512",
              "rsa_pss_rsae_sha256",
              "rsa_pss_rsae_sha384",
              "rsa_pss_rsae_sha512",
              "rsa_pss_pss_sha256",
              "rsa_pss_pss_sha384",
              "rsa_pss_pss_sha512",
              "rsa_pkcs1_sha256",
              "rsa_pkcs1_sha384",
              "rsa_pkcs1_sha512",
              "0x402",
              "0x303",
              "0x301",
              "0x302",
              "ecdsa_sha1",
              "rsa_pkcs1_sha1",
              "0x202"
            ]
          },
          {
            "name": "signature_algorithms_cert (50)",
            "data": "00260403050306030804080508060809080a080b0401050106010402030303010302020302010202"
          },
          {
            "name": "application_layer_protocol_negotiation (16)",
            "protocols": [
              "h2",
              "http/1.1"
            ]
          },
          {
            "name": "status_request_v2 (17)",
            "data": "000702000400000000"
          },
          {
            "name": "extended_master_secret (23)",
            "master_secret_data": "",
            "extended_master_secret_data": ""
          },
          {
            "name": "supported_versions (43)",
            "versions": [
              "TLS 1.2"
            ]
          },
          {
            "name": "extensionRenegotiationInfo (boringssl) (65281)",
            "data": "00"
          }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "771",
        "ja3": "771,49195-49199-49196-49200-49171-49172-156-157-47-53,0-5-10-11-13-50-16-17-23-43-65281,23-24-25,0",
        "ja3_hash": "25caec08e73f3efac7cfd90ccb3a3849",
        "ja4": "t12d1011h2_75366a718a82_f1763c68ef9b",
        "peetprint": "771|2-1.1|23-24-25|1027-1283-1539-2052-2053-2054-2057-2058-2059-1025-1281-1537-1026-771-769-770-515-513-514|0||49195-49199-49196-49200-49171-49172-156-157-47-53|0-10-11-13-16-17-23-43-5-50-65281",
        "peetprint_hash": "ec56fe83bccdadd977cab849582adad8",
        "client_random": "dab0f550ae76dc93054485564033512ec839e03eb533e0261931f5a7cdfa096c",
        "session_id": ""
      },
      "http2": {
        "akamai_fingerprint": "1:65536,3:1000,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "7ad845f20fc17cc8088a0d9312b17da1",
        "sent_frames": [
          {
            "frame_type": "SETTINGS",
            "length": 24,
            "settings": [
              "HEADER_TABLE_SIZE = 65536",
              "MAX_CONCURRENT_STREAMS = 1000",
              "INITIAL_WINDOW_SIZE = 6291456",
              "MAX_HEADER_LIST_SIZE = 262144"
            ]
          },
          {
            "frame_type": "WINDOW_UPDATE",
            "length": 4,
            "increment": 15663105
          },
          {
            "frame_type": "HEADERS",
            "stream_id": 1,
            "length": 394,
            "headers": [
              ":method: GET",
              ":authority: tls.peet.ws",
              ":scheme: https",
              ":path: /api/all",
              "sec-ch-ua: \\\" Not A;Brand\\\";v=\\\"99\\\", \\\"Chromium\\\";v=\\\"92\\",
              "sec-ch-ua-mobile: ?0",
              "upgrade-insecure-requests: 1",
              "user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
              "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "sec-fetch-site: none",
              "sec-fetch-mode: navigate",
              "sec-fetch-user: ?1",
              "sec-fetch-dest: document",
              "accept-encoding: gzip, deflate, br",
              "accept-language: zh-CN,zh;q=0.9"
            ],
            "flags": [
              "EndStream (0x1)",
              "EndHeaders (0x4)"
            ]
          }
        ]
      },
      "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 11745,
        "ip": {
          "id": 5309,
          "ttl": 55,
          "ip_version": 4,
          "dst_ip": "205.185.123.167",
          "src_ip": "49.157.47.219"
        },
        "tcp": {
          "ack": 955169648,
          "checksum": 31775,
          "seq": 1121261300,
          "window": 83
        }
      }
    },
    {
    "ip": "38.48.121.158:39904",
    "http_version": "h2",
    "method": "GET",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "tls": {
        "ciphers": [
            "TLS_GREASE (0x6A6A)",
            "TLS_AES_128_GCM_SHA256",
            "TLS_AES_256_GCM_SHA384",
            "TLS_CHACHA20_POLY1305_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
            "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
            "TLS_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_RSA_WITH_AES_128_CBC_SHA",
            "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
            {
                "name": "TLS_GREASE (0xfafa)"
            },
            {
                "name": "key_share (51)",
                "shared_keys": [
                    {
                        "TLS_GREASE (0xcaca)": "00"
                    },
                    {
                        "X25519Kyber768 (25497)": "bec136303df53c379193ceb24d1cf0c639a84f3e7e49663562fb3c3552484b5441c544c7926dc5cc509d213e0fe0c9fef6b9dcaabff90987e829c872b69f6df85d0ca79becec7c0c30a0dd02499f43a3e50521def385e3c4534a8045fa3921dcec0113e50014044e9e49b8c96b4b6b1095f8431a39bc1a9a5a0b9f555c17c30c7f858ad400c92ca4c1df9b30c5024964295f73f174af494a97c1407eb1a39e1373dd951cfb1a187959afeb831cbd4bb9fbe9156631ba675989db4616dfc45eb4080ddbc4530fc389eb76039c949048e229e6917f2487793e153cfd5a448b7a0e24b3160dfcc604c3c070f9323e77c49c2c435b12a128c06e68368b3dc8a10b39a845209307b6290da72e953baf8bbab62e99a7ed0728c984b9cb832531a4c213c03e63b71898ba2266ba8b284a7d9f4329784615db4277e098adaab371d3ac6031ac2b602613a4e729b72a2bd9d892790044cfa23c477bc1f3e37edba1a6571051650b3af47553ebfc6534c1c21a3082bdd1a462202c0f7c3094b05cb5fa3b20f156a686c744bba8ecf0a4160993a7944bda584a923c8a531205a09123fe06504e54c144663e9858ad7e113f7de3918ce8cddb08859ab2b253ca331dd50e4831c6739712adb2c2fb92c1afa91027521757ccbbfd79bde4d63aead1ced8292165b1ccf6d5838c8b57a7dbcdb0972274e7cb36a79537455b5aea6b23c748f58277ca9ab59c706f91ec8ddec155476625557c0e63aa6563643a11745cfeac704ce79eb8e9bbd8b2304bf776592814f112c931887f33331cc0f520c2784b48bb5bec819766e85088e5c4c36b48355b25c04181dee17ae9c52ea7d5598f98482ef5ae7be2b2d4c435c1486dc3d11778b4876de38f7020702c063f95734ee41000897a02d07727c1744e8f9b1f9abc182863c7d31909e73291fdb82bc26c0ae5931f4b6c4a80532272110a2ed74f9ab00b478a2aed79113c08013593529301538a0b2f7b04316dd46ff0dc02205056984a52673c0a0564891de5b198647ba5b404ad862d87cb0f30a8865e3b282c83a35d307951f231a85c5c80f6c4c31cb0c8d347f74187239a4831a3005faa9cccb32b54459d2df430f9f47306e2c1a910b03fc35cf89640da128903e57937a65a14d056e59220439ab8d876c57b27099348a553e07c351cb6d9149ed6f842f7ba800a745321d4baae62b7ed7386517529b7e789f3fc9f19f8a457589426b812228167a89230558b6841b02ce5678edc51cad48b61f372919c0176c9d086e6c268029017764b505a8265e7a9c809051c741bbadae6af022814d19a10cd6685410c1c40da4799a5559849be746329562518c5fa7b4ba2a31ca806f2a2b435c438add2149bd12eee7a546ab87b9044adc0c947500c39411a3e6a4c39eb6b3e25c4a7e2c3256a09ce3a243c29b2a6baf74490f800a6a182b4c2ca83835c105a4a9c3bb5f21c613c3007e5649a67415a3a677c680a62f14a026c0c4a61832205401fef8604ba18261c836e05f95a01d106f4396b3257042cbc4a6da56ef04024b07cc0789b3d4bc4c1704834a46ba6b3c9670e730b9f8077ec71aa66fc160815b614a73c800229588bc5923aa14ae7ce2e82a716a33a3738097cd7131ddcc5f0b9bcab7abad20047e0606418a1c1296756d4866fff66008024c4a4255bdcc7faf1fec867c23e0ccd877a31cbc217f19d21bf7417cff4a0"
                    },
                    {
                        "X25519 (29)": "d9c632810fb6db38ef058f3bf0a7eec8fd6d9d9f716f1c06f10e3618731a4308"
                    }
                ]
            },
            {
                "name": "application_settings (17513)",
                "protocols": [
                    "h2"
                ]
            },
            {
                "name": "extended_master_secret (23)",
                "master_secret_data": "",
                "extended_master_secret_data": ""
            },
            {
                "name": "supported_versions (43)",
                "versions": [
                    "TLS_GREASE (0x0a0a)",
                    "TLS 1.3",
                    "TLS 1.2"
                ]
            },
            {
                "name": "application_layer_protocol_negotiation (16)",
                "protocols": [
                    "h2",
                    "http/1.1"
                ]
            },
            {
                "name": "psk_key_exchange_modes (45)",
                "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
            },
            {
                "name": "signature_algorithms (13)",
                "signature_algorithms": [
                    "ecdsa_secp256r1_sha256",
                    "rsa_pss_rsae_sha256",
                    "rsa_pkcs1_sha256",
                    "ecdsa_secp384r1_sha384",
                    "rsa_pss_rsae_sha384",
                    "rsa_pkcs1_sha384",
                    "rsa_pss_rsae_sha512",
                    "rsa_pkcs1_sha512"
                ]
            },
            {
                "name": "extensionRenegotiationInfo (boringssl) (65281)",
                "data": "00"
            },
            {
                "name": "signed_certificate_timestamp (18)"
            },
            {
                "name": "server_name (0)",
                "server_name": "tls.peet.ws"
            },
            {
                "name": "ec_point_formats (11)",
                "elliptic_curves_point_formats": [
                    "0x00"
                ]
            },
            {
                "name": "extensionEncryptedClientHello (boringssl) (65037)",
                "data": "0000010001b7002033e0923e80e39e71110abddbad0eeff0d232290200cba479d59fc9e0d756624600b034eb8cf1422f48d2d9eee1d7c49c8f397f0125366885ca63be4901c4ecd335b435a08d336267e330f9646c339e582e0e1f6cf6cef1135da81c3ad9063464868489809f143fc5f27487f4e7ab03a642afae20ca6d39969ad4f1bd7486b93596175589372e3a851ba38cb9b4baec40fc500d5017a1029411b1863c056de6916afb20a92ad583bcfc27ee77e88fa5465e7f34ebe8d62ae986073cbbafffca7d1e19796b3745af248dcef06198d0e5df5d43"
            },
            {
                "name": "status_request (5)",
                "status_request": {
                    "certificate_status_type": "OSCP (1)",
                    "responder_id_list_length": 0,
                    "request_extensions_length": 0
                }
            },
            {
                "name": "session_ticket (35)",
                "data": ""
            },
            {
                "name": "compress_certificate (27)",
                "algorithms": [
                    "brotli (2)"
                ]
            },
            {
                "name": "supported_groups (10)",
                "supported_groups": [
                    "TLS_GREASE (0xcaca)",
                    "X25519Kyber768 (25497)",
                    "X25519 (29)",
                    "P-256 (23)",
                    "P-384 (24)"
                ]
            },
            {
                "name": "TLS_GREASE (0x9a9a)"
            }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,51-17513-23-43-16-45-13-65281-18-0-11-65037-5-35-27-10,25497-29-23-24,0",
        "ja3_hash": "dccca2ad4ece465792ff52f315e20876",
        "ja4": "t13d1516h2_8daaf6152771_b1ff8ab2d16f",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-25497-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "b8ce945a4d9a7a9b5b6132e3658fe033",
        "client_random": "cf89f60e97462023f8853fef6a93d5dfd77a77b3c9ac299664de92b7a3e4f53f",
        "session_id": "78aa24ea1075061d99532b72b48ce6f151845719660d8ac1dd040bd81115cd30"
    },
    "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
            {
                "frame_type": "SETTINGS",
                "length": 24,
                "settings": [
                    "HEADER_TABLE_SIZE = 65536",
                    "ENABLE_PUSH = 0",
                    "INITIAL_WINDOW_SIZE = 6291456",
                    "MAX_HEADER_LIST_SIZE = 262144"
                ]
            },
            {
                "frame_type": "WINDOW_UPDATE",
                "length": 4,
                "increment": 15663105
            },
            {
                "frame_type": "HEADERS",
                "stream_id": 1,
                "length": 496,
                "headers": [
                    ":method: GET",
                    ":authority: tls.peet.ws",
                    ":scheme: https",
                    ":path: /api/all",
                    "sec-ch-ua: \\\"Chromium\\\";v=\\\"124\\\", \\\"Microsoft Edge\\\";v=\\\"124\\\", \\\"Not-A.Brand\\\";v=\\\"99\\",
                    "sec-ch-ua-mobile: ?0",
                    "sec-ch-ua-platform: \\\"Windows\\",
                    "upgrade-insecure-requests: 1",
                    "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
                    "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "sec-fetch-site: none",
                    "sec-fetch-mode: navigate",
                    "sec-fetch-user: ?1",
                    "sec-fetch-dest: document",
                    "accept-encoding: gzip, deflate, br, zstd",
                    "accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "priority: u=0, i"
                ],
                "flags": [
                    "EndStream (0x1)",
                    "EndHeaders (0x4)",
                    "Priority (0x20)"
                ],
                "priority": {
                    "weight": 256,
                    "depends_on": 0,
                    "exclusive": 1
                }
            }
        ]
    },
    "tcpip": {
        "cap_length": 66,
        "dst_port": 443,
        "src_port": 39904,
        "ip": {
            "id": 14820,
            "tos": 40,
            "ttl": 51,
            "ip_version": 4,
            "dst_ip": "205.185.123.167",
            "src_ip": "38.48.121.158"
        },
        "tcp": {
            "ack": 2342331392,
            "checksum": 5740,
            "seq": 1582222622,
            "window": 492
        }
    }
},
    {
    "ip": "38.48.121.158:36250",
    "http_version": "h2",
    "method": "GET",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "tls": {
        "ciphers": [
            "TLS_GREASE (0x8A8A)",
            "TLS_AES_128_GCM_SHA256",
            "TLS_AES_256_GCM_SHA384",
            "TLS_CHACHA20_POLY1305_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
            "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
            "TLS_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_RSA_WITH_AES_128_CBC_SHA",
            "TLS_RSA_WITH_AES_256_CBC_SHA"
        ],
        "extensions": [
            {
                "name": "TLS_GREASE (0x8a8a)"
            },
            {
                "name": "session_ticket (35)",
                "data": ""
            },
            {
                "name": "supported_groups (10)",
                "supported_groups": [
                    "TLS_GREASE (0xaaaa)",
                    "X25519Kyber768 (25497)",
                    "X25519 (29)",
                    "P-256 (23)",
                    "P-384 (24)"
                ]
            },
            {
                "name": "signature_algorithms (13)",
                "signature_algorithms": [
                    "ecdsa_secp256r1_sha256",
                    "rsa_pss_rsae_sha256",
                    "rsa_pkcs1_sha256",
                    "ecdsa_secp384r1_sha384",
                    "rsa_pss_rsae_sha384",
                    "rsa_pkcs1_sha384",
                    "rsa_pss_rsae_sha512",
                    "rsa_pkcs1_sha512"
                ]
            },
            {
                "name": "compress_certificate (27)",
                "algorithms": [
                    "brotli (2)"
                ]
            },
            {
                "name": "key_share (51)",
                "shared_keys": [
                    {
                        "TLS_GREASE (0xaaaa)": "00"
                    },
                    {
                        "X25519Kyber768 (25497)": "737fcc496b0de2aedadc027b67ead6151aafb28e1158ceb03554e7f04f53f13da46587ee799f965ca1e7837386e354bf201d9ffcb2fee2be23cc06deb33287c74bba33ba591a1d8d40aa818276cf6cc04400c0045ca78d49cfa8e67560261e2758a46ef624f6a23df058275eb2985ef5cc5c013ecac70c0f429deb2c7a421722effbca29fcc1931a4cebb0c96fe75e923b0dc542a70be9981b75589c14643ef26fdb472c4a8c2bba495bccb84be5939f5af37cc35259c71953d79880134945bfa2cfffa40b68a8577fb93c4fe8b9750565eeb30f703c3c9ac43560e6673c720737b422687648132ab295c0a91ffb6cf5c07c3d9b4ea0d952e8e060d8f817082446df578ec56988be7b0a2246146f29759c0698441c5723729ec06b30810538e96808349c03ac1aa035cc3f0e40122c34136586833f626c56a8764bd1285ec49ad20b724d3b1079c09c26fc4f35b6713b6a013461000e62a31d995b17b83047970bb92b006169ab767a642b3056ff41b176876ec535aed23ac2fc37b203c02932c42ab15910f290a87a750c53725036375d56d3462291cc0d8952ebeb40495780dbab81dec91a1d346e5db5cbfe65079f672f6a1790696bb1cd50c053b8b28ea30ecb2865013aa0e50c01d87a8601e11865881fc8f7b5dd661448d8a9abd4c65ac0893a50cac9e53fb0bc025fe907307c6988e715b0f3789f0686cc40a1b2f296ab02ccff217cc431c515b234b50a1dac40a321191e42308b185871b9404d1520ceabe66b720c410b7c291bf4144cf739228c2ffc40234820975eb41b71912c76f956f2b03548313e7a2ab7e7db85b241916b8c421a695892a97001f92431ea61fd335b24ab750240ceca3787efa56cfd714887148f2d9b43583b4cce98926511c14b0c8419e4c0d08a9bce75c0cc8a145a6ac0805c263b56698db32d1e618c5be91091c12f26102db28c3ea5336bd9983b17bcb161e3360658ce4f291286d74da7e2bc0948ae0ec4a61c9cad49b64e15003395a84b691b0d3dc1ce9bd757c00bb6d1870620a4182f10bcf2d486c1d99d2212751a0296d77cbb5fd53c62d716a2434069b59af4f2703738128f3022094971fa42bbd5249036b4cfd4197ccd8676a2712cec3c7204f839d6d97293fc7d086a550341478751567da347aa699ab7497e5b21c8a2997c8a5b82293c8786604cf9283633e0c4349c256a12b80eb4ba37047fece9ab18abc4e5308ae6bbac9accb3e8b2b47286c92a545b60b81b7d8223e7c7513aeab2aff7bc0a88353e3320c858c5e1679aabb886e8d19373063c572b9a492a06478c12164b7f1aa572cb90a40dfc00a8439d17b31a8ca50f37ec9c7c3765d018a9642805cc64c935397293c5150773c27eaa875c562ae8f90cc5c73f19623a51c16d757781d77673efc9526719b6c12131617b5248d88e5c54cfa757a688b8762900b483dc5ec1b83df3b5a026a7b87763aa17234956f5635ff15c8111c412327c5cf7a6a1141acaf15e6e29977e4a7ed856157bd7511cdba3050a75b95c9ab857593d1026fdca4338077dff538e9b24c87a666e5f81ca68c195f5e9cf8ab93edc5b5d20b7195ca96c4a4724df5179c1ecc1f8374ff421a662523ddc012fd1c9351ee8c48ef62b1ce1b3dfd80763782b8854b76e9c84792b742ed2a03297d899dead9d646177593104e553d3e2c3bbfee7d39e2dc8d428b2a4a1cffd"
                    },
                    {
                        "X25519 (29)": "614ef223d812ea1e2e701031ec748aad7bd33dd451f83c33f7288ebd50f7bf6e"
                    }
                ]
            },
            {
                "name": "extended_master_secret (23)",
                "master_secret_data": "",
                "extended_master_secret_data": ""
            },
            {
                "name": "signed_certificate_timestamp (18)"
            },
            {
                "name": "extensionRenegotiationInfo (boringssl) (65281)",
                "data": "00"
            },
            {
                "name": "application_settings (17513)",
                "protocols": [
                    "h2"
                ]
            },
            {
                "name": "server_name (0)",
                "server_name": "tls.peet.ws"
            },
            {
                "name": "application_layer_protocol_negotiation (16)",
                "protocols": [
                    "h2",
                    "http/1.1"
                ]
            },
            {
                "name": "extensionEncryptedClientHello (boringssl) (65037)",
                "data": "0000010001c7002047fb7990527c763aa4ed38ba21076c67c6ffc16bdae607077eac65e2e2c2692900d0eee9993bc3fa9c15265f848ee377913869396c6b28f7a08897c625163fb1f24595c91ed405f24d850c78b51571c6387839df6e02ded89d766b1ffa81403a8282efe295556a50a01e6cbca0b44436c94902067c0d1759c81dda55dbbca5811fa078ee7435f553561ab4fafb36ad7877a10382efafc26dddadd3a5dd15dec3a7694ab6f2dbf1be5d71c9cf18ef2a33659d5dff03961364ca2d3ee48fcfcef7eae7decd027e2526a1ce9a2b3ba27920a4fb8039fb20c99cd166fc2c0ef99a02e98964df0fcf87448b52967536560bb29b46"
            },
            {
                "name": "supported_versions (43)",
                "versions": [
                    "TLS_GREASE (0xfafa)",
                    "TLS 1.3",
                    "TLS 1.2"
                ]
            },
            {
                "name": "ec_point_formats (11)",
                "elliptic_curves_point_formats": [
                    "0x00"
                ]
            },
            {
                "name": "status_request (5)",
                "status_request": {
                    "certificate_status_type": "OSCP (1)",
                    "responder_id_list_length": 0,
                    "request_extensions_length": 0
                }
            },
            {
                "name": "psk_key_exchange_modes (45)",
                "PSK_Key_Exchange_Mode": "PSK with (EC)DHE key establishment (psk_dhe_ke) (1)"
            },
            {
                "name": "TLS_GREASE (0xbaba)"
            }
        ],
        "tls_version_record": "771",
        "tls_version_negotiated": "772",
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,35-10-13-27-51-23-18-65281-17513-0-16-65037-43-11-5-45,25497-29-23-24,0",
        "ja3_hash": "75eefb67ce0e57997277c3d6362ad040",
        "ja4": "t13d1516h2_8daaf6152771_b1ff8ab2d16f",
        "peetprint": "GREASE-772-771|2-1.1|GREASE-25497-29-23-24|1027-2052-1025-1283-2053-1281-2054-1537|1|2|GREASE-4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53|0-10-11-13-16-17513-18-23-27-35-43-45-5-51-65037-65281-GREASE-GREASE",
        "peetprint_hash": "b8ce945a4d9a7a9b5b6132e3658fe033",
        "client_random": "da74b8040d2e1c7746fcd766b08308f600f4d6fca78953b7ab2cc22b8d856e57",
        "session_id": "51489f814ce3c8097b4b83d3d751da4940073426908e837baeffd1d2ddac0d14"
    },
    "http2": {
        "akamai_fingerprint": "1:65536,2:0,4:6291456,6:262144|15663105|0|m,a,s,p",
        "akamai_fingerprint_hash": "90224459f8bf70b7d0a8797eb916dbc9",
        "sent_frames": [
            {
                "frame_type": "SETTINGS",
                "length": 24,
                "settings": [
                    "HEADER_TABLE_SIZE = 65536",
                    "ENABLE_PUSH = 0",
                    "INITIAL_WINDOW_SIZE = 6291456",
                    "MAX_HEADER_LIST_SIZE = 262144"
                ]
            },
            {
                "frame_type": "WINDOW_UPDATE",
                "length": 4,
                "increment": 15663105
            },
            {
                "frame_type": "HEADERS",
                "stream_id": 1,
                "length": 460,
                "headers": [
                    ":method: GET",
                    ":authority: tls.peet.ws",
                    ":scheme: https",
                    ":path: /api/all",
                    "sec-ch-ua: \\\"Chromium\\\";v=\\\"124\\\", \\\"Google Chrome\\\";v=\\\"124\\\", \\\"Not-A.Brand\\\";v=\\\"99\\",
                    "sec-ch-ua-mobile: ?0",
                    "sec-ch-ua-platform: \\\"Windows\\",
                    "upgrade-insecure-requests: 1",
                    "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                    "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "sec-fetch-site: none",
                    "sec-fetch-mode: navigate",
                    "sec-fetch-user: ?1",
                    "sec-fetch-dest: document",
                    "accept-encoding: gzip, deflate, br, zstd",
                    "accept-language: zh-CN,zh;q=0.9",
                    "priority: u=0, i"
                ],
                "flags": [
                    "EndStream (0x1)",
                    "EndHeaders (0x4)",
                    "Priority (0x20)"
                ],
                "priority": {
                    "weight": 256,
                    "depends_on": 0,
                    "exclusive": 1
                }
            }
        ]
    },
    "tcpip": {
        "cap_length": 130,
        "dst_port": 443,
        "src_port": 36250,
        "ip": {
            "id": 16182,
            "tos": 40,
            "ttl": 51,
            "ip_version": 4,
            "dst_ip": "205.185.123.167",
            "src_ip": "38.48.121.158"
        },
        "tcp": {
            "ack": 3428067641,
            "checksum": 49087,
            "seq": 3064256554,
            "window": 501
        }
    }
}
]


server_config = {
    "captcha_port": 18999,
    "server_port": 30200
}


host = {
    "3": "al",
    "5": "ad",
    "10": "am",
    "12": "au",
    "13": "at",
    "14": "az",
    "16": "bh",
    "20": "be",
    "26": "ba",
    "29": "br",
    "32": "bg",
    "37": "ca",
    "42": "cl",
    "45": "co",
    "49": "cr",
    "50": "hr",
    "52": "cy",
    "53": "cz",
    "54": "dk",
    "57": "do",
    "64": "ee",
    "68": "fi",
    "69": "fr",
    "75": "ge",
    "76": "de",
    "79": "gr",
    "83": "gu",
    "90": "hu",
    "91": "is",
    "96": "ie",
    "97": "il",
    "98": "it",
    "100": "jp",
    "101": "jo",
    "102": "kz",
    "105": "kw",
    "108": "lv",
    "109": "lb",
    "113": "lt",
    "114": "lu",
    "116": "mk",
    "119": "my",
    "122": "mt",
    "126": "mu",
    "128": "mx",
    "130": "md",
    "134": "me",
    "135": "ma",
    "141": "nl",
    "144": "nz",
    "151": "no",
    "152": "om",
    "159": "pe",
    "160": "ph",
    "162": "pl",
    "163": "pt",
    "164": "pr",
    "165": "qa",
    "167": "ro",
    "174": "sa",
    "175": "rs",
    "179": "sg",
    "180": "sk",
    "181": "si",
    "184": "za",
    "185": "kr",
    "186": "es",
    "191": "se",
    "192": "ch",
    "194": "tw",
    "197": "th",
    "203": "tr",
    "208": "ua",
    "209": "ae",
    "210": "uk",
    "211": "us",
    "212": "uy",
    "219": "vi",
    "235": "xk",
    "236": "mp"
}
gV = {
    "us": {
        "id": 211,
        "dr": "us",
        "ldp": "us"
    },
    "ca": {
        "id": 37,
        "dr": "us",
        "ldp": "ca"
    },
    "au": {
        "id": 12,
        "dr": "us",
        "ldp": "au"
    },
    "nz": {
        "id": 144,
        "dr": "us",
        "ldp": "nz"
    },
    "uk": {
        "id": 210,
        "dr": "eu"
    },
    "de": {
        "id": 76,
        "dr": "eu"
    },
    "fr": {
        "id": 69,
        "dr": "eu"
    },
    "it": {
        "id": 98,
        "dr": "eu"
    },
    "nl": {
        "id": 141,
        "dr": "eu"
    },
    "es": {
        "id": 186,
        "dr": "eu"
    },
    "mx": {
        "id": 128,
        "dr": "us"
    },
    "at": {
        "id": 13,
        "dr": "eu"
    },
    "be": {
        "id": 20,
        "dr": "eu"
    },
    "pt": {
        "id": 163,
        "dr": "eu"
    },
    "pl": {
        "id": 162,
        "dr": "eu"
    },
    "se": {
        "id": 191,
        "dr": "eu"
    },
    "ch": {
        "id": 192,
        "dr": "eu"
    },
    "ro": {
        "id": 167,
        "dr": "eu"
    },
    "gr": {
        "id": 79,
        "dr": "eu"
    },
    "cz": {
        "id": 53,
        "dr": "eu"
    },
    "hu": {
        "id": 90,
        "dr": "eu"
    },
    "ie": {
        "id": 96,
        "dr": "eu"
    },
    "dk": {
        "id": 54,
        "dr": "eu"
    },
    "fi": {
        "id": 68,
        "dr": "eu"
    },
    "sk": {
        "id": 180,
        "dr": "eu"
    },
    "si": {
        "id": 181,
        "dr": "eu"
    },
    "ee": {
        "id": 64,
        "dr": "eu"
    },
    "lv": {
        "id": 108,
        "dr": "eu"
    },
    "mt": {
        "id": 122,
        "dr": "eu"
    },
    "cy": {
        "id": 52,
        "dr": "eu"
    },
    "bg": {
        "id": 32,
        "dr": "eu"
    },
    "hr": {
        "id": 50,
        "dr": "eu"
    },
    "lt": {
        "id": 113,
        "dr": "eu"
    },
    "lu": {
        "id": 114,
        "dr": "eu"
    },
    "jp": {
        "id": 100,
        "dr": "us",
        "ldp": "jp"
    },
    "kr": {
        "id": 185,
        "dr": "us",
        "ldp": "kr"
    },
    "sa": {
        "id": 174,
        "dr": "eu",
        "ldp": "qa"
    },
    "ae": {
        "id": 209,
        "dr": "eu",
        "ldp": "qa"
    },
    "kw": {
        "id": 105,
        "dr": "eu",
        "ldp": "qa"
    },
    "no": {
        "id": 151,
        "dr": "eu"
    },
    "sg": {
        "id": 179,
        "dr": "us",
        "ldp": "sg"
    },
    "cl": {
        "id": 42,
        "dr": "us",
        "ldp": "br"
    },
    "br": {
        "id": 29,
        "dr": "us",
        "ldp": "br"
    },
    "ph": {
        "id": 160,
        "dr": "us",
        "ldp": "jp"
    },
    "il": {
        "id": 97,
        "dr": "eu"
    },
    "my": {
        "id": 119,
        "dr": "us",
        "ldp": "sg"
    },
    "qa": {
        "id": 165,
        "dr": "eu",
        "ldp": "qa"
    },
    "bh": {
        "id": 16,
        "dr": "eu",
        "ldp": "qa"
    },
    "om": {
        "id": 152,
        "dr": "eu",
        "ldp": "qa"
    },
    "tw": {
        "id": 194,
        "dr": "us",
        "ldp": "jp"
    },
    "th": {
        "id": 197,
        "dr": "us",
        "ldp": "sg"
    },
    "lb": {
        "id": 109,
        "dr": "eu",
        "ldp": "qa"
    },
    "jo": {
        "id": 101,
        "dr": "eu",
        "ldp": "qa"
    },
    "za": {
        "id": 184,
        "dr": "eu",
        "ldp": "za"
    },
    "rs": {
        "id": 175,
        "dr": "eu"
    },
    "md": {
        "id": 130,
        "dr": "eu"
    },
    "me": {
        "id": 134,
        "dr": "eu"
    },
    "is": {
        "id": 91,
        "dr": "eu"
    },
    "ad": {
        "id": 5,
        "dr": "eu"
    },
    "ba": {
        "id": 26,
        "dr": "eu"
    },
    "al": {
        "id": 3,
        "dr": "eu"
    },
    "mk": {
        "id": 116,
        "dr": "eu"
    },
    "xk": {
        "id": 235,
        "dr": "eu"
    },
    "kz": {
        "id": 102,
        "dr": "eu"
    },
    "co": {
        "id": 45,
        "dr": "us"
    },
    "az": {
        "id": 14,
        "dr": "eu"
    },
    "ua": {
        "id": 208,
        "dr": "eu"
    },
    "uy": {
        "id": 212,
        "dr": "us",
        "ldp": "br"
    },
    "mu": {
        "id": 126,
        "dr": "eu",
        "ldp": "za"
    },
    "pe": {
        "id": 159,
        "dr": "us",
        "ldp": "br"
    },
    "ge": {
        "id": 75,
        "dr": "eu"
    },
    "am": {
        "id": 10,
        "dr": "eu"
    },
    "ma": {
        "id": 135,
        "dr": "eu"
    },
    "do": {
        "id": 57,
        "dr": "us"
    },
    "tr": {
        "id": 203,
        "dr": "eu"
    },
    "cr": {
        "id": 49,
        "dr": "us"
    },
    "gu": {
        "id": 83,
        "dr": "us",
        "ldp": "jp"
    },
    "mp": {
        "id": 236,
        "dr": "us",
        "ldp": "jp"
    },
    "pr": {
        "id": 164,
        "dr": "us"
    },
    "vi": {
        "id": 219,
        "dr": "us"
    }
}

def get_gif_url(r):
    h = host[str(r)]
    h = gV.get(h,{}).get("ldp") or gV.get(h,{}).get("dr") or "us"
    return "https://"+h+".thtk.temu.com/c/th.gif"

def get_dr(r):
    h = host[str(r)]

    return gV.get(h,{}).get("dr")


redis_config = {
    "REDIS_HOST": "172.24.16.162",
    "REDIS_PORT": 6379,
    "REDIS_DB": 24,
    "REDIS_PASSWORD": "KNzC8A*md%#7HQTq",
}
cookie_key = "temu_login_cookie"
cookie_len = 30

if __name__ == '__main__':

    print(get_dr(210))
    print(get_gif_url(210))