Overview
-------------------------------

In this repository, we aim to numerically solve the minimization problem
$$
\min _{x \in K} J(x)
$$

where

$$
\begin{gathered}
J(u)=\int_{0}^{1}\left(\frac{1}{2} u^{\prime}(x)^{2}-f(x) u(x)\right) d x \\
K=\left\{u \in H^{1}(] 0,1[): u(0)=u(1)=0, u(x) \geq g(x), \forall x \in[0,1]\right\}
\end{gathered}
$$
Here, $f$ and $g$ are two given functions. We will construct another function from $K$ to $I R$, denoted as $\mathrm{J}_{\mathrm{n}}$. Subsequently, a numerical study is conducted on $\mathrm{J}_{\mathrm{n}}$, including the development of algorithms to compute the minimum of this new function.