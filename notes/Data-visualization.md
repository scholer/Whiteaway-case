


Visualization packages:

* matplotlib
* pandas
* seaborn
* holoview
* hvplot - "A high-level plotting API for pandas, dask, xarray, and networkx built on HoloViews"
* datashader - graphics pipeline for creating representations of large datasets.
* bokeh
* Altair
* Vizpy


Dashboards:

* Panel
* Lumen - based on top of Panel.


Visualization platforms and apps:

* Redash
* Plotly
* Apache Superset
* HoloViz - includes Bokeh, HoloViews, GeoViews, Matplotlib, Datashader, hvPlot, Panel, and Param



Apache Superset is a platform consisting of:

* Web application, including caching and APIs.
* Database interfaces to extract data. This is also a really big part of
* Dashboard builder (via graphical interfaces).
* Visualization.




## Installation notes:


You can also install pyviz packages from pyviz channel (they are also on conda-forge):

```
conda install -c pyviz holoviz
# or
conda install -c pyviz holoviews geoviews hvplot bokeh panel param datashader lumen
```

