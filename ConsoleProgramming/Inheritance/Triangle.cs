class Triangle : Shape, IShape
{
    public Triangle()
    {

    }
    public Triangle(int hyp)
    {
        
    }
    public Triangle(int hyp, int height, int length)
    {
        Hypotenuese = hyp;
        Height = height;
        Length = length;
    }
    public double Hypotenuese { get; set; }

    public double getArea()
    {
        return .5 * Length * Height;
    }
}