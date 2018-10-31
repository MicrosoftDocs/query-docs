---
title: "KEEPFILTERS Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# KEEPFILTERS Function (DAX)
Modifies how filters are applied while evaluating a CALCULATE or CALCULATETABLE function.  
  
## Syntax  
  
```dax
KEEPFILTERS(<expression>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**expression**|Any expression.|  
  
## Return Value  
No return value.  
  
## Remarks  
You use KEEPFILTERS within the context CALCULATE and CALCULATETABLE functions, to override the standard behavior of those functions.  
  
By default, filter arguments s in functions such as CALCULATE are used as the context for evaluating the expression, and as such filter arguments for CALCULATE replace all existing filters over the same columns. The new context effected by the filter argument for CALCULATE affects only existing filters on columns mentioned as part of the filter argument. Filters on columns other than those mentioned in the arguments of CALCULATE or other related functions remain in effect and unaltered.  
  
The KEEPFILTERS function allows you to modify this behavior. When you use KEEPFILTERS, any existing filters in the current context are compared with the columns in the filter arguments, and the intersection of those arguments is used as the context for evaluating the expression. The net effect over any one column is that both sets of arguments apply: both the filter arguments used in CALCULATE and the filters in the arguments of the KEEPFILTER function. In other words, whereas CALCULATE filters replace the current context, KEEPFILTERS adds filters to the current context.  
  
## Example  
The following example takes you through some common scenarios that demonstrate use of the KEEPFILTERS function as part of a CALCULATE or CALCULATETABLE formula.  
  
The first three expressions obtain simple data to be used for comparisons:  
  
-   Internet Sales for the state of Washington.  
  
-   Internet Sales for the states of Washington and Oregon (both states combined).  
  
-   Internet Sales for the state of Washington and the province of British Columbia (both regions combined).  
  
The fourth expression calculates Internet Sales for Washington and Oregon, while the filter for Washington and British Columbia is applied.  
  
The next expression calculates Internet Sales for Washington and Oregon but uses KEEPFILTERS; the filter for Washington and British Columbia is part of the prior context.  
  
```dax
EVALUATE ROW(  
  "$$ in WA"  
    , CALCULATE('Internet Sales'[Internet Total Sales]  
                , 'Geography'[State Province Code]="WA"  
      )  
, "$$ in WA and OR"  
    , CALCULATE('Internet Sales'[Internet Total Sales]  
               , 'Geography'[State Province Code]="WA"   
                 || 'Geography'[State Province Code]="OR"  
      )  
, "$$ in WA and BC"  
    , CALCULATE('Internet Sales'[Internet Total Sales]  
               , 'Geography'[State Province Code]="WA"   
                 || 'Geography'[State Province Code]="BC"  
      )  
, "$$ in WA and OR ??"  
    , CALCULATE(  
          CALCULATE('Internet Sales'[Internet Total Sales]  
                    ,'Geography'[State Province Code]="WA"   
                      || 'Geography'[State Province Code]="OR"  
          )  
          , 'Geography'[State Province Code]="WA"   
            || 'Geography'[State Province Code]="BC"  
      )  
, "$$ in WA !!"  
    , CALCULATE(  
          CALCULATE('Internet Sales'[Internet Total Sales]  
                   , KEEPFILTERS('Geography'[State Province Code]="WA"   
                              || 'Geography'[State Province Code]="OR"  
                     )  
          )  
          , 'Geography'[State Province Code]="WA"   
            || 'Geography'[State Province Code]="BC"  
      )  
)  
```dax
When this expression is evaluated against the sample database AdventureWorks DW Tabular 2012, the following results are obtained.  
  
|Column|Value|  
|----------|---------|  
|[$$ in WA]|$  2,467,248.34|  
|[$$ in WA and OR]|$  3,638,239.88|  
|[$$ in WA and BC]|$  4,422,588.44|  
|[$$ in WA and OR ??]|$  3,638,239.88|  
|[$$ in WA !!]|$  2,467,248.34|  
  
> [!NOTE]  
> The above results were formatted to a table, instead of a single row, for educational purposes.  
  
First, examine the expression, **[$$ in WA and OR ??]**. You might wonder how this formula could return the value for sales in Washington and Oregon, since the outer CALCULATE expression includes a filter for Washington and British Columbia. The answer is that the default behavior of CALCULATE overrides the outer filters in 'Geography'[State Province Code] and substitutes its own filter arguments, because the filters apply to the same column.  
  
Next, examine the expression, **[$$ in WA !!]**. You might wonder how this formula could return the value for sales in Washington and nothing else, since the argument filter includes Oregon and the outer CALCULATE expression includes a filter in Washington and British Columbia. The answer is that KEEPFILTERS modifies the default behavior of CALCULATE and adds an additional filter. Because the intersection of filters is used, now the outer filter **'Geography'[State Province Code]="WA" || 'Geography'[State Province Code]="BC")** is added to the filter argument **'Geography'[State Province Code]="WA" || 'Geography'[State Province Code]="OR"**,. Because both filters apply to the same column, the resulting filter **'Geography'[State Province Code]="WA"** is the filter that is applied when evaluating the expression.  
  
## See Also  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
[CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md)  
[CALCULATETABLE Function &#40;DAX&#41;](calculatetable-function-dax.md)  
  
