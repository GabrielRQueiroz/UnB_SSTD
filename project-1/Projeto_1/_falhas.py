# def interpolator(y, interp_rule):
#     temp_z = np.array(y)
#     values = []
#     average = y.sum() / len(y)

#     for element_index in range(0, len(y)):
#         if interp_rule == "AVERAGE":
#             values.append(average)
#         elif interp_rule == "PREVIOUS":
#             values.append(y[element_index])
#         else:
#             raise ValueError("Invalid interpolation rule")

#     for _ in range(FACTOR - 1):
#         temp_z = np.dstack((temp_z, values))


#     return temp_z.flatten()


# def interpolator(y, interp_rule):
#     temp_z = np.array(y)
#     values = []
#     average = y.sum() / len(y)

#     for element_index in range(0, len(y)):
#         if interp_rule == "AVERAGE":
#             values.append(average)
#         elif interp_rule == "PREVIOUS":
#             values.append(y[element_index])
#         else:
#             raise ValueError("Invalid interpolation rule")

#     for _ in range(FACTOR - 1):
#         temp_z = np.insert(temp_z.astype(np.float32), np.arange(0, len(temp_z)), values)


#     return temp_z

# def interpolator(y, interp_rule):
#     temp_z = np.array(y)
#     values = np.array([])
#     average = y.sum() / len(y)

#     for element_index in range(0, len(y)):
#         if interp_rule == "AVERAGE":
#             values = np.append(values, average)
#         elif interp_rule == "PREVIOUS":
#             values = np.append(values, y[element_index])
#         else:
#             raise ValueError("Invalid interpolation rule")

#     for _ in range(FACTOR - 1):
#         temp_z = np.empty(temp_z.size + values.size)
#         temp_z[0::2] = y
#         temp_z[1::2] = values
        
def interpolator(y, interp_rule):
    upsampled_signal = np.zeros((len(y) * FACTOR))
    for row in range(0, len(y)):
        # upsampled_signal[row][0::FACTOR] = y[row]
        upsampled_signal[row * FACTOR] = y[row]
    average = y.sum() / len(y)
    
    nonzero_indices = np.nonzero(upsampled_signal)[0]
    
    for i in range(1, FACTOR):
        if interp_rule == "AVERAGE":
            upsampled_signal[i::FACTOR] = average
        elif interp_rule == "PREVIOUS":
            upsampled_signal[i::FACTOR] = upsampled_signal[nonzero_indices]
                    
    return upsampled_signal