### Euler-Lagrange Equation
Let $x \in ]0,1[$. We know that the Euler-Lagrange equation for this minimization problem is given by:
$$
\begin{aligned}
&\frac{ \partial }{\partial x}\left(\frac{\partial L}{\partial u^{\prime}}\right)-\frac{\partial L}{\partial u}=0, \text { avec } \mathrm{L}(\mathrm{u})=\frac{1}{2} u^{\prime}(x)^{2}-f(x) u(x) \\
&\Rightarrow \frac{ \partial }{\partial x}\left(u^{\prime}(x)\right)+f(x)=0 \\
&\Rightarrow u^{\prime \prime}(x)+f(x)=0 \\
&\Rightarrow u^{\prime \prime}(x)=-f(x)
\end{aligned}
$$
Hence the result:
$$
\left.-u^{\prime \prime}(x)=f(x), \forall x \in\right] 0,1[
$$




Let $x \in ]0,1[$. According to the above, we have: $-u^{\prime\prime}(x)=f(x)$
$$
\begin{aligned}
&\Rightarrow-u^{\prime \prime}(x)=1 \\
&\Rightarrow \mathrm{u}(\mathrm{x})=-\frac{1}{2} \mathrm{x}^{2}+\mathrm{bx}+\mathrm{c}
\end{aligned}
$$
Considering the boundary conditions, we get:
$$
\begin{gathered}
\mathrm{u}(0)=0 \rightarrow \mathrm{c}=0 \\
\mathrm{u}(1)=0 \rightarrow-\frac{1}{2}+\mathrm{b}=0 \rightarrow \mathrm{b}=\frac{1}{2}
\end{gathered}
$$
So the solution to this differential equation is: 
$$
\left.u(x)=-\frac{1}{2} x(x-1), \forall x \in\right ]0,1[
$$

Let $x \in [0,1]$. We then have: $\quad J(u)=\int_{0}^{1}\left(\frac{1}{2} u^{\prime}(x)^{2}-f(x) u(x)\right) d x$,
$$
\begin{aligned}
\rightarrow & J(u)=\int_{0}^{1}\left(\frac{1}{2}\left(\sum_{i=1}^{n} u_{i} \Phi_{i}^{\prime}(x)\right)^{2}-\sum_{i=1}^{n} f(x) u_{i} \Phi_{i}(x)\right) d x \\
\rightarrow & J(u)=\int_{0}^{1} \frac{1}{2}\left(\sum_{i=1}^{n} u_{i} \Phi_{i}^{\prime}(x)\right)^{2} d x-\int_{0}^{1} \sum_{i=1}^{n} f(x) u_{i} \Phi_{i}(x) d x \\
\rightarrow & J(u)=\sum_{k=0}^{n} \int_{x_{k}}^{x_{k+1}} \frac{1}{2}\left(\sum_{i=1}^{n} u_{i} \Phi_{i}^{\prime}(x)\right)^{2} d x-\sum_{k=0}^{n} \int_{x_{k}}^{x_{k+1}} \sum_{i=1}^{n} f(x) u_{i} \Phi_{i}(x) d x \\
\rightarrow & J(u)=\sum_{k=0}^{n} \int_{x_{k}}^{x_{k+1}} \frac{1}{2} \sum_{i=1}^{n} u_{i}^{2} \Phi_{i}^{\prime}(x)^{2} d x+\sum_{k=0}^{n} \int_{x_{k}}^{x_{k+1}}\left(\sum_{i=1}^{n} \sum_{j=i+1}^{n} u_{i} \Phi_{i}^{\prime}(x) u_{j} \Phi_{j}^{\prime}(x)\right) d x- \sum_{0 \leq i, k \leq n} \int_{x_{k}}^{x_{k+1}} f(x) u_{i} \Phi_{i}(x) d x \\
\rightarrow & J(u)=\frac{1}{2} \sum_{0 \leq i, k \leq n} \int_{x_{k}}^{x_{k+1}} u_{i}^{2} \Phi_{i}^{\prime}(x)^{2} d x+\sum_{k=0}^{n} \sum_{i=1}^{n} \sum_{j=i+1}^{n} \int_{x_{k}}^{x_{k+1}} u_{i} \Phi_{i}^{\prime}(x) u_{j} \Phi_{j}^{\prime}(x) d x- \sum_{0 \leq i, k \leq n} \int_{x_{k}}^{x_{k+1}} f(x) u_{i} \Phi_{i}(x) d x
\end{aligned}
$$ 

The value of the function $\Phi_{i}^{\prime}(x)$ depends on the interval. In our case, if $\mathrm{k} \notin [i-1, i+1]$, then $\Phi_{i}^{\prime}(x)$ takes the value 0. Otherwise, the function $\Phi_{i}^{\prime}(x)$ takes two values, either $\frac{1}{h}$ or $-\frac{1}{h}$. Thus, the previous sum becomes:
$$
\begin{aligned}
\rightarrow & J(u)=\frac{1}{2} \sum_{1 \leq i \leq n} u_{i}^{2} \frac{2}{h}+\frac{1}{2} \sum_{k=0}^{n} \sum_{i=1}^{n} \sum_{j=i+1}^{n} u_{i} u_{j} \int_{x_{k}}^{x_{k+1}} \Phi_{i}^{\prime}(x) \Phi_{j}^{\prime}(x) d x- \sum_{0 \leq i, k \leq n} u_{i} \int_{x_{k}}^{x_{k+1}} f(x) \Phi_{i}(x) d x \\
\rightarrow & J(u)=\frac{1}{h} \sum_{1 \leq i \leq n} u_{i}^{2}+\sum_{1 \leq i \leq n} u_{i} u_{i-1} \int_{x_{i-1}}^{x_{i}}-\left(\frac{1}{h}\right)^{2} d x- \sum_{0 \leq i, k \leq n} u_{i}\left(x_{k+1}-x_{k}\right) \frac{f\left(x_{k+1}\right) \Phi_{i}\left(x_{k+1}\right)+f\left(x_{k}\right) \Phi_{i}\left(x_{k}\right)}{2} \\
\rightarrow & J(u)=\frac{1}{h} \sum_{1 \leq i \leq n} u_{i}^{2}-\frac{1}{h} \sum_{1 \leq i \leq n} u_{i} u_{i-1}-\sum_{1 \leq i \leq n} u_{i} h \frac{2 f\left(x_{i}\right)}{2} \\
\rightarrow & J(u)=\frac{1}{h} \sum_{1 \leq i \leq n} u_{i}^{2}-\frac{1}{h} \sum_{1 \leq i \leq n} u_{i} u_{i-1}-\sum_{1 \leq i \leq n} u_{i} h f\left(x_{i}\right) \\
\rightarrow & J(u)=h\left(\frac{1}{2 h^{2}}\left(2 \sum_{1 \leq i \leq n} u_{i}^{2}-2 \sum_{1 \leq i \leq n} u_{i} u_{i-1}\right)-\sum_{1 \leq i \leq n} u_{i} f\left(x_{i}\right)\right) \\
\rightarrow & J(u)=h\left(\frac{1}{2}\langle A u, u\rangle-\langle b, u\rangle\right)=h J_{n}(u)
\end{aligned}
$$
with : $\mathrm{A}=\frac{1}{h^{2}}\left(\begin{array}{ccccc}2 & -1 & 0 & \cdots & 0 \\ -1 & 2 & -1 & \ddots & \vdots \\ 0 & \ddots & \ddots & \ddots & 0 \\ \vdots & \ddots & -1 & 2 & -1 \\ 0 & \cdots & 0 & -1 & 2\end{array}\right), \quad \mathrm{u}=\left(\begin{array}{c}u_{1} \\ \vdots \\ \vdots \\ \vdots \\ u_{n}\end{array}\right), \quad \mathrm{b}=\left(\begin{array}{c}f\left(x_{1}\right) \\ \vdots \\ \vdots \\ \vdots \\ f\left(x_{n}\right)\end{array}\right)$

 The minimization problem can be approximated by the quadratic minimization problem in
    $\begin{aligned}    \mathbb{R}^n \end{aligned}$.


In order to demonstrate that problem (3) has a unique solution, it is necessary to show that the objective function, $J_{n}$, is both coercive and strictly convex, and that the space $K^{n}$ is closed and convex.
* **Show that $J_{n}$ is strictly convex:** 
  
  The matrix $A$ is a symmetric positive definite matrix, as per the previous lab session. Therefore, for all $x \in \mathbb{R}^{n} \backslash{0, \ldots, 0}^{T}$, $\langle A x \mid x\rangle > 0$. So, for any two different vectors $x$ and $y$ in $\mathbb{R}^{n}$ (i.e., $x-y \neq 0$), we have: $\quad\langle A(x-y) \mid x-y\rangle>0$
  $$
    \begin{aligned}
    &\rightarrow\langle A x-b-(A y-b) \mid x-y\rangle>0 \\
    &\Rightarrow\left\langle\nabla J_{n}(x)-\nabla J_{n}(y) \mid x-y\right\rangle>0
    \end{aligned}
  $$
  Therefore, according to the characterization of differentiable convex functions, and since the function $J_{n}$ is differentiable at every vector $x$ in $\mathbb{R}^{n}$ with its gradient being $\nabla J_{n}(x)=A x-b$, the function $J_{n}$ is strictly convex (1).

* **Show that $J_{n}$ is coercive:**
   
    The matrix $\mathrm{A}$ is symmetric, so it is diagonalizable according to the spectral theorem. In this case, we have: $\lambda_{\min }|x|{2}^{2} \leq\langle A x \mid x\rangle \leq \lambda{\max }|x|_{2}^{2}, \forall x \in \mathbb{R}^{n}$. Additionally, according to the Cauchy-Schwarz inequality, $\langle b \mid x\rangle \leq|\langle b \mid x\rangle| \leq|b| \times|x|$.
    $$
    \Rightarrow-\langle b \mid x\rangle \geq-\|b\| \times\|x\|
    $$
    Therefore, we have: $\frac{\lambda_{\min }}{2}|x|_{2}^{2}-|b| \times|x| \leq \frac{1}{2}\langle A x \mid x\rangle-\langle b \mid x\rangle$

And since matrix A is positive definite, all eigenvalues are strictly positive, hence we have:  $J_{n}(x) \geq\|x\|\left(\frac{\lambda_{\min }}{2}\|x\|_{2}-\|b\|\right)$

As $\lim _{\|x\| \rightarrow+\infty}\|x\|\left(\frac{\lambda_{\min }}{2}\|x\|_{2}-\|b\|\right)=+\infty$, we then have $\lim _{\|x\| \rightarrow+\infty} J_{n}(x)=+\infty$ and consequently, the function $J_{n}$ is coercive (2)
- **Show that K^{n} is closed:**
  Since the function $k: x \rightarrow x-g(x)$ is continuous, and $g$ is continuous, the set $K^{n}$ is expressed as $K^{n}=\left\{v \in I R^{n}: k\left(v_{i}\right) \geq 0 \forall 1 \leq i \leq n\right\}$, which is indeed a closed subset of $\mathbb{R}^{n}$. (3)

- **Show that $K^{n}$ is convex:**
  Let $v$ and $w$ be two vectors in $K^{n}$, and let $t \in [0,1]$. We have $v_{i} \geq g\left(x_{i}\right)$ and $w_{i} \geq g\left(x_{i}\right)$:
  $$
  \begin{aligned}
  &\Rightarrow (1-t) v_{i} \geq (1-t) g\left(x_{i}\right) \text { and } t w_{i} \geq t g\left(x_{i}\right) \\
  &\Rightarrow (1-t) v_{i} + t w_{i} \geq g\left(x_{i}\right)
  \end{aligned}
  $$
  Thus, $(1-t) v_{i} + t w_{i} \in K^{n}$, and consequently, $K^{n}$ is convex (4).

  With conditions (1), (2), (3), and (4) satisfied, the minimization problem (3) has a unique solution.


 