from three_to_one import three_to_one_protocol_alice
from netqasm.sdk import EPRSocket
import numpy as np
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state

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
        # Create an entangled pair using the EPR socket to bobe
        arr = epr_socket.create(number=3)
        q_ent1, q_ent2, q_ent3 = arr[0], arr[1], arr[2]
        tempnew = three_to_one_protocol_alice(q_ent1, q_ent2, q_ent3, alice, socket)
        alice.flush()

        dm = get_qubit_state(q_ent3, reduced_dm=False)

        # print(f"`Alice` recieved the teleported state {dm}")

        temp = np.array(([1], [0], [0], [1]))
        temp2 = np.array([1, 0, 0, 1])
        fidelity = (1/2) * (temp2 @ (dm @ temp))
        if tempnew:
            sucess = 1
        else:
            sucess = 0
        print(str(sucess) + ' ' + str(fidelity[0].real) + '\n')

        return {'success': tempnew,
                'fidelity': float(str(fidelity[0].real))}



if __name__ == "__main__":
    main()
