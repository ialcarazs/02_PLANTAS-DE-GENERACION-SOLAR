{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1227a1c6",
   "metadata": {},
   "source": [
    "Como acceder desde otros notebooks. \n",
    "    - Tienen que estar en el mismo directorio para poder acceder\n",
    "\n",
    "            %%capture\n",
    "            %run mis_funciones.ipynb\n",
    "\n",
    "\n",
    "Para acceder desde otros IDE se tiene que utilizar la extensión de Python .py\n",
    "    - Tienen que estar en el mismo directorio para poder acceder\n",
    "\n",
    "    import mis_funciones as mf\n",
    "    mf.componentes_fecha.."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67108715",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns\n",
    "\n",
    "%config IPCompleter.greedy = True "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4737770e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def componentes_fecha (dataframe):\n",
    "    ano = dataframe.index.year\n",
    "    mes = dataframe.index.month\n",
    "    dia = dataframe.index.day\n",
    "    hora = dataframe.index.hour\n",
    "    minuto = dataframe.index.minute\n",
    "    \n",
    "    fechas = pd.DataFrame(({'ano':ano ,'mes':mes ,'dia':dia ,'hora':hora ,'minuto':minuto}))\n",
    "    \n",
    "    return pd.concat([dataframe.reset_index(),fechas], axis=1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
