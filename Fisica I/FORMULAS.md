## Óptica Geométrica

**Convergente** $\to$ ***Focos Reales

$P:$ Potencia $P = \frac{1}{f_o}$

### **Planos:**

**Reflexión**:

$\theta_i = \theta_r$

**Refracción**:

$n_i\sin\theta_i = n_r\sin\theta_r\\

\sin\theta_{crit} = \frac{n_r}{n_i}$

**Prisma**

$i = r'\\r = i'$

$\delta_{min} = 2i -\varphi\\

r = \frac{\varphi}{2}$

### **Esféricos:**

**Espejos**

$\text{General: }\quad \frac 1{x_o} + \frac 1{x_i} = \frac 2R = \frac 1{f_o}$

$\text{Aumento: }\quad A = -\frac{x_i}{x_o}$

$\text{Focos: }$

$f = \frac R2 \\

f_o:(x_i\to\infty) \\

f_i:(x_o\to\infty)$

**Dioptras**

$\text{General: }\quad\frac {n_1}{x_o} - \frac {n_2}{x_i} = \frac{n_1 - n_2}{R}$

$\text{Aumento: }\quad A = \frac{n_1\cdot x_i}{n_2\cdot x_o}$

$\text{Focos:}$

$f_o:(x_i\to\infty) = \frac {n_1\cdot R}{n_1 - n_2}$

$f_i:(x_o\to\infty) = \frac {n_2\cdot R}{n_2 - n_1}$

### **Lentes**

$\text{General: }\quad\frac 1{x_o} - \frac 1{x_i} = \frac{n_L - n_M}{n_M}\bigg(\frac1{R_2}-\frac1{R_1}\bigg)=\frac1{f_o}$

$\text{Aumento: }\quad A = \frac{x_i}{x_o}$

$\text{Focos:}$

$f_o:(x_i\to\infty) = \frac {n_M}{n_L-n_M}\bigg(\frac{R_1\cdot R_2}{R_1-R_2}\bigg)$

$f_i:(x_o\to\infty) = \frac {n_M}{n_M-n_L}\bigg(\frac{R_1\cdot R_2}{R_1-R_2}\bigg) = -f_o$

## Ondas Mecanicas

$$
\boxed{\xi(x,t) = A\cdot\sin(kx \pm wt + \varphi)}
$$

Velocidad de Propagación $\displaystyle\to v= \frac\lambda T=\frac wk$

Longitud de Onda $\displaystyle\to\lambda = \frac vf$

Número de Onda ***$\displaystyle\to k =\frac{2\pi}\lambda$

Frecuencia ***$\displaystyle\to f= \frac 1T=\frac w{2\pi}$

**Velocidad**

Cuerdas: $v = \sqrt\frac F\mu$

Gases $v = \sqrt{\frac{\gamma RT}{M}} = \sqrt{\frac{B}{\delta}}$

Solidos (Transversales): $v = \sqrt\frac G\rho$

Solidos (Longitudinales) $v = \sqrt\frac Y\rho$, $Y = \frac{\frac FA}{\frac{\Delta l}L}$

### **Energía**

$⟨P⟩ =\frac 12\cdot\mu\cdot v\cdot w^2\cdot A^2$

$⟨dE_c⟩ = \frac 14\rho\cdot A^2\cdot w^2$

$⟨I⟩ = \frac 12\cdot\rho\cdot v\cdot w^2\cdot A^2$

$⟨dE_{Pel}⟩ = \frac 14\rho\cdot A^2\cdot w^2$

### **Sonido**

**Presión**

$p(x,t) = p_o\sin(kx - wt - \frac\pi 2)$

$p_o = \rho\cdot w\cdot v\cdot A$

**Decibeles**

$db = 10\log\frac{I}{I_o}\implies I_o = 10^{-12}\cdot\frac {\text{W}}{m^2}$

**Doppler**

$v'_p = v_p - v_r$

$f' = f\cdot\bigg(\frac{v_p - v_r}{v_p - v_f}\bigg)$

$\lambda' = \frac{v_p - v_f}{f}$

### **Ondas Estacionarias**

$$
\xi_1 = A\cdot\sin(kx-\omega t)\\
\xi_2 = A\cdot\sin(kx+\omega t)
$$

$$
\xi_{\text{tot}} = 2A\cdot\sin(kx)\cdot\cos(\omega t)
$$

**Extremos Iguales**

$f_n = n\frac v{2L}$

$\lambda_n = \frac{2L}{n}$

$n=1,2,3,...$

**Extremos Distintos**

$f_n = (2n-1)\frac v{4L}$

$\lambda_n = \frac{4L}{2n-1}$

