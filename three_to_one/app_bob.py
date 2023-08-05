from three_to_one import three_to_one_protocol_bob
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state

def main(app_config=None):

    # Setup a classical socket to alice
    socket = Socket("bob", "alice", log_config=app_config.log_config)

    # Specify an EPR socket to bob
    epr_socket = EPRSocket("alice")

    bob = NetQASMConnection(
        "bob",
        log_config=app_config.log_config,
        epr_sockets=[epr_socket],
    )
    with bob:
        # Receive an entangled pair using the EPR socket to alice
        arr = epr_socket.recv(number=3)
        q_ent1, q_ent2, q_ent3 = arr[0], arr[1], arr[2]

        temp = three_to_one_protocol_bob(q_ent1, q_ent2, q_ent3, bob, socket)
        bob.flush()

        #print(f"Success: {temp}")

if __name__ == "__main__":
    main()
