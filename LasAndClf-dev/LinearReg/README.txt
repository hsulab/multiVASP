!Scripts...
DataOperators.py
    Get the DataSet - CH4_DataSet.csv.
    pkload(pk)
    pkdump(pk, ret)

LinearMethods.py
    Create LeasrSqure, Lasso, Ridge Models with GridSearch.
    --> Dump the lsr.pk, las.pk, rid.pk, which is the GS process.

PreSelection.py
    Pickle the LinearMethods results.
    --> Dump the BestLas.pk, BestRid.pk

FeaSelection.py
    Choose the best combination of features.


LearningCurve.py
    Plot the learning curve of LinearMethods.

Charts.py
    Plot the Bar Chart of the features of the best combination.

!Log...
GsLas.pk --> gs_las
    The Lasso GridSearch Model.

BestLas.pk --> (params, fc_dict)
    params --> Best Lasso Model Parameters by GsLas
    fc_dict --> The features {name:coef} from GsLas

BestReg.pk -->
    bestreg_pk = (len(feas.keys()), best_feas, mean_MSEs, std_MSEs)
    fea.keys() --> features' name from Lasso
    best_feas --> feature combination with smallest test MSE
    mean_MSEs -->
    std_MSEs -->
    The feature selection model, my code


