from dejmps import dejmps_protocol_alice
from netqasm.sdk import EPRSocket
import numpy as np
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state

def format(value):
    return "%.4f" % value

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
        q_ent1 = epr_socket.create()[0]
        q_ent2 = epr_socket.create()[0]
        tempnew = dejmps_protocol_alice(q_ent1, q_ent2, alice, socket)
        alice.flush()
        dm = get_qubit_state(q_ent1, reduced_dm=False)
        temp = np.array(([1], [0], [0], [1]))
        temp2 = np.array([1, 0, 0, 1])
        fidelity = (1/2) * (temp2 @ (dm @ temp))
        if tempnew:
            sucess = 1
        else:
            sucess = 0
        print(str(sucess) + ' ' + format(fidelity[0].real))
        return {
            'success': tempnew,
            'fidelity' : float(str(fidelity[0].real))}



if __name__ == "__main__":
    main()
