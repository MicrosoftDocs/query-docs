---
title: "RAND Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RAND Function (DAX)
Returns a random number greater than or equal to 0 and less than 1, evenly distributed. The number that is returned changes each time the cell containing this function is recalculated.  
  
## Syntax  
  
```  
RAND()  
```  
  
## Return Value  
A decimal number.  
  
## Remarks  
In Power Pivot workbooks, recalculation depends on various factors, including whether the workbook is set to **Manual** or **Automatic** recalculation mode, and whether data has been refreshed. This is different from Microsoft Excel, where you can control when RAND generates a new random number by turning off recalculation.  
  
RAND and other volatile functions that do not have fixed values are not always recalculated. For example, execution of a query or filtering will usually not cause such functions to be re-evaluated. However, the results for these functions will be recalculated when the entire column is recalculated. These situations include refresh from an external data source or manual editing of data that causes re-evaluation of formulas that contain these functions.  
  
Moreover, RAND is always recalculated if the function is used in the definition of a measure.  
  
Also, in such contexts the RAND function cannot return a result of zero, to prevent errors such as division by zero.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
To generate a random real number between two other numbers, you can use a formula like the following:  
  
```  
= RAND()*(int1-int2)+int1  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
