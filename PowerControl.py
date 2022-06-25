import relay_lib_seeed as relay

port = 2


if relay.relay_get_port_status(port):
    relay.relay_off(port)
    print('Power off')
else:
    relay.relay_on(port)
    print('Power on')

