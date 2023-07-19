# Imports
# -------

import click
import pandas as pd

@click.command
@click.option('--index', default=0, help='Drop a row in the file')

def controller(
  index
):

  dataframe = pd.read_csv('./chemical_list.csv', header=None, usecols=[0])
  df = dataframe.drop(index=109, inplace=False)
  df.to_csv('./chemical_list.csv', index=False, header=False)
  print (df)

if __name__ == '__main__':

    controller()
