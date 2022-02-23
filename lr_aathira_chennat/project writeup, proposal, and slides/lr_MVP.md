---
typora-copy-images-to: ./features_pairplt.png
---

# Minimum Viable Product 

## Linear Regression Project- Aathira Chennat

---

* **Goal:**

  This project seeks to estimate the total US box office earnings for a film based on its characteristics, including genre, production company, and running time.

* **Process:**
  * Using data provided by thenumbers.com, I compiled a dataset of all films screened in the US during the years 2017, 2018, 2019. 
    * The target is inflation adjusted total box office. The dataset contains 1418 observations (films)-- i removed films that had missing values for categorical features of interest.
    * Continuous Features: 
      * running time, max theater count, legs (share of the box office during its biggest weekend in theaters), average run in theaters (in weeks), annual rank, opening weekend box office,
    * Categorical Features:
      * distribution company,  director, lead actor,  genre, mpaa rating, movie name, if the movie is part of a franchise, movie source (original screenplay, remake, based on a comic or book), production method (animation, live action, hybrid)
    * Datetime Features:
      * Release date
  * After creating binary dummy variables for the top 5 categories for genre, movie source, production method, and distribution company, I include these and all continuous variables with correlations with the target of less than 0.5 into my simple regression.

* **Preliminary visualizations:**

  Heat Map

  ![features_heatmap](/Users/aathirachennat/Desktop/Metis/Module_2/lr_project/features_heatmap.png)![](/Users/aathirachennat/Desktop/Metis/Module_2/lr_project/features_pairplt.png)

  * I'm having some issues with formatting in seaborn, apologies.

  Regressions: standard regression, ridge regression

  ![lr_prelim_reg1](/Users/aathirachennat/Desktop/Metis/Module_2/lr_project/lr_prelim_reg1.png)

  ![lr_prelim_reg2](/Users/aathirachennat/Desktop/Metis/Module_2/lr_project/lr_prelim_reg2.png)

* **Preliminary conclusions:**

  Looks like this model is on the right track.

  Going forwatd, I can eliminate a lot of features from the regression, including: DV for genres, sources and continous variables like legs and domestic share.

  I'm curious to see how the model performs when I transform the target to log(Y)-- some of the correlations in the paiplot seemed to be non/linear asymptotic. I plan to cross-validate the simple model (with less features), log(y), and a ridge regression.

  