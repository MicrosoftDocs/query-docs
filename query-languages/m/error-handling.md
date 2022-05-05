---
description: "Learn more about: Error handling"
title: "Error handling | Microsoft Docs"
ms.date: 4/21/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Error handling

These functions return diagnostic traces at different levels of verbosity, as well as throw error records.
  
## Error  
  
|Function|Description|  
|------------|---------------|  
|[Diagnostics.ActivityId](diagnostics-activityid.md)|Returns an opaque identifier for the currently-running evaluation.|
|[Diagnostics.Trace](diagnostics-trace.md)|Writes a trace message, if tracing is enabled, and returns value.|  
|[Error.Record](error-record.md)|Returns a record containing fields **Reason**, **Message**, and **Detail** set to the provided values. The record can be used to raise or throw an error.|  

## See also

* [Error handling enumerations](error-handling-enumerations.md)
