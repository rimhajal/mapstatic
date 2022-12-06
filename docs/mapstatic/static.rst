Consumption Prediction
=======================
Here, the steps of prediction's work will be detailed in three parts: the data, the preprocess and the model development.

Data  
^^^^^
French consumption data needed to be imported from the `government <https://odre.opendatasoft.com/explore/dataset/eco2mix-regional-cons-def/table/?disjunctive.libelle_region&disjunctive.nature&sort=-date_heure>`_ thanks to following class before being used in mapstatic's prediction part.

.. class:: datadownloading

This dataset is composed of the french consumption of different types of energy (global, thermal, nuclear, wind, solar, hydraulic,) every thirty minutes since 2013.

Preprocess
^^^^^^^^^^^
Now that dataset is imported, it has to be classified and cleaned.

Indeed, new dataframes are made for each type of energy including only variables of time and values of consumption in MW. The original dataset also contained NaN values (missing values) that had to be replaced by a mean of closed ones.
Another class was construct to do this job:

.. class:: datashaping

If one only wants to view the thermal dataframe for instance, one just has to write the following command in a python editor:

.. code-block:: python

    print(datashaping.datashaping.solardata())

The attempted output is a table like below:

+-------------+----------+----------+
|*date*       |*hour*    |*thermal* |
+=============+==========+==========+
|`...`        |`...`     | \...     |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \345.0   |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \5.0     |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \1220.0  |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \28.0    |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \883.0   |
+-------------+----------+----------+

Modelisation
^^^^^^^^^^^^^
How to use ?
""""""""""""
In order to predict the consumption of any energy on the 8th of December 2022, a last class was created.

.. class:: datamodeling

This class asks the user to choose a certain type of energy and returns a dataframe of the predicted consumption every thirty minutes and its associated graph.
One just has to write a command in an python editor as follows:

.. code-block:: python

    print(prediction.dataset())

Let's take the former example. If user writes 'thermal', the ouput will be:

+----------+-------------+
|*hour*    |*thermal*    |
+==========+=============+
|`00:00`   | \732.256944 |
+----------+-------------+
|`00:30`   | \715.935764 |
+----------+-------------+
|`01:00`   | \679.218750 |
+----------+-------------+
|`01:30`   | \684.390625 |
+----------+-------------+
|`...`     | \...        |
+----------+-------------+
|`23:30`   | \719.147569 |
+----------+-------------+

Then, the following graph will be displayed:

.. image:: ../_images/thermalprediction.pdf
   :align: center


What is the model behind ?
""""""""""""""""""""""""""
In order to predict consumption of all different types of energy, we had choosen to use a simple and understable method. Indeed, other methods are available but they need to know about time series which are a rather complicated mathematical problem.
Choosen method was to calculate some means of data.

First, we observed the behaviour of all energies'consumptions since 2013 to distinguish a tendency. For that, we used the ``datashaping`` class plotting all energies'dataframes.

.. code-block:: python

    datashaping.consumptiondata().plot(figsize=(20, 5), title="French Global Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.thermaldata().plot(figsize=(20, 5), title="French Thermal Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.nucleardata().plot(figsize=(20, 5), title="French Nuclear Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.winddata().plot(figsize=(20, 5), title="French Wind Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.solardata().plot(figsize=(20, 5), title="French Solar Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.hydraulicdata().plot(figsize=(20, 5), title="French Hydraulic Energy Consumption Since 2013", xlabel='Date', ylabel='MW')

Here, there is an annual pattern and not a significative increase or decrease of global consumption for instance.

 .. image:: ../_images/globalconsumption.pdf
   :align: center

This explains the fact that we have choosen to select all the data of global consumption from December of each year since 2013 to predict its value on the 8th December of 2022 thanks to the following class:

.. class:: prediction

The previous class selects the right data, averages them and finally plots them. As explained, the selected data depends on observable behaviour of dataframes.

Of course, there are several other parameters that we could take into account to have a better prediction like temperature, cost of each energy and man others that we don't have access to.



