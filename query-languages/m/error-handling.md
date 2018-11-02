---
title: "Error handling | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Error handling
 
  
## <a name="__toc360789892"></a>Error  
  
|Function|Description|  
|------------|---------------|  
|[Diagnostics.ActivityId](diagnostics-activityid.md)|Returns an opaque identifier for the currently-running evaluation.|
|[Diagnostics.Trace](diagnostics-trace.md)|Writes a trace message, if tracing is enabled, and returns value.|  
|[Error.Record](error-record.md)|Returns a record containing fields “Reason”, “Message”, and “Detail” set to the provided values. The record can be used to raise or throw an error.|  
|[TraceLevel.Critical](tracelevel-critical.md)|Returns 1, the value for Critical trace level.|  
|[TraceLevel.Error](tracelevel-error.md)|Returns 2, the value for Error trace level.|
|[TraceLevel.Information](tracelevel-information.md)|Returns 4, the value for Information trace level.|
|[TraceLevel.Verbose](tracelevel-verbose.md)|Returns 5, the value for Verbose trace level.|
|[TraceLevel.Warning](tracelevel-warning.md)|Returns 3, the value for Warning trace level.|