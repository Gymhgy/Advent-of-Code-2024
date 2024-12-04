var input=In.ReadToEnd().Split("\n").Select(x=>x.Split().Select(int.Parse));
bool Safe(IEnumerable<int> x)=>x.Zip(x.Skip(1), (a, b) => Math.Abs(a - b)).All(y => 1 <= y && y <= 3) && Math.Abs(x.Zip(x.Skip(1), (a, b) => Math.Sign(a - b)).Sum()) == x.Count() - 1;

Print(input.Count(Safe));
Print(input.Count(x => Safe(x) || Enumerable.Range(0, x.Count()).Any(i => Safe(x.Where((_, j) => i != j)))));