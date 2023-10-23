---
description: "Learn more about: UTCNOW"
title: "UTCNOW function (DAX) | Microsoft Docs"
---
# UTCNOW

Returns the current UTC date and time.
  
## Syntax  
  
```dax
UTCNOW()  
```
  
## Return value

A (**datetime)**.  
  
## Remarks  

The result of the UTCNOW function changes only when the formula is refreshed. It is not continuously updated. 
  
## Example

The following:
  
```dax
EVALUATE { FORMAT(UTCNOW(), "General Date") }
```

Returns:

|[Value]  |
|---------|
|2/2/2018 4:48:08 AM    |

## See also

[NOW function](now-function-dax.md)  
[UTCTODAY function](utctoday-function-dax.md)  
