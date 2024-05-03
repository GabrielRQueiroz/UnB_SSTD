### OLD ANALYTICAL SOLUTION FUNCTION
    # roots = np.roots([a_0, a_1, a_2])
    # y_c = 0

    # if np.iscomplexobj(roots):
    #     quoeficient_matrix = np.array(
    #         [
    #             np.abs(roots) ** i * np.exp(1j * np.angle(roots) * i)
    #             for i in range(1, len(roots) + 1)
    #         ]
    #     )
    #     results = np.array([impulse_response_recursive_solution(i) for i in range(1, len(roots) + 1)])
    # else:
    #     quoeficient_matrix = np.array([roots**i for i in range(len(roots))])
    #     results = np.array([impulse_response_recursive_solution(i) for i in range(len(roots))])

    # autovalues = np.linalg.solve(quoeficient_matrix, results)

    # for i in range(len(roots)):

    #     y_c += autovalues[i] * roots[i] ** n

    # return (b_2 / a_2) * impulse(n) + step(n) * y_c
