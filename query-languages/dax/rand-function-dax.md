---
title: "RAND function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/11/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# RAND
Returns a random number greater than or equal to 0 and less than 1, evenly distributed. The number that is returned changes each time the cell containing this function is recalculated.  
  
## Syntax  
  
```dax
RAND()  
```
  
## Return value

A decimal number.  
  
## Remarks

Recalculation in Power Pivot depends on various factors, including whether the workbook is set to **Manual** or **Automatic** recalculation mode, and whether data has been refreshed. This is different from Microsoft Excel, where you can control when RAND generates a new random number by turning off recalculation.  
  
RAND and other volatile functions that do not have fixed values are not always recalculated. For example, execution of a query or filtering will usually not cause such functions to be re-evaluated. However, the results for these functions will be recalculated when the entire column is recalculated. These situations include refresh from an external data source or manual editing of data that causes re-evaluation of formulas that contain these functions.  
  
RAND is always recalculated if the function is used in the definition of a measure.  
  
RAND function cannot return a result of zero, to prevent errors such as division by zero.  
  
## Examples

To generate a random real number between two other numbers, use:  
  
```dax
= RAND()*(b-a)+a

```

To generate a random number greater than 0 and less than 1:

```dax
= RAND()

```

To generate a random number greater than 0 and less than 100

```dax
= RAND()*100

```

To generate a random whole number greater than 0 and less than 100

```dax
INT(RAND()*100)

```

  
## See also

[Math and Trig functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
