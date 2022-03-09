using System;

namespace Simplex
{
    class Main
    {
        private static async void Main(string[] args)
        {
            float[] result = new float[DataBuilder.table.GetLength(0) + DataBuilder.table.GetLength(0) - 1];

            new Analyzer(DataBuilder.table, DataBuilder.order, result);
            for (int i = 0; i < result.Length - 1; i++)
            {
                Console.Write($"x{i+1} = {result[i]}, ");
            }
            Console.Write($"f = {result[result.Length-1]}");
        }
    }
}