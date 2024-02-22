"""Graphic library to ease plotting."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.figure import Figure


def timeline(
    df: pd.DataFrame,
    x_start: str,
    x_end: str,
    y_col: str,
    text: str,
    color: str,
    title: str | None = None,
    **kwargs,
) -> Figure:
    """
    Plot Gantt chart.

    Parameters
    ----------
    df:
        Data for the chart.
    x_start:
        Name of the column for the start time of each operation.
    x_end:
        Name of the column for the end time of each operation.
    y_col:
        Name of the column for the name of the operation.
    text:
        Name of the column for the labels on the horizontal bar.
    color:
        Name of the column for the color of the bar.
    title:
        Optional title.
    kwargs:
        Extra argument such as `figsize`, `x_dt_format` to format the x axis ticks.

    Returns
    -------
    Figure of the Gantt chart.
    """
    figsize = kwargs.get("figsize", (12, 8))
    x_dt_format = kwargs.get("x_dt_format", "%H:%M:%S")

    fig, ax = plt.subplots(figsize=figsize)
    rects = ax.barh(
        y=df[y_col],
        width=(df[x_end] - df[x_start]) / np.timedelta64(1, "ms"),  # type: ignore
        left=(df[x_start] - df[x_start].min()) / np.timedelta64(1, "ms"),
        color=df[color],
    )
    ax.bar_label(rects, df[text], padding=2.5)
    ax.invert_yaxis()
    ax.set_xticks(
        ax.get_xticks(),
        labels=[
            pd.Timestamp(x, unit="ms").strftime(x_dt_format) for x in ax.get_xticks()
        ],
    )
    ax.set_xlabel("Time")
    ax.set_ylabel(y_col)
    ax.set_facecolor("#EAEAF2")
    ax.grid(axis="x", color="0.95", zorder=0)
    ax.set_axisbelow(True)

    if title:
        ax.set_title(title)

    plt.tight_layout()
    return fig
