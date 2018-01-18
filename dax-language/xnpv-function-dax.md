---
title: "XNPV Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 10df2915-90e8-4951-966e-30e01f45122e
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# XNPV Function (DAX)
> [!NOTE]  
> This function is included in SQL Server 2016 Analysis Services (SSAS), Power Pivot in Excel 2016, and Power BI Desktop only. Information provided here is subject to change.  
  
Returns the present value for a schedule of cash flows that is not necessarily periodic.  
  
## Syntax  
  
```  
XNPV(<table>, <values>, <dates>, <rate>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|A table for which the values and dates expressions should be calculated.|  
|values|An expression that returns the cash flow value for each row of the table.|  
|dates|An expression that returns the cash flow date for each row of the table.|  
|rate|The discount rate to apply to the cash flow for each row of the table.|  
  
## Return Value  
Net present value.  
  
## Remarks  
The value is calculated as the following summation:  
  
![XNPV Formula](../DAX/media/dax-xnpv-formula.jpg "XNPV Formula")  
  
The series of cash flow values must contain at least one positive number and one negative number.  
  
## Example  
The following calculates the present value of the CashFlows table:  
  
```  
Present value := XNPV( CashFlows, [Payment], [Date], 0.09 )  
```  
  
|Date|Payment|  
|--------|-----------|  
|1/1/2014|-10000|  
|3/1/2014|2750|  
|10/30/2014|4250|  
|2/15/2015|3250|  
|4/1/2015|2750|  
  
Present value = 2086.65  
  
