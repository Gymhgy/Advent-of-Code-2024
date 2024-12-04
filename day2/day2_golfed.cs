var n=In.ReadToEnd().Split("\n").Select(x=>x.Split().Select(int.Parse));
bool S(IEnumerable<int>x)=>(x=x.Zip(x.Skip(1),(a,b)=>a-b)).All(y=>x.Last()*y>0&y*y<16);
Print(n.Count(S));
Print(n.Count(x=>x.Select((_,i)=>x.Where((_,j)=>j!=i)).Any(S)));