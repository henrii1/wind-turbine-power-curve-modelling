# wind-turbine-power-curve-modelling

This repository focuses on obtaining a method for power curve modelling that is more accurate than existing techniques and can be implemented for real time turbine monitoring of wind farms.
data is proprietary hence isn't published in this work.

A novel filteration technique was introduced in this work based on quantiles set on a normal distribution of data

we utilize a novel quantile filtering algorithm, a Radial Basis Function and Multi-layer Perceptron Neural network

Quantile filtering is based on quantiles set on a normal distribution of data that specifies the location of dataset regarded as clean and the region of dataset regarded as outliers.

we also propose an automatic method of fault detection based on the conversion the distance between points in the 2 dimension space into a confidence interval of a clean data.

for the conditions implemented in this work

        @ONLINE{
            Remove outlier
            for x in range(1, 62):
                 if x <= 3:
                    F = 0.95
            elif ((x > 3) and (x <= 10)):
                    F = 0.9
            elif ((x > 10) and (x <= 20)):
                    F = 0.92
            elif ((x > 20) and (x < 30)):
                    F = 0.96
            else:
                    F = 0.985
            d1[x] = outlier_remover(d1[x], 'wind speed', 0.00001, F)
           }

## Filtration results
<p align="center">
  <img src="https://github.com/henrii1/wind-turbine-power-curve-modelling/blob/eb5a4d7af8ef44b901038202c35f975caa722ffc/pics/Screenshot%202022-04-03%20212914.png" | width=275>  
  <img src="https://github.com/henrii1/wind-turbine-power-curve-modelling/blob/eb5a4d7af8ef44b901038202c35f975caa722ffc/pics/wind%203.png" | width=275>  
   </p>
   
## Notebook link
[Here is the main python notebook](https://github.com/henrii1/wind-turbine-power-curve-modelling/blob/main/WIND_TURBINE_POWER_CURVE_MODEL_BINNING_AND_REGRESSION_NN__(2)%20(1).ipynb) that explains all of the stuff step by step!

## ALGORITHM IMPLEMENTED
below is a picture of the model architecture
<p align="centre">
  <img src="https://github.com/henrii1/wind-turbine-power-curve-modelling/blob/eb5a4d7af8ef44b901038202c35f975caa722ffc/pics/algorithm.png" | width=275>
  </p>
  
  ## Citation
  if you use this code for your publicatons, please cite it as:
  
      @ONLINE{hse,
          author = "Henry Emerald"
          title  = "WTPC modelling using quantile filtering and neural netowrks (MLP and RBF)"
          year   = "2022"
          url    = "https://github.com/henrii1/wind-turbine-power-curve-modelling"
      }
      
## Author
Henry Emerald
