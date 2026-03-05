---
title: "Use DAX user-defined functions (preview)"
description: Best practices for using DAX user-defined functions.
author: hsteffens30
ms.author: jterh
ms.topic: best-practice
ms.date: 09/15/2025
ms.service: powerbi
ms.subservice: dax
---

# DAX user-defined functions (preview)

> [!NOTE]
> DAX user-defined functions are currently in **preview**.

DAX user-defined functions (UDFs) let you package DAX logic and reuse it like any other DAX function. UDFs introduce a new `FUNCTION` keyword, optional [parameters](#parameters) (scalar, table, and references), and [type checking](#type-checking) helpers that make authoring safer and clearer. After you [define a UDF](#define-and-manage-user-defined-functions), you can use it in a [measure](#calling-a-udf-in-a-measure), [calculated column](#calling-a-udf-in-a-calculated-column), [visual calculation](#calling-a-udf-in-a-visual-calculation), or even other [user-defined functions](#calling-a-udf-in-another-udf). Users can centralize business rules, improve maintainability, and evolve calculations safely over time. Functions are first-class model objects you can create and manage in [DAX query view](/power-bi/transform-model/dax-query-view) and [TMDL view](/power-bi/transform-model/desktop-tmdl-view), and they can be viewed in [Model explorer](/power-bi/transform-model/model-explorer) under the *Functions* node.


## Enable user-defined functions

To try UDFs in Desktop:
1. Go to **File > Options and settings > Options**.
2. Select **Preview features** and check **DAX user-defined functions**.
3. Select **OK** and **restart** Power BI Desktop.


## Define and manage user-defined functions

There are several locations to define and manage functions:
- [DAX query view](#using-dax-query-view) (DQV). Define and modify functions in DQV. DQV also includes context-menu **Quick queries** (Evaluate, Define and evaluate, and Define all functions in this model) to help you test and manage UDFs fast.
- [TMDL view](#using-tmdl-view). UDFs can also be authored and edited in TMDL. TMDL view also includes context-menu **Script TMDL to**.
- [Model explorer](#using-model-explorer). Existing functions can be viewed under the *Functions* node in Model explorer.

When defining a UDF, please follow these naming requirements:

**Function names**:
- Must be well-formed and unique within the model.
- Can include periods (dots) for namespacing (e.g. Microsoft.PowerBI.MyFunc). Cannot start or end with a period or have consecutive periods.
- Other than periods, names can only contain alphanumeric characters or underscores. No spaces or special characters allowed.
- Must not conflict with built-in DAX functions or reserved words (e.g. measure, function, define).

**Parameter names**:
- Can only contain alphanumeric characters or underscores. Periods are not allowed.
- Must not be a reserved word.


### Using DAX query view

You can define, update, and evaluate user-defined functions in DAX query view. For additional information on DAX query view, see [DAX query view](/power-bi/transform-model/dax-query-view).


#### General form

```dax
DEFINE
    /// Optional description above the function
    FUNCTION <FunctionName> = ( [ParameterName]: [ParameterType], ... ) => <FunctionBody>
```

> [!TIP]
> Use `///` for function descriptions. Single-line (`//`) or multi-line (`/* */`) comments will not appear in IntelliSense function descriptions.


#### Example: Simple tax function

```dax
DEFINE
    /// AddTax takes in amount and returns amount including tax
    FUNCTION AddTax = 
        ( amount : NUMERIC ) =>
            amount * 1.1

EVALUATE
{ AddTax ( 10 ) }
// Returns 11
```


#### Saving to the model

To save a UDF from DAX query view to the model:
- Click **Update model with changes** to save all UDFs in the query.
- Or click **Update model: Add new function** above the defined function to save a single UDF.

:::image type="content" source="media/dax-user-defined-functions/dax-query-view-save-to-model.png" alt-text="Screenshot of DAX query view in Power BI Desktop, highlighting two locations where you can save a user-defined function. The first is the Update model with changes button at the top of the view. The second is a status line in the code editor labeled Update model: Add new function" lightbox="media/dax-user-defined-functions/dax-query-view-save-to-model.png":::


### Using TMDL view

You can define and/or update user-defined functions in TMDL view. For additional information on TMDL view, see [TMDL view](/power-bi/transform-model/desktop-tmdl-view).


#### General form

```tmdl
createOrReplace
    /// Optional description above the function
    function <FunctionName> = ( [ParameterName]: [ParameterType], ... ) => <FunctionBody>
```


#### Example: Simple tax function

```tmdl
createOrReplace
    /// AddTax takes in amount and returns amount including tax
    function AddTax = 
        (amount : NUMERIC) =>
            amount * 1.1
```


#### Saving to the model

Click the **Apply** button at the top of the view to save all UDFs in the script to the model.

:::image type="content" source="media/dax-user-defined-functions/view-save-to-model.png" alt-text="Screenshot of TMDL view in Power BI Desktop, highlighting the Apply button at the top of the view. This is the location where you can save a user-defined function." lightbox="media/dax-user-defined-functions/view-save-to-model.png":::


#### Using TMDL script in a Power BI Project

UDFs are also included in the semantic model TMDL script when using a [Power BI project](/power-bi/developer/projects/projects-overview). They can be found in `functions.tmdl` within the *definition* folder.

:::image type="content" source="media/dax-user-defined-functions/project-script.png" alt-text="Visual Studio Code screenshot of a Power BI project. Explorer is open to the semantic model folder. 'functions.tmdl' is open in the code editor. Three functions are displayed: CustomerLifetimeValue, AverageOrderValue, and AddTax." lightbox="media/dax-user-defined-functions/project-script.png":::


### Using Model explorer

You can view all user-defined functions in the model from Model explorer under the *Functions* node. For additional information on Model explorer, see [Model explorer](/power-bi/transform-model/model-explorer).

:::image type="content" source="media/dax-user-defined-functions/model-explorer-view-functions.png" alt-text="Model explorer panel in Power BI Desktop showing the expanded Functions node. Three user-defined functions are listed: AddTax, AverageOrderValue, and CustomerLifetimeValue." lightbox="media/dax-user-defined-functions/model-explorer-view-functions.png":::

In [DAX query view](#using-dax-query-view), you can use **Quick queries** in the right-click menu of a UDF within Model explorer to easily define and evaluate functions.

:::image type="content" source="media/dax-user-defined-functions/model-explorer-quick-queries.png" alt-text="Model explorer pane in Power BI Desktop displays the expanded Functions node. Two context menus are open: the first menu provides Quick queries, Rename, Delete from model, Hide in report view, Unhide all, Collapse all, and Expand all. Quick queries is highlighted and selected. The second menu is highlighted and offers Quick queries options Evaluate, Define and evaluate, Define new function, and Define all functions in this model." lightbox="media/dax-user-defined-functions/model-explorer-quick-queries.png":::

In [TMDL view](#using-tmdl-view), you can **drag and drop** functions into the canvas or use **Script TMDL to** in the right-click menu of a UDF within Model explorer to generate scripts.

:::image type="content" source="media/dax-user-defined-functions/model-explorer-script-to.png" alt-text="Model explorer pane in Power BI Desktop displays the expanded Functions node. Two context menus are open: the first menu provides Script TMDL to, Rename, Delete from model, Hide in report view, Unhide all, Collapse all, and Expand all. Script to TMDL is highlighted and selected. The second menu is highlighted and offers Script to TMDL options Script tab and Clipboard." lightbox="media/dax-user-defined-functions/model-explorer-script-to.png":::

### Using DMVs to inspect UDFs

You can inspect UDFs in your model using [Dynamic Management Views](/analysis-services/instances/use-dynamic-management-views-dmvs-to-monitor-analysis-services?) (DMVs). These views allow you to query information about functions, including UDFs.

You can use the [INFO.FUNCTIONS](..\info-functions-dax.md) function to inspect the UDFs in the model. To restrict the result to UDFs only, specify the `ORIGIN` parameter as `2`.

```dax
EVALUATE INFO.FUNCTIONS("ORIGIN", "2")
```

This query returns a table of all UDFs currently in the model, including their name, description, and associated metadata.


## Using a user-defined function

Once a UDF is defined and saved to the model, you can call it from measures, calculated columns, visual calculations, and other UDFs. This works the same as calling built-in DAX functions.


### Calling a UDF in a measure

Use a UDF in a measure to apply reusable logic with full filter context.

```dax
Total Sales with Tax = AddTax ( [Total Sales] )
```

The example measure is shown in the table below:

:::image type="content" source="media/dax-user-defined-functions/measure.png" alt-text="Table showing Total Sales and Total Sales with Tax. Total Sales with Tax is highlighted. Visualizations pane is open. Total Sales with Tax is highlighted in the Columns field well." lightbox="media/dax-user-defined-functions/measure.png":::


### Calling a UDF in a calculated column

UDFs can be used in a calculated column to apply reusable logic to every row in a table.

> [!NOTE]
> When using a UDF in a calculated column, ensure the function returns a scalar of a consistent type. See [Parameters](#parameters) for more information. If needed, convert the result to the desired type using [CONVERT](../convert-function-dax.md) or similar functions.

```dax
Sales Amount with Tax = CONVERT ( AddTax ( 'Sales'[Sales Amount] ), CURRENCY )
```

We can see this example measure used in the table below:

:::image type="content" source="media/dax-user-defined-functions/calculated-column.png" alt-text="Table showing Sales Amount and Sales amount with Tax. Sales Amount with Tax is highlighted. Visualizations pane is open. Sales Amount with Tax is highlighted in the Columns field well." lightbox="media/dax-user-defined-functions/calculated-column.png":::


### Calling a UDF in a visual calculation

You can use UDFs in a visual calculation to apply logic directly to the visual. For additional information on visual calculations, see [Visual Calculations](/power-bi/transform-model/desktop-visual-calculations-overview).

> [!NOTE]
> Visual calculations only operate on fields present in the visual. They cannot access model objects that aren't part of the visual, and you cannot pass model objects (such as columns or measures not in the visual) into a UDF in this context.

```dax
Sales Amount with Tax = AddTax ( [Sales Amount] )
```

We can see this example measure in the table below:

:::image type="content" source="media/dax-user-defined-functions/visual-calculation.png" alt-text="In visual calculation edit mode. Table showing Sales Amount and Sales amount with Tax. Sales Amount with Tax is highlighted. Visual calculation formula for Sales amount with Tax is highlighted." lightbox="media/dax-user-defined-functions/visual-calculation.png":::


### Calling a UDF in another UDF

You can nest UDFs by calling a function from another. In this example we define our simple `AddTax` UDF and call it in another UDF, `AddTaxAndDiscount`.

```dax
DEFINE
    /// AddTax takes in amount and returns amount including tax
    FUNCTION AddTax = 
        ( amount : NUMERIC ) =>
            amount * 1.1

	FUNCTION AddTaxAndDiscount = 
        (
			amount : NUMERIC,
			discount : NUMERIC
		) =>
		    AddTax ( amount - discount )

EVALUATE
{ AddTaxAndDiscount ( 10, 2 ) }
// Returns 8.8
```


## Parameters

DAX UDFs can accept zero or more parameters. When you define parameters for a UDF, you can optionally specify type hints for each parameter:
- **Type**: what type of value the parameter accepts (`AnyVal`, `Scalar`, `Table`, or `AnyRef`).
- **Subtype** (only for scalar type): the specific scalar data type (`Variant`, `Int64`, `Decimal`, `Double`, `String`, `DateTime`, `Boolean`, or `Numeric`). 
- **ParameterMode**: when the argument is evaluated (`val` or `expr`).

Type hints are in the form: `[type] [subtype] [parameterMode]`

You can include all, some, or none of these type hints for each parameter to make your functions safer and more predictable at call sites. If you omit everything and just write the parameter name it behaves as `AnyVal val`, meaning the argument is evaluated immediately at call time. This is useful for simple functions.


### Type

Type defines the category of argument your parameter accepts and whether it is passed as a **value** or an **expression**.

There are two type families in DAX UDF parameters: **value types** and **expression types**:
- **Value types**: this argument is **evaluated immediately** (eager evaluation) when the function is called and the resulting value is passed into the function.
    - **`AnyVal`**: Accepts a scalar or a table. This is the default if you omit type for a parameter.
    - **`Scalar`**: Accepts a scalar value (can additionally add a subtype).
    - **`Table`**: Accepts a table.
- **Expression types**: this argument passes an **unevaluated expression** (lazy evaluation). The function decides when and in what context to evaluate it. This is required for reference parameters and useful when you need to control filter context (e.g. inside [CALCULATE](../calculate-function-dax.md)). `expr` types can be references to a column, table, calendar, or measure.
    - **`AnyRef`**: Accepts a reference (a column, table, calendar, or measure).


### Subtype

Subtype lets you define a specific `Scalar` data type. If you define a subtype, you do not need to explicitly define the parameter as a `Scalar` type, this is automatically assumed.

Subtypes are:
- **`Variant`**: Accepts any scalar.
- **`Int64`**: Accepts a whole numner.
- **`Decimal`**: Accepts a fixed-precision decimal (such as Currency or Money).
- **`Double`**: Accepts a floating-point decimal.
- **`String`**: Accepts text.
- **`DateTime`**: Accepts date/time.
- **`Boolean`**: Accepts TRUE/FALSE.
- **`Numeric`**: Accepts any numerical value (`Int64`, `Decimal`, or `Double` subtypes)


### ParameterMode

ParameterMode controls when and where the parameter expression is evaluated. These are:
- **`val` (eager evaluation)**: The expression is evaluated once before invoking the function. The resulting value is then passed into the function. This is common for simple scalar or table inputs. This is the default if you omit parameterMode for a parameter.
- **`expr` (lazy evaluation)**: The expression is evaluated inside the function, potentially in a different context (e.g. row context or filter context) and possibly multiple times if referenced multiple times or inside iterations. This is required for reference parameters and useful when you need to control evaluation context.

The `Scalar` type can use either `val` or `expr`. Use `val` when you want the scalar evaluated once in the caller's context. Use `expr` when you want to defer evaluation and possibly apply context inside the function. See [Example: Table parameter](#example-table-parameter-value-vs-expression) as an example.

The `AnyRef` type must be `expr` as its references (columns, tables, measures, etc.) need to be evaluated in the function's context.


### Example: Type casting

```dax
DEFINE
    /// returns x cast to an Int64
    FUNCTION CastToInt = (
            x : SCALAR INT64 VAL
        ) =>
        x

EVALUATE
{ CastToInt ( 3.4 ), CastToInt ( 3.5 ), CastToInt ( "5" ) }
// returns 3, 4, 5
```

This uses a `Scalar` type, `Int64` subtype, and `val` parameterMode for predictable rounding and text-to-number coercion, as well as ensuring any expressions are eagerly evaluated. You can also achieve this by just including the `Int64` subtype as seen in the example below. Non-numeric strings will result in an error.

```dax
DEFINE
    /// returns x as an Int64
    FUNCTION CastToInt = (
            x : INT64
        ) =>
        x

EVALUATE
{ CastToInt ( 3.4 ), CastToInt ( 3.5 ), CastToInt ( "5" ) }
// returns 3, 4, 5
```


### Example: Table parameter (value vs expression)

To illustrate how UDF parameterMode affects filter context consider two functions that both count rows in the 'Sales' table. Both use `CALCULATETABLE(t, ALL('Date'))` in their bodies, but one parameter is declared as a `val` (eager evaluation) and the other as `expr` (lazy evaluation):

```dax
DEFINE
    /// Table val: receives a materialized table, context can't be changed
    FUNCTION CountRowsNow = (
            t : TABLE VAL
        ) =>
        COUNTROWS ( CALCULATETABLE ( t, ALL ( 'Date' ) ) )
    
    /// Table expr: receives an unevaluated expression, context CAN be changed
    FUNCTION CountRowsLater = (
            t : TABLE EXPR
        ) =>
        COUNTROWS ( CALCULATETABLE ( t, ALL ( 'Date' ) ) )

EVALUATE
{
    CALCULATE ( CountRowsNow ( 'Sales' ), 'Date'[Fiscal Year] = "FY2020" ),
    CALCULATE ( CountRowsLater ( 'Sales' ), 'Date'[Fiscal Year] = "FY2020" )
}
// returns 84285, 121253
```

CountRowsNow returns the count of sales for FY2020 only. The 'Sales' table is already filtered by the year before entering the function, so `ALL('Date')` inside the function has no effect.

CountRowsLater returns the count of sales for all years. The function receives an unevaluated table expression and evaluates it under `ALL('Date')`, removing the external year filter.


## Type checking

Type checking in UDFs can be done with new and existing type checking functions you can call inside your function body to confirm the runtime type of passed parameters. This allows UDFs to use context control, validate parameters up front, normalize inputs before calculation.

> [!NOTE]
> For `expr` parameterMode parameters, type checks occur when the parameter is referenced in the function body (not at function call time).


### Available type checking functions

UDFs can use the following functions to test scalar values. Each return `TRUE`/`FALSE` depending on whether the value provided is of that type.

| Category     | Functions                                                                             |        
|--------------|---------------------------------------------------------------------------------------|
| Numeric      | [ISNUMERIC](../isnumeric-function-dax.md), [ISNUMBER](../isnumber-function-dax.md)    |
| Double       | [ISDOUBLE](../isdouble-function-dax.md)                                               |
| Whole number | [ISINT64](../isint64-function-dax.md), [ISINTEGER](../isinteger-function-dax.md)      |
| Decimal      | [ISDECIMAL](../isdecimal-function-dax.md), [ISCURRENCY](../iscurrency-function-dax.md)|
| String       | [ISSTRING](../isstring-function-dax.md), [ISTEXT](../istext-function-dax.md)          |
| Boolean      | [ISBOOLEAN](../isboolean-function-dax.md), [ISLOGICAL](../islogical-function-dax.md)  |
| Date and Time| [ISDATETIME](../isdatetime-function-dax.md)                                           |


### Example: Check if parameter is a string

```dax
DEFINE
    /// Returns the length of a string, or BLANK if not a string
    FUNCTION StringLength = (
            s
        ) =>
        IF ( ISSTRING ( s ), LEN ( s ), BLANK () )

EVALUATE
{ StringLength ( "hello" ), StringLength ( 123 ) }
// Returns: 5, BLANK
```
This prevents errors and allows you to decide how to handle non-string input into the function (in this example, returns `BLANK`).


### Example: Accept multiple parameter types

```dax
DEFINE
    /// Helper 1: get currency name by int64 key
    FUNCTION GetCurrencyNameByKey = (
            k : INT64
        ) =>
        LOOKUPVALUE ( 'Currency'[Currency], 'Currency'[CurrencyKey], k )
    
    /// Helper 2: get currency name by string code
    FUNCTION GetCurrencyNameByCode = (
            code : STRING
        ) =>
        LOOKUPVALUE ( 'Currency'[Currency], 'Currency'[Code], code )
    
    /// Accepts key (int64) or code (string) and returns the currency name
    FUNCTION GetCurrencyName = (
            currency
        ) =>
        IF (
            ISINT64 ( currency ),
            GetCurrencyNameByKey ( currency ),
            GetCurrencyNameByCode ( currency )
        )

EVALUATE
{ GetCurrencyName ( 36 ), GetCurrencyName ( "USD" ) }
// returns "Euro", "US Dollar"
```

This example shows how to use type checking in UDFs to safely accept multiple input types and return a single, predictable result. `GetCurrencyName` takes one argument, `currency`, which can be either a whole-number currency key or a text currency code. The function checks the argument type with `ISINT64`. If the input is an integer, it calls the helper `GetCurrencyNameByKey` that looks up the currency name based on the currency key. If the input is not an integer, it calls the helper `GetCurrencyNameByCode` that looks up the currency name based on the currency code.


## Define multiple functions at once

UDFs allow you to define several functions in a single query or script, making it easy to organize reusable logic. This is especially useful when you want to encapsulate related calculations or helper routines together. Functions can be evaluated together or individually.

```dax
DEFINE
    /// Multiplies two numbers
    FUNCTION Multiply = (
            a,
            b
        ) =>
        a * b

    /// Adds two numbers and 1
    FUNCTION AddOne = (
            x,
            y
        ) =>
        x + y + 1

    /// Returns a random integer between 10 and 100
    FUNCTION RandomInt = () =>
        RANDBETWEEN ( 10, 100 )

EVALUATE
{ Multiply ( 3, 5 ), AddOne ( 1, 2 ), RandomInt () }
// returns 15, 4, 98
```


## Advanced example: Flexible currency conversion

To show how DAX UDFs can handle more complex logic we will look at a currency conversion scenario. This example uses type checking and nested functions to convert a given amount into a target currency using either the average or end-of-day exchange rate for a given date.

```tmdl
createOrReplace
	function ConvertDateToDateKey =  
		( 
			pDate: scalar variant 
		) => 
		YEAR ( pDate ) * 10000 + MONTH ( pDate ) * 100 + DAY ( pDate ) 
	
	function ConvertToCurrency = 
		( 
			pCurrency:scalar variant, 
			pDate: scalar variant, 
			pUseAverageRate: scalar boolean, 
			pAmount: scalar decimal 
		) => 
		var CurrencyKey = 
			EVALUATEANDLOG ( 
				IF ( 
					ISINT64 ( pCurrency ), 
					pCurrency, 
					CALCULATE ( 
						MAX ( 'Currency'[CurrencyKey] ), 
						'Currency'[Code] == pCurrency 
					) 
				) 
				, "CurrencyKey" 
			) 

		var DateKey = 
			EVALUATEANDLOG ( 
				SWITCH ( 
					TRUE, 
					ISINT64 ( pDate ), pDate, 
					ConvertDateToDateKey ( pDate ) 
				) 
				, "DateKey" 
			) 

		var ExchangeRate = 
			EVALUATEANDLOG ( 
				IF ( 
					pUseAverageRate, 
					CALCULATE ( 
						MAX ( 'Currency Rate'[Average Rate] ), 
						'Currency Rate'[DateKey] == DateKey, 
						'Currency Rate'[CurrencyKey] == CurrencyKey 
					), 
					CALCULATE ( 
					MAX ( 'Currency Rate'[End Of Day Rate] ), 
						'Currency Rate'[DateKey] == DateKey, 
						'Currency Rate'[CurrencyKey] == CurrencyKey 
					) 
				) 
				, "ExchangeRate" 
			) 

		var Result = 
			IF ( 
				ISBLANK ( pCurrency ) || ISBLANK ( pDate ) || ISBLANK ( pAmount ), 
				BLANK (), 
				IF ( 
					ISBLANK ( ExchangeRate ) , 
					"no exchange rate available", 
					ExchangeRate * pAmount 
				) 
			) 

		RETURN Result
```

The `ConvertToCurrency` function accepts flexible input types for both currency and date. Users can provide either a currency key or date key directly or supply a currency code or standard date value. The function checks the type of each input and handles it accordingly: if `pCurrency` is a whole number, it is treated as a currency key; otherwise, the function assumes a currency code and attempts to resolve the corresponding key. `pDate` follows a similar pattern, if it is a whole number, it is treated as a date key; otherwise the function assumes it is a standard date value and is converted to a date key using the `ConvertDateToDateKey` helper function. If the function cannot determine a valid exchnage rate, it returns the message "no exchange rate available".

This logic can then be used to define a measure such as **Total Sales in Local Currency**.

```dax
Total Sales in Local Currency = 
ConvertToCurrency (
    SELECTEDVALUE ( 'Currency'[Code] ),
    SELECTEDVALUE ( 'Date'[DateKey] ),
    TRUE,
    [Total Sales]
)
```

This can be optionally paired with a [dynamic format string](/power-bi/create-reports/desktop-dynamic-format-strings) to display the result in the appropriate currency format.

```dax
CALCULATE (
    MAX ( 'Currency'[Format String] ),
    'Currency'[Code] == SELECTEDVALUE ( 'Currency'[Code] )
)
```

An example result can be seen in the screenshot below.

:::image type="content" source="media/dax-user-defined-functions/advanced-example.png" alt-text="Table showing Full Date, Currency, Total Sales in Local Currency, and Total Sales." lightbox="media/dax-user-defined-functions/advanced-example.png":::


## Considerations and limitations

User-defined functions are currently in preview, and during preview, please be aware of the following considerations and limitations:

General:
- Cannot author or model DAX UDFs in Service.
- Cannot hide/unhide a UDF in the model.
- Cannot put UDFs in display folders.
- No 'create function' button in the ribbon.
- Cannot combine UDFs with translations.
- UDFs are not supported in models without tables.
- No 'define with references' quick query in DAX query view.
- [Object-Level Security (OLS)](/fabric/security/service-admin-object-level-security) does not transfer to functions or vise versa. For example, consider the following function `F` that refers to secured measure `MyMeasure`:
    ```dax
    function F = () => [MyMeasure] + 42
    ```

    when the `MyMeasure` is secured using object-level security, function F is not secured automatically. If `F` runs under an identity without access to `MyMeasure`, it acts as if `MyMeasure` doesn’t exist. We recommend to avoid revealing secure objects in function names and descriptions.

Defining a UDF:
- Recursion or mutual recursion is not supported.
- Function overloading is not supported.
- Explicit return types not supported.

UDF parameters:
- Optional parameters are not supported.
- Parameter descriptions are not supported.
- UDFs cannot return an `enum` value. Built-in functions that accept `enum` values as their function parameters will not be able to use UDFs in that context.
- Unbound parameters of type hint `expr` are not evaluated.

IntelliSense Support:
- Although UDFs can be used in live connect or composite models, there is no IntelliSense support.
- Although UDFs can be used in visual calculations, the visual calculations formula bar does not have IntelliSense support for UDFs.
- TMDL view does not have proper IntelliSense support for UDFs.

### Known bugs

The following issues are currently known and may impact functionality:
- References to a tabular model object (e.g. measure, table, column) in a UDF are not automatically updated when those objects are renamed. If you rename an object that a UDF depends on, the function body will still contain the old name. You must manually edit the UDF expression to update all references to the renamed object.
- Certain advanced scenarios involving UDFs can result in parser inconsistencies. For example, users may see red underlines or validation errors when passing columns as `expr` parameters or using unqualified column references.


## Related content

- [DAX query view](/power-bi/transform-model/dax-query-view)
- [TMDL view](/power-bi/transform-model/desktop-tmdl-view)
- [Model explorer](/power-bi/transform-model/model-explorer)
