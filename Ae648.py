import numpy as np
import matplotlib.pyplot as plt

phi0_deg = 48.0
phi0 = np.pi*phi0_deg/180.0

N = 100

phi_arr = (np.pi/180.0)*np.linspace(40, 150, N)
d2pi = np.zeros(N)

P_arr = np.zeros(N)
kv = 1.0
kh = 10.0
L = 1.0

for i in range(N):
    # phi_deg = phi_arr[i]
    phi = phi_arr[i]
    P = 4.0*kh*L*(np.sin(phi) - np.sin(phi0))*np.cos(phi)/np.sin(phi) + kv*L*(np.cos(phi0) - np.cos(phi))
    P_arr[i] = P
    c1 = kv*L*L
    c2 = 4.0*kh*L*L
    sincube = np.sin(phi)*np.sin(phi)*np.sin(phi)
    d2pi[i] = (c1*sincube + c2*(np.sin(phi0)-sincube))/(np.sin(phi))

plt.plot((180.0/np.pi)*phi_arr, P_arr)
plt.xlabel('$\phi$')
plt.ylabel('P')
plt.title('P vs $\phi$')
plt.show()

# plt.plot((180.0/np.pi)*phi_arr, d2pi)
# plt.xlabel('$\phi$')
# plt.ylabel('${\partial}^2 \pi / \partial {\phi}^2$')
# plt.title('${\partial}^2\pi / \partial {\phi}^2$ vs $\phi$')
# plt.show()