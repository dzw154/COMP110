#ord("C#")
#print("C">"A")
#print(chr(129313))
#print("\U0001F6A2")
#age: int = 21
#msg: str = f"You are {age}!"
#print(msg)

# print("\U0001F972")

# print("\U0001F973")

# print("\U0001F974")

# count = 0
# for i in range(4):
#     for j in range(4):
#         count += 1
# print(count)
# print()


# count2 = 0
# for i in range(4):
#     count2 += 1
# print(count2)
# print()

import numpy as np

# Given matrix A
A = np.array([[1, 1],
              [0, 2]])

# 1. Compute A^T A
A_T_A = np.dot(A.T, A)

# 2. Perform SVD on A^T A
U, S, Vt = np.linalg.svd(A_T_A)

# 3. Compute the pseudo-inverse of Sigma
S_plus = np.zeros((A_T_A.shape[0], A_T_A.shape[1])).T
tolerance = max(A_T_A.shape) * np.finfo(float).eps
nonzero_S = S > tolerance
S_plus[nonzero_S] = 1/S[nonzero_S]

# 4. Compute the pseudo-inverse of A^T A
A_T_A_plus = Vt.T @ S_plus @ U.T

# 5. Compute P_c
P_c = A @ A_T_A_plus @ A.T

print("Projection matrix Pc:")
print(P_c)

# 1. Compute A A^T
A_A_T = np.dot(A, A.T)

# 2. Perform SVD on A A^T
U, S, Vt = np.linalg.svd(A_A_T)

# 3. Compute the pseudo-inverse of Sigma
S_plus = np.zeros((A_A_T.shape[0], A_A_T.shape[1])).T
tolerance = max(A_A_T.shape) * np.finfo(float).eps
nonzero_S = S > tolerance
S_plus[nonzero_S] = 1/S[nonzero_S]

# 4. Compute the pseudo-inverse of A A^T
A_A_T_plus = Vt.T @ S_plus @ U.T

# 5. Compute the projection matrix Pr
P_r = A.T @ A_A_T_plus @ A

print("Projection matrix Pr:")
print(P_r)

print(P_c @ A @ P_r)