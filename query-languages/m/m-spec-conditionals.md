---
title: M Language Conditionals 
description: Describes using conditionals in the Power Query M formula language
ms.topic: conceptual
ms.date: 8/2/2022
---


# Conditionals

The _if-expression_ selects from two expressions based on the value of a logical input value and evaluates only the selected expression.

_if-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `if`  _if-condition_  `then`  _true-expression_  `else`  _false-expression<br/>
if-condition:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
true-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
false-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_

The following are examples of _if-expressions_:

```powerquery-m
if 2 > 1 then 2 else 1          // 2
if 1 = 1 then "yes" else "no"   // "yes"
```

The following holds when evaluating an _if-expression_:

* If the value produced by evaluating the _if-condition_ is not a logical value, then an error with reason code `"Expression.Error"` is raised.

* The _true-expression_ is only evaluated if the _if-condition_ evaluates to the value `true`.

* The _false-expression_ is only evaluated if the _if-condition_ evaluates to the value `false`.

* The result of the _if-expression_ is the value of the _true-expression_ if the _if-condition_ is `true`, and the value of the _false-expression_ if the _if-condition_ is `false`.

* Errors raised during the evaluation of the _if-condition_, _true-expression_, or _falseexpression_ are propagated.
