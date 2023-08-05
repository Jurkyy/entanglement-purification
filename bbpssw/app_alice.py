from bbpssw import bbpssw_protocol_alice
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket

def main(app_config=None):

    # Setup a classical socket to bob
    socket = Socket("alice", "bob", log_config=app_config.log_config)

    # Specify an EPR socket to bob
    epr_socket = EPRSocket("bob")

    alice = NetQASMConnection(
        "alice",
        log_config=app_config.log_config,
        epr_sockets=[epr_socket],
    )
    with alice:
        # Create an entangled pair using the EPR socket to bob
        arr = epr_socket.create(number=2)
        q_ent1, q_ent2 = arr[0], arr[1]
        bbpssw_protocol_alice(q_ent1, q_ent2, alice, socket)
    # Send the outcome to bob
    #socket.send(str(m))
    # Create Alice's context, initialize EPR pairs inside it and call Alice's BBPSSW method. Finally, print out whether or not Alice successfully created an EPR Pair with Bob.

if __name__ == "__main__":
    main()
