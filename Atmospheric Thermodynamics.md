#ICM

# Ideal Gas Law for dry Air 
## Dry Air 
In the Homosphere the content is considered constant and therefore we can come up with an equation of state for dry air with a fixed amount of certain molecules in it. 
### Content : 



### Equation of state 
$$
PV = NRT 
$$

Here $N = \sum_{i=1}^{k}n_{i}$ with a total mass $M=\sum_{i=1}^{k}n_{i}\cdot m_{i}$ 

$$
\frac{PV}{M}=\underbrace{ \frac{N}{M} R/ }_{ R_{d} }T \Leftrightarrow P_{d} = \rho R_{d}T 
$$
Which is the equation of state for dry Air. 


## Moist air
For a mixture of dry air and water vapor the total pressure p is given by 
$$
P = P_{d} + e
$$
$P_{d}=\rho_{d}R_{d}T$  and $e=\rho_{v}R_{v}T$ are the partial pressures of dry air and water vapor. 

### Equation of state
Can be transformed into 
$$
P = \rho R_{d}\underbrace{ \left( \frac{\rho_{d}}{\rho}+\frac{\rho_{v}}{\rho} \frac{R_{v}}{R_{d}} \right) T }_{ T_{v} }
$$
Where $T_{v}$ is called the virtual temperature which includes the density and compositions of the actual air.  It is the temperature that a dry parcel of air would need to have to match the density of the moist parcel, at a given pressure.  $T_{v} \geq T$ because $R_{v}>R_{d}$. $T_{v}=T$ for $\rho_{v}=0$.

Therefore, for the same pressure and temperature moist air is lighter than dry air. 



# Important moisture variables

- water vapor mixing ratio in $\frac{g}{kg}$ : $w = \frac{\rho_{v}}{\rho_{d}}$
- specific humidity in $\frac{g}{kg}$ : $q = \frac{\rho_{v}}{\rho}$
- relative humidity in percent : $RH=\frac{e}{e_{s}}$
	- $e_{s}$ is the maximum amount of water vapor pressure before the water condenses (saturation water pressure)
	- Given by the [https://en.wikipedia.org/wiki/Clausius%E2%80%93Clapeyron_relation](asd)
	



# Thermodynamics 

## First-Law 
$$
\begin{align}
\underbrace{ \delta q }_{ \text{external energy} }  & = \underbrace{ \delta u }_{ \text{change in inner energy} } + p\underbrace{ \delta \alpha }_{ \frac{1}{\rho} } \\
 &= c_{v}dT + pd\alpha \\
 & =c_{p}dT - \alpha dp
\end{align}
$$
$$
\begin{align}
\delta q  & = \delta u+pd\alpha \\
 & =c_{v}dT+pd\alpha \\
d(p\alpha)  & = \alpha dp + pd\alpha = d(RT)= RdT \\
pd\alpha  & = RdT - \alpha dp \\
 \\
\delta q  & = c_{v}dT + pd\alpha = \underbrace{ c_{c}dT + RdT }_{ c_{p}T } - \alpha dp
\end{align}
$$

- Isobaric Process 
- Isochoric Process
- Adiabatic Process


# The many forms of atmospheric temperature

## Potential temperature 
$$
\theta = T\left( \frac{1000\text{hPa}}{p} \right)^{\kappa}
$$
It is conserved under dry adiabatic processes, where dry here means that no water vapor phase change take place (i.e : no condensation, evaporation). $\theta$ is hence a conserved quantity under the condition of dry adiabatic changes, such as the lifting of a clear-air parcel.

$$
\begin{align}
c_{p}dT  & = \alpha dp = \frac{RT}{p}dp \\
 \int_{T_{0}}^{T}c_{p} dT& =\int_{p}^{P_{0}} R \frac{1}{p}dp \\
\ln\left( \frac{T}{T_{0}} \right)  & = \underbrace{ \frac{R}{c_{p}} }_{ \kappa }\ln \left( \frac{P_{0}}{P} \right) \\
\frac{T}{T_{0}}  & = \left( \frac{P_{0}}{P} \right)^{\kappa}  \\
T  & =T_{0} \left( \frac{P_{0}}{P} \right)^{\kappa}
\end{align}
$$
## Equivalent potential temperature

The equivalente potential temperature $\theta_{e}$ is conserved for dry and moist adiabatic motions

$$
\theta_{e}
$$


## Dew-point temperature
The dew-point temperature $T_{d}$ is the temperature to which an air parcel would need to cool to reach a relative humidity of 100% while staying at the same pressure. 

$T_{d}$ is a measure of the vapor content. 


# Lapse rates

$$
\Gamma_{d} = -\frac{dT}{dz} = \frac{g}{c_{p}} \approx \frac{10K}{km}
$$

# Moist lapse rates

$$
\Gamma_{m}=\left[ 1+\frac{L_{v}dq_{s}}{c_{p}dT} \right]^{-1}\Gamma_{d} < \Gamma_{d}
$$



