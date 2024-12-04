var x=In.ReadToEnd().Split('\n');
var a=x.Select(n=>int.Parse(n.Split()[0])).OrderBy(n=>n);
var b=x.Select(n=>int.Parse(n.Split()[^1])).OrderBy(n=>n);
Print(a.Zip(b, (n,m)=>Math.Abs(n-m)).Sum());
Print(a.Sum(n=>b.Count(m=>m==n)*n));