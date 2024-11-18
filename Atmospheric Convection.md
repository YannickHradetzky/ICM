#ICM 

# Atmospheric convection 

Is the vertical movement of air caused by differences in temperature and moisture. Plays a crucial role in redistributing energy vertically. 

## Buoyancy
According to Archimedes principle
$$
b = -\left[ \rho-\frac{\rho_{env}}{\rho} \right]g
$$
Can we rewritten using temperature and the ideal gas law: (Chapter 3.1)[[Skript_ICM.pdf]]
$$
b = \left[ T_{v}-\frac{T_{v,env}}{T_{v,env}} \right]g
$$
"Warm air is lighter and rises due to positive buoyancy"
We have neglected the effect of condensate laoding, which decreases buoyancy

## local instability
Refers to a condition where a small parcel of air, when displaced vertically by an infinitesimal amount, becomes buoyant and continues to rise or fall on its own.


![[Screenshot 2024-10-09 at 14.53.21.png]] 
Figure 3.1) 
- Solid line is the density gradient of the environment
- Dashed line is the dry adiabatic movement of air
- **The Temperature Gradient of the environment needs to be stronger than than the Laps rate in order for it to be stable to ensure the air above is always warmer.**
- Saturated case experiences latent heating and therefore would cool less.
	- Called conditional instability (depends on the moisture)

![[Screenshot 2024-10-09 at 14.59.04.png]]
Figure 3.2) 
- $\Gamma = \frac{dT}{dz} = 0$  Lines of constant temperature
- Inversion : Warm air above me is warmer -> Always lighter

## Potential instability
Also called convective instability. The stability of a layer of air can change if the entire layer is lifted over some distance, instead of an infinitesimal displacement of an air parcel. The lifting of a layer of moist air can transform an initially stable air mass into an unstable or conditionally unstable state.

Potential instability can occur for moist air but not for dry air. Whether there is potential instability depends on the vertical distribution of humidity in the atmosphere.

![[Screenshot 2024-10-09 at 15.16.18.png]]
Figure 3.4) 

### CIN and CAPE
- **CIN** is the negative buoyancy vertically integrated over the near surface atmosphere that presents a barrier to convective motions. 
- **CAPE** is the positive buoyancy vertically integrated further above, roughly speaking in the free troposphere up to the tropopause, and represents the maximum possible energy that can be released (e.g converted into kinetic energy) by the parcel after the CIN barrier has been overcome.
$$
CIN = -\int_{0}^{z_{LFC}}b(z)dz = \int_{0}^{z_{LFC}}\left[\frac{T_{v}-T_{v,env}}{Tv,env} \right]gdz
$$

Can be rewritten into pressure coordinates by means of the **hydrostatic equation** and **ideal gas law**. (Useful for **skew T - lnP diagram** )
- $dp=-\rho gdz$
- $p=\rho R_{d}T_{v,env}$

$$
\begin{align}
dp & =-g\cdot\frac{p}{R_{d}T_{v,env}}dz \\
 -\rho gdz& =-g \cdot \frac{p}{R_{d}T_{v,env}}dz \\
g \frac{dz}{T_{v,env}} & =\frac{R_{d}}{p}dp = -R_{d}d\ln(p)
\end{align}
$$

$$
CIN = R_{d}\int_{P_{sfc}}^{P_{LFC}}\underbrace{ (T_{v}-T_{v,env}) }_{ \approx T-T_{env} }d\ln(p)\approx R_{d}\int_{P_{sfc}}^{P_{LFC}}(T-T_{env})d\ln(p)
$$

For $CAPE$
$$
\begin{align}
CAPE  & = \int_{z_{LFC}}^{Z_{EL}}b(z)dz \\
 & =\int_{z_{LFC}}^{Z_{EL}}\frac{T_{v}-T_{v,env}}{T_{v,env}}gdz \\
 & =R_{d}\int_{z_{LFC}}^{Z_{EL}}(T_{v,env}-T_{v})d\ln(p) \\
 & \approx R_{d}\int_{z_{LFC}}^{Z_{EL}}(T_{env}-T)d\ln(p) & 
\end{align}
$$





![[Screenshot 2024-10-09 at 15.34.50.png]]
Figure 3.5) 
- LCL : Lifting Condensation Level
- LFC : Level of Free Convection 
- EL : Level of equilibrium

So in the area of CIN is the energy that needs to be overcome to become buoyant.
and CAPE is the total amount of energy that is available in the upward motion. 

## What is the fundamental modeling problem in representing convection and turbulence? 
The correlation function on lower scales can not be computed precisely.
Simulation spans a magnitude of 8 on size 
