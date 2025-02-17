from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Layout and Style",
)

text1 = """
# Row Styles
Row customisation can be achieved in the following ways:

- `Row Style`: Providing a CSS style for all rows.
- `Row Class`: Providing a CSS class for all rows.
- `getRowStyle`: Conditional formatting of rows based on cell values.


### Styling all rows
"""

text2 = """
### Conditional row style

 - `styleConditions` (list of dicts). Each dict has keys of "condition" and "style". The value of the "condition" key is a 
 JavaScript function that when True the value of the "style" key will be applied.
 
 In this example we use the data in the `sickDays` column.  For  example `"data.sickDays >= 8"` will apply a background color of "lightcoral".

```
getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.data.sickDays > 5 && params.data.sickDays <= 7",
            "style": {"backgroundColor": "sandybrown"},
        },
        {"condition": "params.data.sickDays >= 8", "style": {"backgroundColor": "lightcoral"}},
    ]
}
```
Here is how to use the row index to highlight alternating rows:

```
getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.node.rowIndex % 2 === 0",
            "style": {"backgroundColor": "lavenderblush"},
        },
    ]
}
```

The properties available are:
 - `data` The data associated with this row from rowData. Data is undefined for row groups.
- `node` The RowNode associated with this row
- `rowIndex` The index of the row
- `api` The grid api.
- `columnApi` The column api.
- `context` Application context as set on gridOptions.context.
"""

text3 = """

### Refresh of Styles
If you refresh a row, or a cell is updated due to editing, the `rowStyle`, `rowClass` and `rowClassRules` are all applied again. This has the following effect:

 - `rowStyle`: All new styles are applied. If a new style is the same as an old style, the new style overwrites the old style.
 - `rowClass`: All new classes are applied. Old classes are not removed so be aware that classes will accumulate. If you want to remove old classes, then use `rowClassRules`.
 - `rowClassRules`: Note!  This not yet available in dash-ag-grid.

"""


text4 = """
### Highlighting Rows and Columns
The grid can highlight both Rows and Columns as the mouse hovers over them.

Highlighting Rows is on by default. To turn it off, set the `dashGridOption` property `suppressRowHoverHighlight=True`.

Highlighting Columns is off by default. To turn it on, set the grid property `columnHoverHighlight=True`.

Note if you hover over a header group, all columns in the group will be highlighted.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.row_styling", make_layout=make_tabs),
        make_md(text2),
        make_md(text3),
        example_app("examples.layout.row_styling_conditional", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.layout.row_styling_highlights", make_layout=make_tabs),
        # up_next("text"),
    ],
)
