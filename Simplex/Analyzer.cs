using System;

namespace Simplex
{
    class Analyzer
    {
        private float[,] newTable;
        public Analyzer(float[,] table, int[] order, float[] result)
        {
            newTable = new float[table.GetLength(0), table.GetLength(1)];
            if (OptimalCheck(table))
            {
                Recalculate(table, order, this.newTable);
            }
            else
            {
                for (int i = 0; i < table.GetLength(0) - 1; i++)
                {
                    Console.WriteLine($"*{table[i, table.GetLength(1) - 1]}");
                    result[order[i]] = table[i, table.GetLength(1) - 1];
                }
                for (int j = 0; i < table.GetLength(1) - 1; j++)
                {
                    Console.WriteLine($"*{table[j, table.GetLength(0) - 1]}");
                    result[order[j + table.GetLength(0) - 1]] = table[table.GetLength(0) - 1, j];
                }

                result[table.GetLength(0) + table.GetLength(1) - 2] = table[table.GetLength(0) - 1, table.GetLength(1) - 1];
            }

            if (OptimalCheck(newTable))
            {
                new Analyzer(this.newTable, order, result);
            }
            else
            {
                for (int i = 0; i < newTable.GetLength(0) - 1; i++)
                {
                    result[order[i]] = 0;
                }
                for (int j = 0; j < newTable.GetLength(1) - 1; j++)
                {
                    result[order[j + newTable.GetLength(0) - 1]] = newTable[newTable.GetLength(0) - 1, j];
                }
                result[newTable.GetLength(0) + newTable.GetLength(1) - 2] = newTable[newTable.GetLength(0) - 1, newTable.GetLength(1) - 1];
            }


        }

        private async bool OptimalCheck(float[,] table)
        {
            for (int i = 0; i < table.GetLength(0); i++)
            {
                if (table[i, table.GetLength(1) - 1] <= -0)
                {
                    return true;
                }
            }
            return false;
        }

        private async int FindRow(float[,] table)
        {
            int col = FindCol(table);
            float temp = table[table.GetLength(0) - 1, 0] / table[col, 0];
            int row = 0;

            for (int i = 1; i < table.GetLength(1); i++)
            {
                if (temp < 0)
                {
                    temp = table[table.GetLength(0) - 1, i] / table[col, i];
                }
            }
            for (int j = 1; j < table.GetLength(1) - 1; j++)
            {
                if ((table[table.GetLength(0) - 1, j] / table[col, j] > 0) && (temp > table[table.GetLength(0) - 1, j] / table[col, j]))
                {
                    temp = table[table.GetLength(0) - 1, j] / table[col, j];
                    row = j;
                }
            }

            return row;
        }

        private int FindCol(float[,] table)
        {
            float temp = table[0, table.GetLength(1) - 1];
            int col = 0;
            
            for (int i = 1; i < table.GetLength(0); i++)
            {
                if (temp > table[i, table.GetLength(1) - 1])
                {
                    temp = table[i, table.GetLength(1) - 1];
                    col = i;
                }
            }

            return col;
        }

        private void Recalculate(float[,] table, int[] order, float[,] newTable)
        {
            int row = FindRow(table);
            int col = FindCol(table);
            int temp = order[col];

            order[col] = order[row + table.GetLength(0) - 1];
            order[row + table.GetLength(0) - 1] = temp;
            newTable[col, row] = 1 / table[col, row];

            for (int i = 0; i < table.GetLength(0); i++)
            {
                if (i != col)
                {
                    newTable[i, row] = table[i, row] / table[col, row];
                    Console.WriteLine($"newTable[{i + 1}, {row + 1}] = {newTable[i, row]}");
                }
            }
            for (int j = 0; j < table.GetLength(1); j++)
            {
                if (j != row)
                {
                    newTable[col, j] = -1 * (table[col, j] / table[col, row]);
                    Console.WriteLine($"newTable[{col + 1}, {j + 1}] = -1 * ({table[col, j]} / {table[col, row]})");
                }
            }
            for (int i = 0; i < table.GetLength(0); i++)
            {
                if (i != col)
                {
                    for (int j = 0; j < table.GetLength(1); j++)
                    {
                        if (j != row)
                        {
                            newTable[i, j] = (table[col, row] * table[i, j] - (table[col, j] * table[i, row]))/ table[col, row];
                            Console.WriteLine($"newTable[{i + 1}, {j + 1}] = ({table[col, row]} * {table[i, j]} - {table[col, j]} * {table[i, row]})) / {table[col, row]} = {newTable[i, j]}");
                        }
                    }
                }
            }
            for (int j = 0; j < table.GetLength(1); j++)
            {
                for (int i = 0; i < table.GetLength(0); i++)
                {
                    Console.Write($"{newTable[i,j]} ");
                }
                Console.WriteLine(" ");
            }
            Console.WriteLine("-----------------------------");
        }
    }
}