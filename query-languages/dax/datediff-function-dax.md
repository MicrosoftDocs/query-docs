---
description: "Learn more about: DATEDIFF"
title: "DATEDIFF function (DAX) | Microsoft Docs"
---
# DATEDIFF
  
Returns the number of interval boundaries between two dates.  
  
## Syntax  
  
```dax
DATEDIFF(<Date1>, <Date2>, <Interval>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Date1|A scalar datetime value.|  
|Date2|A scalar datetime value.|  
|Interval|The interval to use when comparing dates. The value can be one of the following:<br /><br />-   SECOND<br />-   MINUTE<br />-   HOUR<br />-   DAY<br />-   WEEK<br />-  MONTH<br />-   QUARTER<br />-   YEAR|  
  
## Return value

The count of interval boundaries between two dates.  
  
## Remarks

A positive result is returned if Date2 is larger than Date1.
A negative result is returned if Date1 is larger than Date2.
  
## Example

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

The following DAX query:

```dax
EVALUATE
VAR StartDate =  DATE ( 2019, 07, 01 )
VAR EndDate =    DATE ( 2021, 12, 31 )
RETURN
    {
        ( "Year",     DATEDIFF ( StartDate, EndDate, YEAR ) ),
        ( "Quarter",  DATEDIFF ( StartDate, EndDate, QUARTER ) ),
        ( "Month",    DATEDIFF ( StartDate, EndDate, MONTH ) ),
        ( "Week",     DATEDIFF ( StartDate, EndDate, WEEK ) ),
        ( "Day",      DATEDIFF ( StartDate, EndDate, DAY ) )
    }   
```

Returns the following:

|Value1  |Value2  |
|---------|---------|
|Year     |   2      |
|Quarter     |    9     |
|Month     |    29     |
|Week    |    130     |
|Day    |      914   |