$n=1,2,3,...$

### **Batidos**

$\xi_1 = A\cdot\sin(kx-\omega_1 t+\varphi_1)$

$xi_2 = A\cdot\sin(kx-\omega_2 t+\varphi_2)$

$\xi_{\text{tot}} = 2A \cdot \cos\bigg(\frac{\Delta k}2x -\frac{\Delta\omega}2t+\frac{\Delta\varphi}2\bigg) \cdot \cos\bigg(k_px-w_pt+\varphi_p\bigg)$

$omega_\text{Onda Moduladora} = \frac{w_2-w_1}2$

$f_\text{Onda Moduladora} = \frac{f_2-f_1}2$

$f_\text{Pulso} = \big|f_2-f_1\big|$

## Óptica Física

### **Interferencia**

$\xi_1(x,t) = A_1\sin(kx_1-wt+\varphi_1)\\\xi_2(x,t) = A_2\sin(kx_2-wt+\varphi_2)$

$\xi(x,t) = 2A \cdot \cos\bigg[kx_p - wt +\varphi_p\bigg] \cdot \cos\bigg[\frac{k\cdot\Delta x}{2}+\frac{\Delta\varphi}{2}\bigg]$

Diferencia de Fase $\implies\Delta = k\Delta x + \Delta\varphi \to[rad]$

Aproximación $\implies\sin\theta \approx \tan\theta = \frac{y}{D}$

**Young:**

$d\sin\theta = n\cdot\lambda$

$y_{max} = n\cdot\frac{\lambda\cdot D}d$

$n=0,1,2,\cdots$

$d\sin\theta = \frac{(2n+1)}{2}\cdot\lambda$

$y_{min} = \frac{2n-1}2\cdot\frac{\lambda\cdot D}d$

$n=1,2,3,\cdots$

**Intensidad:**

$I = 4I_0\cdot \cos^2\bigg(\frac\delta2\bigg)$

$N$ **Rendijas**

$d\sin\theta = n\cdot\lambda$

$y_{max} = n\cdot\frac{\lambda\cdot D}d$

$n=0,1,2,\cdots$

$d\sin\theta = \frac{n}{N}\cdot\lambda$

$y_{min} = \frac nN\cdot\frac{\lambda\cdot D}d$

$n=1,2,3,\cdots$ No Múltiplo de $N$:

**Amplitud**

$A = A_0\frac{\sin\Big(\frac{N\cdot k\cdot\Delta x}2\Big)} {\sin\Big(\frac{ k\cdot\Delta x}2\Big)}$

**Intensidad**

$I = I_0\frac{\sin^2\Big(\frac{N\cdot k\cdot\Delta x}2\Big)}{\sin^2\Big(\frac{k\cdot\Delta x}2\Big)}$

$I_{max} = N^2\cdot I_0$

### **Difracción**

**Una Rendija**

$a\cdot\sin\theta = n\lambda$

$y_{min} = n\cdot\lambda\frac Da$

$n=1,2,3,\cdots$

**Intensidad**

$\beta = \frac{a\pi\sin\theta}\lambda = \frac{ak\sin\theta}2$

$I = I_0\frac{\sin^2\beta}{\beta^2}$

### **Red De Difracción**

Constate de Red $C = \frac 1d$

**Interferencia**

$d\sin\theta = m\cdot\lambda$

$y_{max} = m\cdot\frac{\lambda D}{d}$

$m=0,1,2,\cdots$

$d\sin\theta = \frac mN\cdot\lambda$

$y_{min} = \frac mN\cdot\frac {\lambda D}d$

$m=1,2,3,\cdots$

**Difracción**

$b\sin\theta = n\lambda$

$y_{min} = n\cdot\lambda\cdot\frac{D}{a}$

$n=1,2,3,\cdots$

**Relación $a,d$. (Coincidencia de máximo de interferencia con mínimo de difracción)**

$\frac da = \frac mn \to y_{max_m},y_n\text{ coinciden}$

**Intensidad**

$\beta = \frac{a\pi\cdot\sin\theta}\lambda = \frac{ak\cdot\sin\theta}2$

$I = I_0\cdot \frac{\sin^2\beta}{\beta^2}\cdot \frac{\sin^2(N\cdot\gamma)}{\sin^2\gamma}$

$\gamma= \frac{\delta}2 = \frac{dk\cdot\sin\theta}2$

$I_{max} = N^2\cdot I_0$

### **Unidades**

$cm = 10^{-2}m$

$mm = 10^{-3}m$

$Pa: \text{Pascales}$

$\mu m = 10^{-6}m$

$nm = 10^{-9}m$

$1 atm = 101325 Pa = 1013,25hPa$
